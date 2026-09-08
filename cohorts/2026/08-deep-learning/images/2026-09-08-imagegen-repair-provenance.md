# Deep-learning illustration repair provenance — 2026-09-08

This ledger covers only `cohorts/2026/08-deep-learning`. Earlier claims that
the module's screenshot-derived assets were already crisp are withdrawn.

## Accepted repair

### `04-conv-neural-nets-06-logistic-regression-crisp.png`

- **Status:** accepted after native and simulated 608px inspection.
- **Source JPG:** `04-conv-neural-nets-06-logistic-regression.jpg`
  - SHA-256: `c9f2eba9ba6a6d34fe9727d049ab1e37fa6467ed363d40f67114d302e835b5c9`
- **Bounded crop:** `04-conv-neural-nets-06-logistic-regression-cropped.png`
  - SHA-256: `9892e4430f3b45385eee914a53b19d26e6c5821c6ff5411b634edc350b2339b5`
- **Generated output:** `04-conv-neural-nets-06-logistic-regression-crisp.png`
  - SHA-256: `cfb07af4e6a461121a43a86367bd72d61621c5eb0d4f6f7235910f9c478a6416`
  - Dimensions: `1774x887`
- **Method:** built-in imagegen edit/redraw using the original JPG and bounded
  crop as references. The result is a clean typeset redraw, not a resize or
  sharpened copy.
- **Semantic checks:** input vector `x₁, x₂, x₃, ⋮, xₙ`; weighted inputs;
  `Σ xᵢwᵢ`; sigmoid; and `prob t-shirt` are present, with arrows in the
  lesson's input → sum → sigmoid → probability order. Camera footage,
  handwriting, browser/player chrome, and overlays are absent.
- **Metadata:** generated PNG contains C2PA metadata identifying the OpenAI
  image-generation service.

## Pending targets

The remaining nine targets from the strict 68-reference audit are not claimed
as repaired here. They require the same original-JPG-plus-bounded-crop
workflow and independent visual/semantic review:

- `06-learning-rate-04-train-accuracy-crisp.png`
- `06-learning-rate-05-val-accuracy-crisp.png`
- `06-learning-rate-06-two-lr-validation-crisp.png`
- `06-learning-rate-07-select-001-crisp.png`
- `09-dropout-07-dropout-02-vs-train-imagegen.png`
- `09-dropout-08-no-regularization-overfit-imagegen.png`
- `08-more-layers-02-activation-functions-crisp.png`
- `05-transfer-learning-05-pooling-vectors-crisp.png`
- `05-transfer-learning-08-history-plot-crisp.png`

