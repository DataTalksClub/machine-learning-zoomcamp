# Serverless screenshot rollout: lessons 01-04

Capability check: this worker has the `imagegen` skill and used the built-in
imagegen workflow only for bounded explanatory diagrams. Exact code, command,
URL, UI, plot, and numeric screenshots use deterministic crops/upscaling.
Original source assets remain in place.

## 01-intro-01-clothes-classification-use-case.jpg

- **Disposition:** `crop/replace` → `images/01-intro-01-clothes-classification-use-case-imagegen.png`
- **Teaching point:** a user uploads a pants photo; a clothes-classification service returns `PANTS` to the classifieds website.
- **Source inspection:** 592×360; source crop `+22+0 480×360` removed the black frame and webcam tile before generation.
- **Method:** imagegen `scientific-educational` redraw from the clean crop; required `CLOTHES CLASSIFICATION SERVICE` and `PANTS`, two-way upload/result flow; no camera, face tile, controls, cursor, watermark, or extra service.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 2, caption/accessibility 2 — **12/12; keep**.
- **Validation:** generated image inspected at 1536×1024; labels and flow match the caption; no face/camera/recording overlay; Markdown reference resolves.

## 01-intro-02-aws-lambda-deployment.jpg

- **Disposition:** `crop/replace` → `images/01-intro-02-aws-lambda-deployment-imagegen.png`
- **Teaching point:** a picture URL is sent to the Lambda-hosted model, which returns classes and scores including `PANTS`.
- **Source inspection:** 592×360; source crop `+22+0 408×360` excluded the black frame, webcam tile, and recording overlay before generation.
- **Method:** imagegen `scientific-educational` redraw with exact labels `PICTURE URL`, `AWS LAMBDA`, `CLASSES + SCORES`, and `PANTS`; first draft was rejected because it invented numeric probabilities, then a targeted edit replaced all numbers with qualitative score bars.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 2, caption/accessibility 2 — **12/12; keep**.
- **Validation:** corrected output inspected at 1691×930; required labels, request/response directions, and strongest `PANTS` score bar match the lesson; no face/camera/recording overlay or invented numeric value; Markdown reference resolves.

## 01-intro-03-lambda-uses-tf-lite.jpg

- **Disposition:** `crop/replace` → `images/01-intro-03-lambda-uses-tf-lite-imagegen.png`
- **Teaching point:** the AWS Lambda service uses TensorFlow Lite internally to classify the pants image.
- **Source inspection:** 592×360; source crop `+22+0 408×360` excluded the black frame, webcam tile, and recording overlay before generation.
- **Method:** imagegen `scientific-educational` redraw with the exact labels `AWS LAMBDA`, `TF-LITE`, and `PANTS`; Lambda contains the TF-Lite inference component and arrows show the data flow.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 2, caption/accessibility 2 — **12/12; keep**.
- **Validation:** generated image inspected at 1835×857; labels, containment relationship, and arrows match the caption; no face/camera/recording overlay or invented metric; Markdown reference resolves.

## 02-aws-lambda-07-serverless-vs-serverful.jpg

- **Disposition:** `crop/replace` → `images/02-aws-lambda-07-serverless-vs-serverful-imagegen.png`
- **Teaching point:** Lambda activity and cost rise during daytime traffic and return to zero at night, illustrating pay-per-request behavior.
- **Source inspection:** 592×360; source crop `+22+0 408×360` removed the black frame, webcam tile, and recording control overlay.
- **Method:** imagegen `scientific-educational` redraw with a blue daytime curve, sun/moon contrast, red `$` marker under the active interval, and exact axis label `TIME`; no numeric axes or invented metrics.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 2, caption/accessibility 2 — **12/12; keep**.
- **Validation:** generated image inspected at 1660×948; day/night relationship, baseline, cost marker, and `TIME` label match the caption; no face/camera/recording overlay or numeric invention; Markdown reference resolves.

## 02-aws-lambda-01-search-lambda.jpg

