# Classification illustration provenance repair: 2026-09-08

This ledger records the focused repair of the 11 unresolved active image
references identified in Pascal's classification audit. The original
non-crisp JPGs are retained unchanged. Every row also retains a bounded
reference crop cut directly from that JPG; the crop geometry and SHA-256 are
recorded below.

Six screenshot-derived assets were redrawn with the built-in imagegen tool
using both the original JPG and its bounded crop. They were not produced by
resizing, sharpening, or feeding the previous target to imagegen. The final
PNG was copied byte-for-byte from the generated output. Each generated asset
was checked at native resolution and at a simulated 608px lesson display.

Five assets are exact-text mathematical diagrams or data charts. For those,
the durable choice is a deterministic native render from the lesson values,
not generated text. Their imagegen output is therefore `N/A`; the ledger
records the historical native-render commit used to restore the crisp output.
Their retained crop is an audit reference, not a generation input.

## Source, crop, and output ledger

| Published target | Original source | Crop geometry `(x, y, width, height)` | Retained crop/reference | Imagegen output ID or native source | Source SHA-256 | Crop SHA-256 | Final SHA-256 |
|---|---|---:|---|---|---|---|---|
| `01-churn-project-01-churn-problem-crisp.png` | `01-churn-project-01-churn-problem.jpg` | `(0, 0, 500, 350)` | `01-churn-project-01-churn-problem-imagegen-crop.jpg` | `exec-95ea9106-7424-4eb3-bb68-bdc98b313b14` | `06edf274cccda92cf134d62ffc5553acff2b04d2c12b8a1607774c7c18453480` | `d7b099cf25b8680792ab1e72218ce50c0a22bb9564c1ed437c0f38ffd49de274` | `5ca9173550e38c556628e4177781d3b1851d68f9d59b7faeb987dffb282714fe` |
| `01-churn-project-02-binary-classification-crisp.png` | `01-churn-project-02-binary-classification.jpg` | `(70, 0, 430, 340)` | `01-churn-project-02-binary-classification-imagegen-crop.jpg` | `exec-5fd7e014-091f-4649-874e-965a4356f01e` | `82b9623682e26076a716e0ccfcce58dd6deb8daa28c38823a0c65ce4442bf2d7` | `7ab5fe4b8d56063626988137c244fd497132d68ab5d2e74a6a602b33a0b8037a` | `12dd44b05eb0644ff164b7367e0944db4fd776ca038700ca55fa739cd8eee895` |
| `03-validation-01-train-val-test-split-crisp.png` | `03-validation-01-train-val-test-split.jpg` | `(60, 0, 445, 350)` | `03-validation-01-train-val-test-split-imagegen-crop.jpg` | `exec-049f3625-1235-4d8d-8a2e-e4619d8c6b27` | `ceba738175622476ab0ea05dc3fba66e758c52ad9d52fe992b2d55428b7ffac5` | `07bc73282422512bf3a4cdb3c51269296922af1554d3e272584765d366e43d3c` | `ba84b56bd138bfff14d2ec9080bf2ed2eaf67744b299a6713b2e7e21d4f966cf` |
| `07-correlation-01-correlation-coefficient-imagegen-pilot.png` | `07-correlation-01-correlation-coefficient.jpg` | `(10, 0, 480, 350)` | `07-correlation-01-correlation-coefficient-imagegen-crop.jpg` | `exec-97148a95-9cf8-42f4-8be7-d169e31f1c23` | `a88754f900a64e14d96f74ecc36a26f6e2322310ab9769ba83cdf7fb87f96316` | `dff673f926140e05f95bfa3c3b805dedd27a4398009a5b2915de8da0d00d1581` | `f6cbcf961aab153b1463e2a3c951655a3bc3f160f8ce280c8f98cafe80a01380` |
| `07-correlation-02-binary-target-imagegen-pilot.png` | `07-correlation-02-binary-target.jpg` | `(45, 0, 450, 350)` | `07-correlation-02-binary-target-imagegen-crop.jpg` | `exec-5f193c35-4edd-440e-9576-56e27118fd67` | `74867c70734f8e679b4f02f58bfa1f2aa30a33f5b7c934a0894f773f9f7f8848` | `b9d95a058f5a4b3d39fc452251fe57bce976e9da789f3130c0e42cd6fced87e8` | `c50ad5128ea626cb0fe864ee7388b89736280dba132a85c459c72e9f10611e4c` |
| `07-correlation-04-churn-rate-tenure-clean.png` | `07-correlation-04-churn-rate-tenure.jpg` | `(0, 0, 500, 350)` | `07-correlation-04-churn-rate-tenure-native-reference-crop.jpg` | `N/A — deterministic native render restored from `384db52` | `d15e6457d7138b621cadd11ddb56e384f569b9d9fb2979770a30a7428d491774` | `7e6c469ff474274a0eb7bb1405cbf8a8df0a26ac4efffde9f5a13cfc3714203e` | `4b5a73e8befb0b0e4ccd41390e52b1e3c09cd955fd98e7de89bb6f439dbed964` |
| `07-correlation-05-churn-rate-monthly-charges-clean.png` | `07-correlation-05-churn-rate-monthly-charges.jpg` | `(0, 0, 500, 350)` | `07-correlation-05-churn-rate-monthly-charges-native-reference-crop.jpg` | `N/A — deterministic native SVG render from lesson values (this repair)` | `6cb0f6789a2dff0e7523af77235744491833dbe17291a5c8355846019740326c` | `0dacb770367cbeabd49ab24004149a97bec3d08aac6b7f2217f5f23d3dd30cc8` | `bfab1c6eaf7668ef95eb51bad325d5dd0677f82d7f8bf64a243230c52636a82e` |
| `08-ohe-01-one-hot-table-crisp.png` | `08-ohe-01-one-hot-table.jpg` | `(25, 0, 455, 350)` | `08-ohe-01-one-hot-table-imagegen-crop.jpg` | `exec-db996eda-f5c9-4483-8b84-26ac453289a8` | `2e76c41b448060ac899a4a516cb39339f28fb7af052e8d907f91878220ad7310` | `ae25fce42c01e7d1ab93844e1cec76941a4884fb419bf0e497d4463ff32fa2e4` | `d2841b9278b0ea4f0cc53907ebae06d5673dc61c8dd1c8a7a89f0fcab53f2e45` |
| `09-logistic-regression-01-binary-classification-clean.png` | `09-logistic-regression-01-binary-classification.jpg` | `(70, 0, 430, 350)` | `09-logistic-regression-01-binary-classification-native-reference-crop.jpg` | `N/A — deterministic native render restored from `f5a1299` | `a275e0adda3c1d3f26b495bb2d3663388a9a5370389032a8f0cb0cb3bb346c90` | `bfed30e882799b082bfcebb0300fdba9e6aea2dd25811a4518086cf53ddcbfd8` | `614026e0a405049c7f372da53dc3bf7eca6b81d397c892e9e191bca5c0eafee6` |
| `09-logistic-regression-02-from-linear-to-logistic-clean.png` | `09-logistic-regression-02-from-linear-to-logistic.jpg` | `(60, 0, 440, 350)` | `09-logistic-regression-02-from-linear-to-logistic-native-reference-crop.jpg` | `N/A — deterministic native render restored from `d6ba065` | `c886cce85a2d37e12a299d4be0549bce31f43f323d5821d7850a6ecad488479a` | `20340dbd8aeaf7330b2bdfad820123426a7e83d5f3c18196ccb29f79d8ae97f7` | `8df82ef42af1ca031fc5fdf952e42ea07d1731d5e7817238f220f8a57be42338` |
| `09-logistic-regression-03-sigmoid-formula-clean.png` | `09-logistic-regression-03-sigmoid-formula.jpg` | `(60, 0, 440, 350)` | `09-logistic-regression-03-sigmoid-formula-native-reference-crop.jpg` | `N/A — deterministic native render restored from `0f9e745` | `fdad3243aca9682c8a755676d1891fc2a5d7831b05a6352dc0a027b403ffa992` | `2502cc75d21ad45ad60e7953b481583f3a0c516b27e071c03c090ee21431dea3` | `bb24b9a7bc111633014d30b396ed763052cae6b9dae94f9cccdc9c1397204c0f` |

