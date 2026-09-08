---
video_url: "https://www.youtube.com/watch?v=y4_YQjfOsDo&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"
code:
  - label: Test script
    path: code/test.py
---
# Preparing a Docker image

In the previous lesson we converted the notebook to a Python script
and tested it locally. Now we package everything - the script and the
model - into a Docker image, so that we can later deploy it to AWS
Lambda. We build the image, run it as a container, and send a test
request to it.

> Note: the materials in this unit are outdated.
> 
> Refer to the [ONNX Workshop](workshop/) for the up-to-date materials.

## The Dockerfile

We create a file called `Dockerfile`. The first line is the `FROM`
instruction - the base image. AWS prepares ready-made base images for
Lambda. They live in a public registry: go to public.ecr.aws (it
redirects to a gallery of public AWS images), search for "lambda
python", and open the Python image maintained by AWS Lambda. In the
"image tags" tab we see all the available tags; we pick the one for
Python 3.8:

Next, we install the dependencies. We need keras-image-helper, and we
need the TF-Lite runtime. For the runtime we use the same install
command we used in the notebook, which points pip to the extra index
of the google-coral project:

```dockerfile
FROM public.ecr.aws/lambda/python:3.8

RUN pip install keras-image-helper
RUN pip install --extra-index-url \
    https://google-coral.github.io/py-repo/ tflite_runtime

COPY clothing-model.tflite .
COPY lambda_function.py .

CMD [ "lambda_function.lambda_handler" ]
```

We don't install NumPy or Pillow explicitly: keras-image-helper
depends on both, and tflite-runtime depends on NumPy, so pip pulls
them in automatically.

The two `COPY` lines put the model and the script inside the image.
The last line, `CMD`, tells Lambda where the entry point of our
function is: it lives in the `lambda_function.py` file, in the
`lambda_handler` function. Exactly how `CMD` translates to the handler
is a bit mysterious - the Lambda base images specify an ENTRYPOINT
already, and we only overwrite the arguments passed to it.

## Building and running the image

Build the image:

```bash
docker build -t clothing-model .
```

The dot means "use the Dockerfile from the current directory". Docker
pulls the base image and executes all the instructions.

Then run the container:

```bash
docker run -it --rm -p 8080:8080 clothing-model:latest
```

The Lambda base image listens on port 8080, so we publish it locally
with `-p 8080:8080`.

## Testing the container

Now we want to send a request to the container and see if it replies
with predictions. Create a small script, `test.py`:

```python
import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'url': 'http://bit.ly/mlbookcamp-pants'}

result = requests.post(url, json=data).json()
print(result)
```

The URL looks strange, but that's how AWS does it: this long path
(`/2015-03-31/functions/function/invocations`) is the local endpoint
the Lambda base image exposes. We send a POST request with a JSON
body containing the URL of the pants picture - the same payload we'll
use in production.

Run it:

```bash
python test.py
```

And we get an error.

## Error 1: the wheel was compiled for a different Linux

The first error says that the module `lambda_function` cannot be
imported: the underlying TF-Lite library was compiled against a
version of GLIBC that doesn't exist in the container:

```text
Unable to import module 'lambda_function':
/lib64/libm.so.6: version `GLIBC_2.27' not found
(required by /var/lang/lib/python3.8/site-packages/tflite_runtime/...)
```

The reason: all Lambda images are based on Amazon Linux, which is a
CentOS-based distribution. The tflite-runtime binary we installed
from the google-coral index was compiled for a Debian-based
distribution like Ubuntu - that's why it worked on my laptop but not
here.

The fix: TF-Lite must be compiled in the same environment where it
will run. I went through the trouble of compiling it for Amazon Linux
and published the precompiled wheels in the
[tflite-aws-lambda](https://github.com/alexeygrigorev/tflite-aws-lambda)
repository. The README there explains how to compile it yourself for
different Python and TensorFlow versions, but you can simply take a
ready wheel: we use Python 3.8 and TensorFlow 2.7.0, so we take the
matching one:

With `pip install` you can pass a URL to a wheel file instead of a
package name, and pip downloads and installs it. So we replace the
tflite-runtime line in the Dockerfile:

```dockerfile
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp38-cp38-linux_x86_64.whl
```

(One note on tooling: here I use plain `pip install` in the
Dockerfile, not a dependency manager like pipenv. This library is
tricky in the sense that different environments need different
binaries - one wheel for my local laptop, another one for the Docker
image - so I keep the two installs separate.)

Rebuild the image:

Then run the container again and test.

## Error 2: float32 is not JSON serializable

Now we get a different error - and this one is expected, we have seen
it before in the Flask sessions:

```text
Unable to marshal response: Object of type float32 is not JSON
serializable
```

The predictions are a NumPy array of `float32` values, and JSON doesn't
know how to serialize NumPy types. We need to convert them to usual
Python floats. In `lambda_function.py`, inside `predict`, convert the
array to a list:

```python
float_predictions = preds[0].tolist()

return dict(zip(classes, float_predictions))
```

`tolist()` takes a NumPy array and converts it to a usual Python list
with usual Python floats - and those are serializable.

Rebuild, run, and test once more. This time it works: we get back the
dictionary of scores with "pants" on top, plus some statistics like
the duration of the request.

So now we have taken the code from the notebook, put it into a script,
packaged the script with the model into a Docker image, and verified
that the container works. In the next lesson we deploy this image to
AWS Lambda.

## Notes

Refer to [updates.md](updates.md) for info on running TF lite
in 2024. 

### Using `pip install` for TF-Lite binaries

When using `pip` to install the compiled binary, make sure you use the raw file, not a link to the github page.

Correct:

```bash
pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl
```


(Note `/raw/` in the path)

Also correct:

```bash
pip install https://github.com/alexeygrigorev/tflite-aws-lambda/blob/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl?raw=true
```

The wheel file above is for Python 3.10. Check other available compiled TF lite versions [here](https://github.com/alexeygrigorev/tflite-aws-lambda/tree/main/tflite).


Not correct - won't work:

```bash
pip install https://github.com/alexeygrigorev/tflite-aws-lambda/blob/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl
```

If the file is incorrect, you'll get an error message like that: 

```
zipfile.BadZipFile: File is not a zip file
```

### `ENTRYPOINT` vs `CMD`

This link explains the difference between them: https://stackoverflow.com/a/34245657

> `ENTRYPOINT` specifies a command that will always be executed when the container starts.
> `CMD` specifies arguments that will be fed to the `ENTRYPOINT`.

In case of the lambda base pacakge, the authors already specified the entrypoint and
we only need to overwrite the arguments passed to the entrypoint,


<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>

* [Notes from Peter Ernicke](https://knowmledge.com/2023/12/04/ml-zoomcamp-2023-serverless-part-5/)