- **Disposition:** `crop/replace` → `images/02-aws-lambda-01-search-lambda-cropped.png`
- **Teaching point:** the AWS console search identifies Lambda and shows its serverless promise.
- **Source inspection:** 592×360; deterministic crop `+0+20 500×316` removes the browser URL strip, webcam tile, and right-side black frame while retaining the AWS search UI.
- **Method:** deterministic Lanczos upscale to 1000×632 with light sharpening; exact UI text and labels were not regenerated.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `Lambda` and `Run Code without Thinking about Servers` remain readable, no face/camera/recording overlay remains, and Markdown reference resolves.

## 02-aws-lambda-02-create-function.jpg

- **Disposition:** `crop/replace` → `images/02-aws-lambda-02-create-function-cropped.png`
- **Teaching point:** the new Lambda function is configured with name `mlzoomcamp-test`, Python 3.9, and `x86_64` architecture.
- **Source inspection:** 592×360; deterministic crop `+0+20 500×316` removes the browser URL strip, webcam tile, and right-side black frame while retaining the form choices.
- **Method:** deterministic Lanczos upscale to 1000×632 with light sharpening; exact UI values were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; function name, runtime, architecture, and permissions text remain readable; no face/camera/recording overlay remains; Markdown reference resolves.

## 02-aws-lambda-03-pong-handler.jpg

- **Disposition:** `crop/replace` → `images/02-aws-lambda-03-pong-handler-cropped.png`
- **Teaching point:** the Lambda handler prints the event parameters and returns `PONG` before deployment.
- **Source inspection:** 592×360; deterministic crop `+0+20 500×316` removes the browser URL strip, webcam tile, and right-side black frame while retaining the exact code editor state.
- **Method:** deterministic Lanczos upscale to 1000×632 with light sharpening; exact code and deployment state were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `lambda_handler`, `print("parameters: ", event)`, and `return "PONG"` remain readable; no face/camera/recording overlay remains. A small native pointer/hover artifact over the code remains because removing it safely would alter exact UI pixels; Markdown reference resolves.

## 02-aws-lambda-04-test-pong-response.jpg

- **Disposition:** `crop/replace` → `images/02-aws-lambda-04-test-pong-response-cropped.png`
- **Teaching point:** after deployment, the test response is `PONG` and the function logs show the event parameters.
- **Source inspection:** 592×360; deterministic crop `+0+75 548×261` removes the browser strip, webcam tile, recording banner edge, and black frame while retaining the deployed status, response, and logs.
- **Method:** deterministic Lanczos upscale to 1096×522 with light sharpening; exact response and log text were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `Changes deployed`, `Response`, `PONG`, and event parameters remain readable; no face/camera/recording overlay remains; Markdown reference resolves.

## 02-aws-lambda-05-pants-response.jpg

- **Disposition:** `crop/replace` → `images/02-aws-lambda-05-pants-response-cropped.png`
- **Teaching point:** the deployed handler receives a URL and returns the prediction `{"prediction": "pants"}`.
- **Source inspection:** 592×360; deterministic crop `+0+75 548×261` removes the browser strip, webcam tile, recording banner edge, and black frame while retaining the response and logs.
- **Method:** deterministic Lanczos upscale to 1096×522 with light sharpening; exact JSON response and request URL text were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; response JSON, deployed status, and URL parameter remain readable; no face/camera/recording overlay remains; Markdown reference resolves.

## 02-aws-lambda-06-final-handler-code.jpg

- **Disposition:** `crop/replace` → `images/02-aws-lambda-06-final-handler-code-cropped.png`
- **Teaching point:** the final Lambda handler reads `event['url']`, calls `predict(url)`, and returns the result.
- **Source inspection:** 592×360; deterministic crop `+0+75 548×261` removes the browser strip, webcam tile, and black frame while retaining the exact code editor state.
- **Method:** deterministic Lanczos upscale to 1096×522 with light sharpening; exact handler code and `Changes not deployed` state were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `event['url']`, `predict(url)`, and `return results` remain readable; no face/camera/recording overlay remains; Markdown reference resolves.

## 02-aws-lambda-08-invite-link-function.jpg

