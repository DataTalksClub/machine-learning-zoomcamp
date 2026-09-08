# Serverless screenshot rollout: lessons 05–09

Capability check: this worker has the `imagegen` skill. These 28 assets are
exact technical screenshots: code, commands, URLs, AWS/GitHub/PyPI UI,
plots, and numeric output. Per the rollout rubric, deterministic crops and
Lanczos upscaling are used for every asset; imagegen is not used because it
could alter exact technical content. Original source assets remain in place.

Each accepted screenshot is committed separately. Temporary crops and contact
sheets stay under `.tmp/` and are not committed.

## 05-docker-image-01-ecr-public-gallery.jpg

- **Disposition:** `crop/replace` → `images/05-docker-image-01-ecr-public-gallery-cropped.png`
- **Teaching point:** the ECR Public Gallery contains the AWS Lambda Python base image used for the container.
- **Source inspection:** 592×360; crop `+0+52 550×250` removes the browser strip, webcam tile, cookie banner, and black frame while retaining the Python image cards.
- **Method:** deterministic Lanczos upscale to 1100×500 with light sharpening; exact gallery labels and image-card content were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; AWS Lambda Python card and surrounding base-image cards remain visible, no face/camera/recording overlay remains, and the Markdown reference resolves.

## 05-docker-image-02-dockerfile.jpg

- **Disposition:** `crop/replace` → `images/05-docker-image-02-dockerfile-cropped.png`
- **Teaching point:** the Dockerfile installs the dependencies, copies the model and handler, and points `CMD` to `lambda_function.lambda_handler`.
- **Source inspection:** 592×360; crop `+0+0 500×315` removes the webcam tile, right-side black frame, and bottom status strip while retaining the complete visible Dockerfile.
- **Method:** deterministic Lanczos upscale to 1000×630 with light sharpening; exact code and dependency URL were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `FROM`, both `RUN` lines, `COPY` lines, and the Lambda handler command remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves.

## 05-docker-image-03-test-script.jpg

- **Disposition:** `crop/replace` → `images/05-docker-image-03-test-script-cropped.png`
- **Teaching point:** `test.py` imports `requests` and targets the local Lambda invocation endpoint.
- **Source inspection:** 592×360; crop `+0+0 500×315` removes the webcam tile, right-side black frame, and bottom status strip while retaining the visible test script.
- **Method:** deterministic Lanczos upscale to 1000×630 with light sharpening; exact code and local endpoint text were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `import requests` and the local `2015-03-31/Function` URL remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves.

## 05-docker-image-04-glibc-error.jpg

- **Disposition:** `crop/replace` → `images/05-docker-image-04-glibc-error-cropped.png`
- **Teaching point:** the local container invocation fails because the installed TF-Lite runtime requires an unavailable GLIBC version.
- **Source inspection:** 592×360; crop `+0+52 550×263` removes the webcam tile, editor tabs, and right-side black frame while retaining the Dockerfile context and terminal error.
- **Method:** deterministic Lanczos upscale to 1100×526 with light sharpening; exact error text and visible Dockerfile lines were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; the `GLIBC_2.27` failure and `python test.py` invocation remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves. The top Dockerfile line is partially clipped by the focused crop.

## 05-docker-image-05-tflite-wheels.jpg

- **Disposition:** `crop/replace` → `images/05-docker-image-05-tflite-wheels-cropped.png`
- **Teaching point:** the repository provides precompiled TF-Lite runtime wheels, including the Python 3.8 / TF-Lite 2.7.0 wheel needed by the image.
- **Source inspection:** 592×360; crop `+0+52 550×265` removes browser chrome, webcam tile, footer, and black frame while retaining the wheel list and highlighted `cp38` file.
- **Method:** deterministic Lanczos upscale to 1100×530 with light sharpening; exact filenames and version labels were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; the highlighted `tflite_runtime-2.7.0-cp38-cp38-linux_x86_64.whl` row remains readable, no face/camera/recording overlay remains, and the Markdown reference resolves. The first visible row is partially clipped by the focused crop.

## 05-docker-image-06-rebuild.jpg