## Validation and invariants

- Original JPG sources were not modified.
- The six generated redraws remove webcam faces, browser/capture chrome,
  control wheels, cursors, and source selection artifacts.
- The generated redraws preserve the lesson's exact formulas, percentages,
  labels, row order, binary values, and relationship directions.
- The churn-rate charts preserve `60%`, `40%`, `17%`, `8%`, `18%`, and `32%`
  with the correct tenure and monthly-charge groupings.
- The logistic-regression native renders preserve the exact binary-class
  mapping, weighted-sum-to-sigmoid relationship, and sigmoid formula/curve.
- Every published target was inspected at native resolution and after a
  608px-wide resize. No target is an enlargement or sharpening derivative of
  the previous published PNG.

## Focused correction: 2026-09-08

Two assets were repaired after an independent audit found a terminology error
and an incorrect chart scale.

### `07-correlation-01-correlation-coefficient-imagegen-pilot.png`

- The original JPG and retained crop above were the only imagegen inputs; the
  previous published PNG was not supplied as an input.
- Imagegen output: `exec-97148a95-9cf8-42f4-8be7-d169e31f1c23`.
- The two middle-strength labels now read exactly `MEDIUM`; `MODERATE` does
  not appear in the published image.
- The final PNG is byte-identical to the recorded output hash and was checked
  at native `1774x887` and simulated `608x304` lesson size.