- **Disposition:** `crop/replace` → `images/02-aws-lambda-08-invite-link-function-cropped.png`
- **Teaching point:** the `join-datatalks-club` Lambda function is connected to an API Gateway trigger.
- **Source inspection:** 592×360; deterministic crop `+0+20 500×316` removes the browser URL strip, webcam tile, and right-side black frame while retaining the function overview and trigger relationship.
- **Method:** deterministic Lanczos upscale to 1000×632 with light sharpening; exact AWS UI labels were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; function name, API Gateway trigger, and overview relationship remain readable; no face/camera/recording overlay remains. A small native pointer on the blank canvas remains; Markdown reference resolves.

## 01-intro-04-module-plan.jpg

- **Disposition:** `crop/replace` → `images/01-intro-04-module-plan-cropped.png`
- **Teaching point:** the module plan starts with deploying the previously trained clothes-classification model and introduces AWS Lambda and TensorFlow Lite.
- **Source inspection:** 592×360; deterministic crop `+0+0 500×336` removes the webcam tile, black frame, and bottom editor status bar while retaining the exact plan text.
- **Method:** deterministic Lanczos upscale to 1000×672 with light sharpening; exact headings and bullets were preserved.
- **Rubric:** instructional contribution 1, relevance 2, readability 2, complementarity 1, durability 2, caption/accessibility 2 — **10/12; keep**.
- **Validation:** output inspected; headings and bullets remain readable, no face/camera/recording overlay remains, and Markdown reference resolves.

## 01-intro-05-module-plan-lambda-gateway.jpg

- **Disposition:** `crop/replace` → `images/01-intro-05-module-plan-lambda-gateway-cropped.png`
- **Teaching point:** the later module steps package the model, create/configure Lambda, test it, and expose it through API Gateway.
- **Source inspection:** 592×360; deterministic crop `+0+0 500×336` removes the webcam tile, black frame, and bottom editor status bar while retaining the exact plan text.
- **Method:** deterministic Lanczos upscale to 1000×672 with light sharpening; exact headings and bullets were preserved.
- **Rubric:** instructional contribution 1, relevance 2, readability 2, complementarity 1, durability 2, caption/accessibility 2 — **10/12; keep**.
- **Validation:** output inspected; Lambda, Docker, and API Gateway plan items remain readable, no face/camera/recording overlay remains, and Markdown reference resolves.

## 03-tensorflow-lite-01-load-keras-model.jpg

- **Disposition:** `crop/replace` → `images/03-tensorflow-lite-01-load-keras-model-cropped.png`
- **Teaching point:** the notebook imports TensorFlow 2.7.0 and loads `clothing-model.h5` with Keras.
- **Source inspection:** 592×360; deterministic crop `+0+30 500×306` removes browser chrome, webcam tile, and right-side black frame while retaining the notebook warning/version and load cell.
- **Method:** deterministic Lanczos upscale to 1000×612 with light sharpening; exact code, version, and warning text were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `2.7.0`, `keras.models.load_model('clothing-model.h5')`, and notebook output remain readable; no face/camera/recording overlay remains; Markdown reference resolves.

## 03-tensorflow-lite-02-keras-predictions.jpg

- **Disposition:** `crop/replace` → `images/03-tensorflow-lite-02-keras-predictions-cropped.png`
- **Teaching point:** the notebook prepares `pants.jpg`, calls `model.predict(X)`, and shows the raw prediction vector.
- **Source inspection:** 592×360; deterministic crop `+0+30 500×306` removes browser chrome, webcam tile, and right-side black frame while retaining the exact cells and numeric output.
- **Method:** deterministic Lanczos upscale to 1000×612 with light sharpening; code and prediction values were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `load_img`, `preprocess_input`, `model.predict(X)`, and all displayed values remain readable; no face/camera/recording overlay remains; Markdown reference resolves.

## 03-tensorflow-lite-03-convert-to-tflite.jpg

- **Disposition:** `crop/replace` → `images/03-tensorflow-lite-03-convert-to-tflite-cropped.png`
- **Teaching point:** `TFLiteConverter` converts the Keras model and writes `clothing-model.tflite`.
- **Source inspection:** 592×360; deterministic crop `+0+30 500×215` removes browser chrome, webcam tile, and right-side black frame while retaining the heading and complete conversion cell.
- **Method:** deterministic Lanczos upscale to 1000×430 with light sharpening; exact code and source warning text were preserved. The lower log output was intentionally excluded because it is not needed for the caption.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `TFLiteConverter`, `converter.convert()`, and `clothing-model.tflite` remain readable; no face/camera/recording overlay remains; Markdown reference resolves.

