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
