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