## 03-tensorflow-lite-04-model-sizes.jpg

- **Disposition:** `crop/replace` → `images/03-tensorflow-lite-04-model-sizes-cropped.png`
- **Teaching point:** the converted TF-Lite model is present as `clothing-model.tflite` at 81M versus the original Keras model at 83M.
- **Source inspection:** 592×360; deterministic crop `+0+30 500×306` removes browser chrome, webcam tile, and right-side black frame while retaining the exact `ls -lh` output.
- **Method:** deterministic Lanczos upscale to 1000×612 with light sharpening; filenames and size values were preserved. The source's native text selection highlight remains because removing it safely would alter exact terminal/notebook pixels.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `83M`, `81M`, and both model filenames remain readable; no face/camera/recording overlay remains; Markdown reference resolves.

## 03-tensorflow-lite-05-interpreter-indexes.jpg

- **Disposition:** `crop/replace` → `images/03-tensorflow-lite-05-interpreter-indexes-cropped.png`
- **Teaching point:** TF-Lite creates an interpreter, allocates tensors, and obtains the input/output tensor indexes.
- **Source inspection:** 592×360; deterministic crop `+0+30 500×306` removes browser chrome, webcam tile, and right-side black frame while retaining all relevant notebook cells.
- **Method:** deterministic Lanczos upscale to 1000×612 with light sharpening; exact imports, model path, and index calls were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; interpreter construction, `allocate_tensors`, `input_index`, and `output_index` remain readable; no face/camera/recording overlay remains; Markdown reference resolves.

## 03-tensorflow-lite-06-keras-preprocess-source.jpg

- **Disposition:** `crop/replace` → `images/03-tensorflow-lite-06-keras-preprocess-source-cropped.png`
- **Teaching point:** Keras' `tf` preprocessing mode divides by 127.5, subtracts 1, and returns the normalized array.
- **Source inspection:** 592×360; focused deterministic crop `+0+185 500×120` removes browser chrome, webcam tile, empty page area, and unrelated source lines while retaining the exact `tf` branch.
- **Method:** deterministic Lanczos upscale to 1000×240 with light sharpening; exact source code and values were preserved. The native code-selection highlight remains because removing it safely would alter exact source pixels.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `if mode == "tf"`, `x /= 127.5`, `x -= 1.`, and `return x` remain readable; no face/camera/recording overlay remains; Markdown reference resolves.

## 03-tensorflow-lite-07-keras-image-helper.jpg

- **Disposition:** `crop/replace` → `images/03-tensorflow-lite-07-keras-image-helper-cropped.png`
- **Teaching point:** `keras-image-helper` is installed and used to create an Xception preprocessor with the expected target size and URL input.
- **Source inspection:** 592×360; deterministic crop `+0+30 500×306` removes browser chrome, webcam tile, and right-side black frame while retaining the install output and exact code cells.
- **Method:** deterministic Lanczos upscale to 1000×612 with light sharpening; exact package name, target size, and URL were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; install success, `create_preprocessor('xception', target_size=(299, 299))`, and `from_url` usage remain readable; no face/camera/recording overlay remains; Markdown reference resolves.

## 03-tensorflow-lite-08-tflite-runtime-install.jpg

- **Disposition:** `crop/replace` → `images/03-tensorflow-lite-08-tflite-runtime-install-cropped.png`
- **Teaching point:** the TensorFlow Lite guide shows installation of `tflite-runtime` and the separate runtime inference path.
- **Source inspection:** 592×360; deterministic crop `+0+30 500×306` removes browser chrome, webcam tile, and right-side black frame while retaining the guide heading, install command, and warning.
- **Method:** deterministic Lanczos upscale to 1000×612 with light sharpening; exact command and page text were preserved. The native command selection highlight remains because removing it safely would alter the exact website capture.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `Install TensorFlow Lite for Python`, the `tflite-runtime` pip command, and inference heading remain readable; no face/camera/recording overlay remains; Markdown reference resolves.