### `07-correlation-05-churn-rate-monthly-charges-clean.png`

- The original JPG and retained crop remain unchanged and are retained as
  source/reference evidence; the crop is not used as a generated image input.
- Re-rendered deterministically from the exact lesson values: tenure `60%`,
  `40%`, `17%`; monthly charges `8%`, `18%`, `32%`.
- The y-axis is now explicitly scaled from `0%` to `60%`, with visible guides
  and ticks at `20%`, `40%`, and `60%`; the 60% and 40% bars terminate exactly
  on their corresponding guides.
- Native render spec: `1400x820` canvas, baseline `y=650`, `60%` guide
  `y=180`, `40%` guide `y=337`, `20%` guide `y=493`, rasterized from the
  deterministic SVG with ImageMagick `convert`.
- The final PNG was checked at native `1400x820` and simulated `608x356`
  lesson size; no screenshot overlays or camera artifacts are present.

## Focused correction: 2026-09-09

Two classification illustrations were regenerated after an independent audit
found an incorrect probability and unsupported invented content. The original
published PNGs were not used as imagegen inputs.

### `12-using-log-reg-04-production-diagram-imagegen.png`

- Imagegen inputs were the retained original JPG
  `12-using-log-reg-04-production-diagram.jpg` and the bounded crop
  `12-using-log-reg-04-production-diagram-imagegen-crop.jpg`.
- The crop geometry is `(10, 35, 480, 285)` from the `598x360` original.
- Imagegen output: `exec-dd4d8a99-c139-4a78-9d60-92d580dfba99`.
- The probability is now exactly `0.5968852088293909`; the prior published
  image incorrectly displayed `0.596885208293909`.
- The threshold flow is explicit: `p >= 0.5?` → `CHURN` →
  `PROMOTIONAL EMAIL`; the negative branch is `NO CHURN`.
- Source SHA-256:
  `c664421034f1332ee6d299fc314b0ea9f9952000e6f3b03d133fefe576635dcf`.
- Crop SHA-256:
  `76f93089d4d860fb903097080e053bd8dd74d6ca0cd2f625967ed3f559486b44`.
- Final SHA-256:
  `f382a888c202088abfc44e509f27a1f689eb46f02afbd031119771bd2fe14992`.
- Native output is `2163x727`; the output contains C2PA metadata identifying
  OpenAI image generation. It was inspected natively and at a simulated
  `608px` lesson width.

### `14-explore-more-01-preprocessing-model-comparison-imagegen.png`

- No original JPG or bounded crop exists for this illustration: it was added
  as a standalone generated asset in `e1337ff`.
- It was regenerated from the exact lesson concepts, without using the prior
  invented illustration as an imagegen input.
- Imagegen output:
  `exec-e1caf79f-87a8-4c14-a41e-02d51f3b1adc`.