- **Disposition:** `crop/replace` → `images/05-docker-image-06-rebuild-cropped.png`
- **Teaching point:** rebuilding the image installs `tflite-runtime-2.7.0` and completes all Dockerfile steps successfully.
- **Source inspection:** 592×360; crop `+55+20 447×293` isolates the terminal window and removes the editor, webcam tile, and surrounding black frame.
- **Method:** deterministic Lanczos upscale to 894×586 with light sharpening; exact installation warnings, Docker steps, and success output were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `Successfully installed ... tflite-runtime-2.7.0`, Docker steps 4–6, and `Successfully built/tagged` remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves.

## 05-docker-image-07-float32-error.jpg

- **Disposition:** `crop/replace` → `images/05-docker-image-07-float32-error-cropped.png`
- **Teaching point:** after switching to the compatible wheel, inference reaches a JSON serialization error because the prediction contains `float32` values.
- **Source inspection:** 592×360; crop `+0+52 550×308` removes the webcam tile, editor tabs, and right-side black frame while retaining the Dockerfile context and both terminal errors.
- **Method:** deterministic Lanczos upscale to 1100×616 with light sharpening; exact wheel URL fragment, GLIBC failure, and `float32 not JSON serializable` output were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; the float32 serialization error is visible and readable, no face/camera/recording overlay remains, and the Markdown reference resolves. The long wheel URL remains bounded by the original viewport.

## 05-docker-image-08-tolist-fix.jpg

- **Disposition:** `crop/replace` → `images/05-docker-image-08-tolist-fix-cropped.png`
- **Teaching point:** converting the prediction array with `.tolist()` makes the class-score dictionary JSON serializable and the local test succeeds.
- **Source inspection:** 592×360; crop `+0+52 550×308` removes the webcam tile, editor tabs, and right-side black frame while retaining the fix and terminal response.
- **Method:** deterministic Lanczos upscale to 1100×616 with light sharpening; exact code, class names, and prediction values were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `float_predictions = preds[0].tolist()` and the successful `python test.py` output remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves. The long JSON line remains bounded by the original viewport.

## 06-creating-lambda-01-ecr-create-repository.jpg

- **Disposition:** `crop/replace` → `images/06-creating-lambda-01-ecr-create-repository-cropped.png`
- **Teaching point:** the terminal first shows the missing AWS CLI command and then the `pip install awscli` fallback.
- **Source inspection:** 592×360; crop `+55+20 447×293` isolates the terminal window and removes the AWS page, webcam tile, and surrounding frame.
- **Method:** deterministic Lanczos upscale to 894×586 with light sharpening; exact command, package suggestions, and version text were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; the `aws ecr create-repository` failure and `pip install awscli` command remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves.

## 06-creating-lambda-02-docker-push.jpg

- **Disposition:** `crop/replace` → `images/06-creating-lambda-02-docker-push-cropped.png`
- **Teaching point:** Docker tags the image with the remote ECR URI and uploads its layers with `docker push`.
- **Source inspection:** 592×360; crop `+55+20 447×293` isolates the terminal and removes editor chrome, webcam tile, and surrounding frame.
- **Method:** deterministic Lanczos upscale to 894×586 with light sharpening; exact ECR repository URI, layer states, and transfer sizes were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `docker tag`, `docker push`, repository path, and layer upload states remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves.

## 06-creating-lambda-03-create-function.jpg

- **Disposition:** `crop/replace` → `images/06-creating-lambda-03-create-function-cropped.png`
- **Teaching point:** the Lambda function is created from the ECR container image with `x86_64` selected and the default logging role.
- **Source inspection:** 592×360; crop `+0+50 550×268` removes the browser bar and webcam tile while retaining the image field, architecture choice, permissions, and create button.
- **Method:** deterministic Lanczos upscale to 1100×536 with light sharpening; exact console labels and selected architecture were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `x86_64`, permissions text, and `Create function` remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves. The image URI field is partially visible because the crop focuses on the configuration controls.

## 06-creating-lambda-04-timeout-error.jpg

- **Disposition:** `crop/replace` → `images/06-creating-lambda-04-timeout-error-cropped.png`
- **Teaching point:** the first Lambda invocation fails because the function times out after the default three seconds.
- **Source inspection:** 592×360; crop `+0+50 550×268` removes the browser bar, webcam tile, and side frame while retaining the failed execution result and timeout message.
- **Method:** deterministic Lanczos upscale to 1100×536 with light sharpening; exact error JSON and summary identifiers were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `Execution result: failed` and `timed out after 3.00 seconds` remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves. Lower summary rows are intentionally excluded because they are not needed for the caption.

