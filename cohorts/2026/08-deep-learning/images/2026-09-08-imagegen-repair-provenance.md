# Deep-learning illustration repair provenance — 2026-09-08

This ledger covers only `cohorts/2026/08-deep-learning`. Earlier claims that
the module's screenshot-derived assets were already crisp are withdrawn.

## Accepted repair

### `05-transfer-learning-05-pooling-vectors-crisp.png`

- **Status:** accepted after native and simulated 608px inspection.
- **Source JPG:** `05-transfer-learning-05-pooling-vectors.jpg`
  - SHA-256: `8a68f52b57ce87e5302ad73e159da793411f18c6a3f497b55a7d08ed6af05de3`
- **Bounded crop:** `05-transfer-learning-05-pooling-vectors-cropped.png`
  - SHA-256: `45beb4289cc7e7940b81a0fff9ffe659bfbc09f37b81832ec08162ab2044b44a`
- **Generated output:** `05-transfer-learning-05-pooling-vectors-crisp.png`
  - SHA-256: `975adb5a347bd205be20f32ca66c4495714b4740f0d9721187bd31c10ee6d692`
  - Dimensions: `1942x809`
- **Method:** built-in imagegen redraw using the original JPG and bounded crop as
  references. The result is a clean typeset diagram, not a resize or sharpened
  copy.
- **Semantic checks:** exact batch shapes `32 × 150 × 150 × 3` and
  `32 × 2048`; exact single-image feature-map shape `5 × 5 × 2048`; and the
  lower inset's `5 × 5` spatial slices averaged into `2048` vector values,
  labeled `3D` to `1D`. The base-model → global-average-pooling → vectors
  direction is complete and readable at 608px.
- **Metadata:** generated PNG contains C2PA metadata identifying the OpenAI
  image-generation service.

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

The remaining eight targets from the strict 68-reference audit are not claimed
as repaired here. They require the same original-JPG-plus-bounded-crop
workflow and independent visual/semantic review:

- `06-learning-rate-04-train-accuracy-crisp.png`
- `06-learning-rate-05-val-accuracy-crisp.png`
- `06-learning-rate-06-two-lr-validation-crisp.png`
- `06-learning-rate-07-select-001-crisp.png`
- `09-dropout-07-dropout-02-vs-train-imagegen.png`
- `09-dropout-08-no-regularization-overfit-imagegen.png`
- `08-more-layers-02-activation-functions-crisp.png`
- `05-transfer-learning-08-history-plot-crisp.png`