- The replacement contains only lesson-grounded concepts: excluding least
  useful features; a scikit-learn train/validation/test split; OneHotEncoding;
  StandardScaler for `lbfgs`; LinearRegression; RidgeRegression; finding the
  best regularization parameter; and comparison on validation data.
- It intentionally contains no invented dataset rows, model leaderboard,
  validation scores, or unsupported model names.
- Previous final SHA-256:
  `83ab0805858c0509da3cad0cecc048e5dc0daa66ed5c025d3f2c44c7b844aa35`.
- Final SHA-256:
  `830ba83b35d13c9213ef33d6bfe1d8920be245eb3c58c8d7e1b1e34167a31df9`.
- Native output is `1536x1024`; the output contains C2PA metadata identifying
  OpenAI image generation. It was inspected natively and at a simulated
  `608px` lesson width.

## Focused current-reference audit: 2026-09-09

The current `*imagegen*.png` reference set contains exactly twelve published
targets across modules 02 and 03. This section records the eight
classification targets; the four regression targets are recorded in the
regression ledger. The existing target-specific records below were verified
against the committed/published bytes and left unchanged because they already
demonstrate valid imagegen provenance or, for the standalone illustration,
contain durable OpenAI C2PA evidence.

| Published target | Original source | Crop `(x,y,width,height)` | Retained crop | Imagegen output or C2PA evidence | Source SHA-256 | Crop SHA-256 | Final SHA-256 | Final dimensions | Disposition |
|---|---|---:|---|---|---|---|---|---:|---|
| `05-risk-03-difference-vs-risk-ratio-imagegen-pilot.png` | `05-risk-03-difference-vs-risk-ratio.jpg` | `(10,0,490,350)` | `05-risk-03-difference-vs-risk-ratio-imagegen-crop.jpg` | `exec-ae484b62-9986-4c3b-9999-c747e7ef0aeb` | `1e7f5d511bdd6780623065702a82f02dec57ab002f3ef16d83f8b79a0ea3efbe` | `56c155574e8778f92534b6f7c1dbca0549d2d0d1ae70b5dbedb8b6aa0a614dc0` | `12f2b1156249142115a6b1a922575e7eac77102194a4c7a35c09f45a4cd5b5b7` | `1619x971` | **UNCHANGED / ACCEPT** — existing target-specific imagegen ledger |
| `06-mutual-info-01-mutual-information-wikipedia-imagegen-pilot.png` | `06-mutual-info-01-mutual-information-wikipedia.jpg` | `(105,65,440,270)` | `06-mutual-info-01-mutual-information-wikipedia-imagegen-crop.jpg` | `exec-ca46d1d9-63e8-42c4-9bf6-546310985c94` | `64c7d86a57e0899d5ee759b526cdaec17802bb5b405c72ce1952e80c79a1e60b` | `b4a26ffbf558ea6ddbbfbaf0d8d363cf80b82d87249fd9c0be12136eb02b29bf` | `9b93593622941301cbac9d08005b108f603b5dda1a1dbff841ea5e04de85af26` | `1536x1024` | **UNCHANGED / ACCEPT** — existing target-specific imagegen ledger |
| `07-correlation-01-correlation-coefficient-imagegen-pilot.png` | `07-correlation-01-correlation-coefficient.jpg` | `(10,0,480,350)` | `07-correlation-01-correlation-coefficient-imagegen-crop.jpg` | `exec-97148a95-9cf8-42f4-8be7-d169e31f1c23` | `a88754f900a64e14d96f74ecc36a26f6e2322310ab9769ba83cdf7fb87f96316` | `dff673f926140e05f95bfa3c3b805dedd27a4398009a5b2915de8da0d00d1581` | `f6cbcf961aab153b1463e2a3c951655a3bc3f160f8ce280c8f98cafe80a01380` | `1774x887` | **UNCHANGED / ACCEPT** — existing target-specific imagegen ledger |
| `07-correlation-02-binary-target-imagegen-pilot.png` | `07-correlation-02-binary-target.jpg` | `(45,0,450,350)` | `07-correlation-02-binary-target-imagegen-crop.jpg` | `exec-5f193c35-4edd-440e-9576-56e27118fd67` | `74867c70734f8e679b4f02f58bfa1f2aa30a33f5b7c934a0894f773f9f7f8848` | `b9d95a058f5a4b3d39fc452251fe57bce976e9da789f3130c0e42cd6fced87e8` | `c50ad5128ea626cb0fe864ee7388b89736280dba132a85c459c72e9f10611e4c` | `1619x971` | **UNCHANGED / ACCEPT** — existing target-specific imagegen ledger |
| `11-log-reg-interpretation-06-second-example-imagegen.png` | `11-log-reg-interpretation-06-second-example-slide.jpg` | `(15,0,490,300)` | `11-log-reg-interpretation-06-second-example-imagegen-crop.jpg` | `exec-f038c40d-be8b-4c8e-a297-1f39a87fe554` | `c59aced91bc0f594b433dd1ab7a1c3eaae113f0e7d3453ba48e68423315a8082` | `3387f67f83e28bdb216b1dcea296e9d12d872b4f10e068336910dd2bb6b3f75a` | `4cb3aae78f2de1965ed44d77f0b449c01ae088b49c6acff5e14e20de42d380c5` | `2172x724` | **UNCHANGED / ACCEPT** — existing target-specific imagegen ledger |
| `12-using-log-reg-04-production-diagram-imagegen.png` | `12-using-log-reg-04-production-diagram.jpg` | `(10,35,480,285)` | `12-using-log-reg-04-production-diagram-imagegen-crop.jpg` | `exec-dd4d8a99-c139-4a78-9d60-92d580dfba99` | `c664421034f1332ee6d299fc314b0ea9f9952000e6f3b03d133fefe576635dcf` | `76f93089d4d860fb903097080e053bd8dd74d6ca0cd2f625967ed3f559486b44` | `f382a888c202088abfc44e509f27a1f689eb46f02afbd031119771bd2fe14992` | `2163x727` | **UNCHANGED / ACCEPT** — focused correction already has target-specific imagegen ledger |
| `13-summary-01-churn-prediction-imagegen.png` | `13-summary-01-churn-prediction-slide.jpg` | `(10,0,520,340)` | `13-summary-01-churn-prediction-imagegen-crop.jpg` | `exec-cfdf6aa4-d261-470e-9422-d31591a98c6d` | `6990dac4951ec303e71dfd997469a3181cbe3515a9596aebc0b73298b8cfada7` | `8ffb2de138d970ee6a4a98cafafd1f607b8a1408237858a605794537f54be9e2` | `050e5d9a2c91505c34aadf842cb2df18356f1acd76c4a1fc2f99a1f1a63d9f43` | `1617x973` | **UNCHANGED / ACCEPT** — existing target-specific imagegen ledger |
| `14-explore-more-01-preprocessing-model-comparison-imagegen.png` | `N/A — standalone generated asset; no target-specific source JPG exists` | `N/A` | `N/A — no source crop exists` | `C2PA claim `urn:c2pa:a45f683a-71ac-408e-8285-0cdd35a4476f`; execution ID not retained | `N/A` | `N/A` | `830ba83b35d13c9213ef33d6bfe1d8920be245eb3c58c8d7e1b1e34167a31df9` | `1536x1024` | **UNCHANGED / ACCEPT** — existing OpenAI C2PA imagegen output; no prior target was used |

### Inspection and invariants

- All eight classification targets were inspected at native resolution and at
  simulated 608px lesson width. Existing imagegen rows were byte-identical to
  their recorded final hashes and were therefore not regenerated.
- Their existing records preserve the exact formulas, percentages, labels,
  row order, binary values, plots, and relationship directions. Face, camera,
  browser/editor chrome, cursor, playback, and selection overlays are absent.
- `14` is intentionally a standalone generated illustration: no original JPG
  or bounded crop exists, but the committed/published PNG has OpenAI C2PA
  metadata identifying `gpt-image`. It was left unchanged rather than using
  an invented source chain or feeding the prior target back into imagegen.
- No imagegen target in this classification slice was created by upscaling,
  Lanczos resizing, or sharpening the previous published PNG.
