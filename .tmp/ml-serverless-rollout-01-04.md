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
