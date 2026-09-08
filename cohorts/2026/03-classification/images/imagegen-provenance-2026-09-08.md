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