## 04-preparing-code-01-lesson-plan.jpg

- **Disposition:** `crop/replace` → `images/04-preparing-code-01-lesson-plan-cropped.png`
- **Teaching point:** the lesson moves inference code from a notebook into a script, tests it locally, and then prepares a Docker image.
- **Source inspection:** 592×360; deterministic crop `+0+0 500×336` removes the webcam tile, black frame, and bottom editor status bar while retaining the exact plan text.
- **Method:** deterministic Lanczos upscale to 1000×672 with light sharpening; exact headings and bullets were preserved.
- **Rubric:** instructional contribution 1, relevance 2, readability 2, complementarity 1, durability 2, caption/accessibility 2 — **10/12; keep**.
- **Validation:** output inspected; notebook-to-script, local testing, and Docker plan items remain readable; no face/camera/recording overlay remains; Markdown reference resolves.

## 04-preparing-code-02-nbconvert.jpg

- **Disposition:** `crop/replace` → `images/04-preparing-code-02-nbconvert-cropped.png`
- **Teaching point:** `jupyter nbconvert --to script tensorflow-model.ipynb` writes the generated `tensorflow-model.py` script.
- **Source inspection:** 592×360; deterministic crop `+0+0 500×336` removes the webcam tile, black frame, and bottom editor status bar while retaining the terminal command and output.
- **Method:** deterministic Lanczos upscale to 1000×672 with light sharpening; exact command, filenames, and byte counts were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; nbconvert command, conversion messages, and `tensorflow-model.py` output remain readable; no face/camera/recording overlay remains; Markdown reference resolves.

## 04-preparing-code-03-generated-script.jpg

- **Disposition:** `crop/replace` → `images/04-preparing-code-03-generated-script-cropped.png`
- **Teaching point:** the generated Python file contains leftover IPython cell magics such as `run_line_magic` and `system` calls.
- **Source inspection:** 592×360; deterministic crop `+0+0 500×336` removes the webcam tile, black frame, and bottom editor status bar while retaining the file header and magic calls.
- **Method:** deterministic Lanczos upscale to 1000×672 with light sharpening; exact visible code was preserved. The long source URL remains limited by the original editor viewport and is not used as a generated approximation.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `tensorflow-model.py`, `ipython().run_line_magic`, and `ipython().system` remain readable; no face/camera/recording overlay remains; Markdown reference resolves.

## 04-preparing-code-04-predict-function.jpg

- **Disposition:** `crop/replace` → `images/04-preparing-code-04-predict-function-cropped.png`
- **Teaching point:** the cleaned script's `predict(url)` function prepares the image, invokes TF-Lite, and returns a class-to-score dictionary.
- **Source inspection:** 592×360; focused deterministic crop `+0+55 552×220` removes the webcam tile, editor chrome, cursor/autocomplete overlay, and bottom status area while retaining the function body.
- **Method:** deterministic Lanczos upscale to 1104×440 with light sharpening; exact visible code was preserved. The long `output_index` line remains limited by the original viewport edge.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `predict(url)`, `from_url`, `set_tensor`, `invoke`, `get_tensor`, and the return dictionary remain readable; no face/camera/recording overlay or autocomplete popup remains; Markdown reference resolves.

## 04-preparing-code-05-test-in-ipython.jpg

- **Disposition:** `crop/replace` → `images/04-preparing-code-05-test-in-ipython-cropped.png`
- **Teaching point:** importing `lambda_function` and calling `predict` returns the expected dictionary of clothing scores, with `pants` highest.
- **Source inspection:** 592×360; deterministic crop `+0+0 500×336` removes the webcam tile, black frame, and bottom editor status bar while retaining the terminal output and values.
- **Method:** deterministic Lanczos upscale to 1000×672 with light sharpening; exact URL, class names, and scores were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; IPython command, all class scores, and highest `pants` value remain readable; no face/camera/recording overlay remains. A small native pointer over the URL remains; Markdown reference resolves.
