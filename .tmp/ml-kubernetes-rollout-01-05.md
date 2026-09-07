# Kubernetes lessons 01–05 screenshot rollout

Scope: every Markdown image reference in `01-overview.md` through
`05-kubernetes-intro.md`. Originals remain in place; accepted replacements
are sibling assets. Imagegen is used only for bounded explanatory diagrams;
exact code, commands, URLs, plots, numeric output, and UI use deterministic
crops and upscaling.

## Acceptance records

### `01-overview-01-tf-serving-inference.jpg`

- Lesson: `01-overview.md`; caption: TensorFlow Serving: C++ inference with the clothes model.
- Disposition: imagegen replacement; the source is a bounded inference diagram.
- Source inspection: `594x360`; camera tile and black side bars present.
- Preparation crop: `.tmp/ml-kubernetes-rollout-01-05-crops/01-overview-01-tf-serving-inference-source.png`, coordinates `475x360+23+0`.
- Invariants checked: left-to-right image input, arrow label `X`, `INFERENCE`, `TF-SERVING`, `C++`, and `CLOTHING MODEL`.
- Prompt iteration: first generation accepted after visual inspection; no face, camera tile, chrome, cursor, watermark, or extra component remains.
- Output: `images/01-overview-01-tf-serving-inference-imagegen.png`.
