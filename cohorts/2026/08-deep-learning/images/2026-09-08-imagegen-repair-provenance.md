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

## Deterministic chart repair batch

The original non-crisp JPG and bounded crop for each target were inspected
before rendering. These seven assets are exact lesson plots, so they were
rendered natively from the values preserved in `notebook.ipynb`, rather than
sent to imagegen or enlarged/sharpened. The reproducible renderer is
`2026-09-08-deep-learning-chart-repair.py`.

The source values are taken from notebook cell 32 (learning-rate runs), cell
28 (the first transfer-learning history), and cell 46 (dropout runs). Each
output was inspected at its native `2000x1200` resolution and as a simulated
608px-wide render. The old screenshots, JPGs, and crops remain in the repo as
source evidence.

| Output | Source JPG SHA-256 | Crop SHA-256 | Output SHA-256 |
|---|---|---|---|
| `06-learning-rate-04-train-accuracy-crisp.png` | `ad05e4fe586b7dc6bfb90ca23673a3d90c7bbb3d894cd87dc8d2d0ba52982662` | `da6d1a41e52fe9a9b9a93870de7ac889b7479fb03f767ade992a039cc75f6027` | `4b8426594724ff9f08aaec6a395633f78fe0958b72a6d4b47fc31e0ea4f8bd63` |
| `06-learning-rate-05-val-accuracy-crisp.png` | `b46c71ab64e87793bfa627ed65e5eaa9c507ec218428eb7dbea01880550cb144` | `238e4fa02ffb8d36b1fd9674b7b321e80f1e5805364b544e2fca7aee6199c8ce` | `a08f39399b0896a5daff98ad8ddb8f4b6c6a9475372c489a39a56c7df2a70e6b` |
| `06-learning-rate-06-two-lr-validation-crisp.png` | `cde56116a2ff21508387f0db27439ef156286b030a9eb149d595cf9dfcbecf2d` | `7d48f9ba976d2d72e9c8c5146d0b5f6b53cdf58340aea370231bd69e150ab14f` | `ef71c0cd534d0f936d5de73f7aa86e8e16f627af353421230e9562d51582cabf` |
| `06-learning-rate-07-select-001-crisp.png` | `ce983a098a250f451c74411b51cd8947c6bbe5247f0ff5f2204de93bd8d7a1ef` | `c0a36cb916834c8cb0fbf5bc7c2e8c856c658b38309d49451fc0b328f964e396` | `6fd5ea19711d31dbcaa0882c461d41743e01e9c06360341cbb0b033125ec70b4` |
| `05-transfer-learning-08-history-plot-crisp.png` | `c5f34a79b0c4f36598013c86c2b36cfc7cf37c436325a1d210b774768253460f` | `65d99a3751fd8e50b9bfe3b49f602c3125f9123ad487dd611ee52e5fdd14d3ab` | `ac6c207500f575e03b61f6cc697c875272c6089863f0e11468a64eb5ef0fb5d1` |
| `09-dropout-07-dropout-02-vs-train-imagegen.png` | `5ace28408560bfb243f78fa493cb1904583e65bd2408ac218871adfbfa2a893e` | `b77b5cba81dbb14f4218aebb4b28af25df60a9ea49777a88fde63a950c2814b6` | `5e3e768cbcbe33318bd992ffa4d58047ebf10a4eb6683b3e2882c7e5b577c9d0` |
| `09-dropout-08-no-regularization-overfit-imagegen.png` | `e5516a038aad0d2d2bdd3d2ba5ab4262c4a426fca35d407803784316d24965e1` | `aed04390b7252349dcc91bd10a071a7baf7e91685f5bb110d5455f38790c2f16` | `cc8c1ca563945ab3e44c804297199df39dc2e0faf4d2b2677fdfc54c9c960b69` |

The dropout filenames retain their existing `imagegen` suffix for stable
lesson links, but the replacement pixels are deterministic native renders;
they are not imagegen output.

## Remaining target in this batch

The ReLU page screenshot still requires the original-JPG-plus-bounded-crop
imagegen redraw. It is intentionally kept separate from the deterministic
chart commit:

- `08-more-layers-02-activation-functions-crisp.png`