## 06-creating-lambda-05-configure-timeout-memory.jpg

- **Disposition:** `crop/replace` → `images/06-creating-lambda-05-configure-timeout-memory-cropped.png`
- **Teaching point:** the Lambda configuration is changed to 1024 MB of memory and a 30-second timeout.
- **Source inspection:** 592×360; crop `+0+50 550×268` removes the browser bar, webcam tile, and side frame while retaining memory, timeout, role, and save controls.
- **Method:** deterministic Lanczos upscale to 1100×536 with light sharpening; exact values and role text were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `1024 MB`, `30 sec`, role selection, and `Save` remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves.

## 06-creating-lambda-06-test-success.jpg

- **Disposition:** `crop/replace` → `images/06-creating-lambda-06-test-success-cropped.png`
- **Teaching point:** the warm Lambda invocation completes in about 2226 ms with 1024 MB configured and 270 MB used.
- **Source inspection:** the original filename is swapped with the following pricing asset; the success capture is `06-creating-lambda-07-lambda-pricing.jpg` (592×360). Crop `+0+50 550×268` removes the browser bar, webcam tile, and side frame while retaining the successful invocation summary.
- **Method:** deterministic Lanczos upscale to 1100×536 from the success source; exact duration, billed duration, memory, and max-memory values were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**. The ref/source mismatch was corrected so the lesson now shows the content described by its caption.
- **Validation:** output inspected; `Duration 2226.24 ms`, `1024 MB`, and `270 MB` remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves.

## 06-creating-lambda-07-lambda-pricing.jpg

- **Disposition:** `crop/replace` → `images/06-creating-lambda-07-lambda-pricing-cropped.png`
- **Teaching point:** the AWS Lambda Europe (Ireland) pricing table shows the price per millisecond for each memory setting.
- **Source inspection:** the original filename is swapped with the preceding success asset; the pricing capture is `06-creating-lambda-06-test-success.jpg` (592×360). Crop `+0+50 550×268` removes the browser bar, webcam tile, and side frame while retaining the region, memory, and price table.
- **Method:** deterministic Lanczos upscale to 1100×536 from the pricing source; exact table values and highlighted 1024 MB row were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**. The ref/source mismatch was corrected so the lesson now shows the content described by its caption.
- **Validation:** output inspected; `Europe (Ireland)`, `Memory (MB)`, `Price per 1ms`, and the highlighted `1024` row remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves.

## 06-creating-lambda-08-price-calculation.jpg

- **Disposition:** `crop/replace` → `images/06-creating-lambda-08-price-calculation-cropped.png`
- **Teaching point:** the IPython calculation multiplies the per-millisecond Lambda price by 2000 ms for one image, 10,000 images, and one million images, including an ARM comparison.
- **Source inspection:** 592×360; crop `+0+0 500×340` removes the webcam tile, right-side black frame, and bottom status strip while retaining the code and four numeric results.
- **Method:** deterministic Lanczos upscale to 1000×680 with light sharpening; exact expressions and values were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; the per-image, 10,000-image, one-million-image, and ARM calculations remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves.

## 07-api-gateway-01-create-rest-api.jpg

- **Disposition:** `crop/replace` → `images/07-api-gateway-01-create-rest-api-cropped.png`
- **Teaching point:** API Gateway starts a new regional REST API and asks for its friendly name and description.
- **Source inspection:** 592×360; crop `+0+50 550×268` removes browser chrome, webcam tile, and surrounding frame while retaining the REST API choices and settings form.
- **Method:** deterministic Lanczos upscale to 1100×536 with light sharpening; exact API Gateway labels and selected `New API` / `Regional` options were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `New API`, `Settings`, `API name`, and `Regional` remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves. The long explanatory line remains bounded by the source viewport.

## 07-api-gateway-02-create-resource.jpg

- **Disposition:** `crop/replace` → `images/07-api-gateway-02-create-resource-cropped.png`
- **Teaching point:** API Gateway creates a child resource named `predict` with resource path `/predict`.
- **Source inspection:** 592×360; crop `+0+50 550×268` removes browser chrome, webcam tile, and surrounding frame while retaining the resource form and path explanation.
- **Method:** deterministic Lanczos upscale to 1100×536 with light sharpening; exact resource name, path, proxy-resource option, and CORS control were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `New Child Resource`, `predict`, `/ predict`, and `Enable API Gateway CORS` remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves.

