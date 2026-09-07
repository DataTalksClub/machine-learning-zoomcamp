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
