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