## 07-api-gateway-03-lambda-permission.jpg

- **Disposition:** `crop/replace` → `images/07-api-gateway-03-lambda-permission-cropped.png` (**source/caption mismatch recorded for parent review**).
- **Teaching point stated by the lesson:** the AWS “Add Permission to Lambda Function” dialog confirms API Gateway may invoke Lambda.
- **Source inspection:** the 592×360 source is actually a local `test.py` editor frame, not that AWS dialog. Crop `+0+0 500×315` removes the webcam tile, right-side black frame, and bottom status strip while preserving the exact source rather than inventing UI.
- **Method:** deterministic Lanczos upscale to 1000×630 with light sharpening; no text or controls were regenerated.
- **Rubric:** instructional contribution 0, relevance 0, readability 2, complementarity 0, durability 1, caption/accessibility 0 — **3/12; parent review required**. The asset should be removed or replaced if a matching permission-dialog source is found.
- **Validation:** output inspected; the actual test script remains readable and no face/camera/recording overlay remains. The screenshot does not substantiate the surrounding permission-dialog paragraph; the Markdown reference resolves.

## 07-api-gateway-04-method-test.jpg

- **Disposition:** `crop/replace` → `images/07-api-gateway-04-method-test-cropped.png`
- **Teaching point:** the API Gateway method-test page is ready for a `POST /predict` request.
- **Source inspection:** the original filename is swapped with the following response asset; the method-test capture is `07-api-gateway-05-test-response.jpg` (592×360). Crop `+0+50 550×268` removes browser chrome, webcam tile, and surrounding frame while retaining the method tree and test form.
- **Method:** deterministic Lanczos upscale to 1100×536 from the method-test source; exact `POST`, `/predict`, path, query-string, and header controls were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**. The ref/source mismatch was corrected so the lesson now shows the content described by its caption.
- **Validation:** output inspected; `/predict - POST - Method Test` and the test form remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves.

## 07-api-gateway-05-test-response.jpg

- **Disposition:** `crop/replace` → `images/07-api-gateway-05-test-response-cropped.png`
- **Teaching point:** the API Gateway test returns the class-score JSON and records the request in execution logs.
- **Source inspection:** the original filename is swapped with the preceding method-test asset; the response/log capture is `07-api-gateway-04-method-test.jpg` (592×360). Crop `+0+52 550×255` removes browser chrome, webcam tile, cookie/footer banner, and side frame while retaining response headers and logs.
- **Method:** deterministic Lanczos upscale to 1100×510 from the response source; exact score fragments, response headers, and `POST /predict` logs were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**. The ref/source mismatch was corrected so the lesson now shows the content described by its caption.
- **Validation:** output inspected; response-score text, `Response Headers`, and execution logs remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves. The uppermost score rows are outside the source viewport crop.

## 07-api-gateway-06-deploy-stage.jpg

- **Disposition:** `crop/replace` → `images/07-api-gateway-06-deploy-stage-cropped.png`
- **Teaching point:** API Gateway deploys the API to a new stage named `test`.
- **Source inspection:** 592×360; focused crop `+80+30 380×245` isolates the deployment dialog and removes browser chrome, webcam tile, page clutter, and black frame.
- **Method:** deterministic Lanczos upscale to 760×490 with light sharpening; exact stage fields and `Deploy` control were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; `Deploy API`, `[New Stage]`, stage name `test`, and `Deploy` remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves.

## 07-api-gateway-07-test-py-gateway-url.jpg

- **Disposition:** `crop/replace` → `images/07-api-gateway-07-test-py-gateway-url-cropped.png`
- **Teaching point:** `test.py` replaces the local invocation URL with the deployed API Gateway URL and keeps the `/predict` request payload.
- **Source inspection:** 592×360; crop `+0+52 552×308` removes the webcam tile, editor tabs, and right-side black frame while retaining the URL line, terminal calculation, and file listing.
- **Method:** deterministic Lanczos upscale to 1104×616 with light sharpening; exact URL prefix, payload, and terminal values were preserved.
- **Rubric:** instructional contribution 2, relevance 2, readability 2, complementarity 2, durability 1, caption/accessibility 2 — **11/12; keep**.
- **Validation:** output inspected; the API Gateway URL, commented local URL, and `/predict` context remain readable, no face/camera/recording overlay remains, and the Markdown reference resolves. The final URL characters are clipped by the original editor viewport.
