## Python 3.12 vs TF Lite 2.17

The latest versions of TF Lite don't support Python 3.12 yet. 

As a workaround, we can use the previous version of TF Lite 
to serve the models created by TensorFlow 2.17. We tested 
it with TF Lite 2.14 and the deep learning models we use
in the course work successfully with this setup.

Here's how you do it


First, use Python 3.10. It means that you will need to use
`public.ecr.aws/lambda/python:3.10` as the base image:

```docker 
FROM public.ecr.aws/lambda/python:3.10
```

Second, use numpy 1.23.1:

```docker
RUN pip install numpy==1.23.1
```

When installing tf lite interpreter for AWS lambda, 
make sure you don't install dependencies with `--no-deps` flag:

```docker
RUN pip install --no-deps https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl
```

If you don't do it, pip will try to upgdate the version of numpy
and your code won't work (as the tflite runtime was compiled 
with numpy 1, not numpy 2).





