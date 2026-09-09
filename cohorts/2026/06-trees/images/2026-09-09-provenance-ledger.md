# 06-trees durable provenance — 2026-09-09

This ledger records durable source-to-crop provenance for the twelve
illustrations in this queue. Seven published PNGs retain their previously
accepted bytes. The four `10-summary` PNGs are regenerated in focused commits
from their original non-crisp JPGs and bounded crops; their previous PNGs are
never used as imagegen inputs. The final-model semantic correction to the
`10-summary-06` output and the later eta-plot semantic correction are recorded
below. The remaining strict-audit queue is recorded at the end: three
source-backed redraws and one retained direct-imagegen output.

## Method

The original non-crisp JPG is the source of truth. Each crop is made directly
from that JPG with the checked-in
[`2026-09-09-provenance-crops.sh`](2026-09-09-provenance-crops.sh) script and
ImageMagick's `-crop WIDTHxHEIGHT+X+Y` geometry. The camera tile, recorder
controls, browser chrome, and unrelated notebook cells are outside the crop
where applicable. The source JPG, crop JPG, and published imagegen PNG are all
retained together.

The seven earlier diagram crops use the coordinates recorded in the original
rollout notes. The eta plot has its own checked-in crop script because its
published output required a semantic repair. The four summary crops are
bounded content regions from the original notebook screenshots. Each
regenerated imagegen output is made using the original JPG and its matching
bounded crop only; the old crisp PNG is not supplied as a reference.

No sharpening, upscaling, or imagegen operation is performed by the crop
script. It only preserves the source content region needed to audit the
existing redraw. The crop-script SHA-256 is
`bd0219c40c9d4fe979ac2002d5268b4174270f68b49410b5e05d46add97fcd70`.

## Published assets and hashes

`Crop` is `(x, y, width, height)` in source-JPG pixels. The output hash is the
hash of the currently published PNG. Historical replacement hashes are
recorded in the relevant sections below.

| Published PNG | Source JPG | Crop JPG | Crop | Source SHA-256 | Crop SHA-256 | Published PNG SHA-256 |
|---|---|---|---|---|---|---|
| `03-decision-trees-01-risk-rules-tree-imagegen.png` | `03-decision-trees-01-risk-rules-tree.jpg` | `03-decision-trees-01-risk-rules-tree-imagegen-crop.jpg` | `(25, 0, 480, 260)` | `14353b2d6cb259dde5b8243b6db9cc6e28d4e3a44bc34d66840bc09b26cdddab` | `c4d1b8034f874a5abcb6036b5852ca29de15cf58a312591514900e49fa602dd5` | `726ff359fa548a53f8d66d6e1daae2de2b7bf61f06a73c282a63bb9cc9cf3024` |
| `03-decision-trees-05-memorizing-imagegen.png` | `03-decision-trees-05-memorizing.jpg` | `03-decision-trees-05-memorizing-imagegen-crop.jpg` | `(110, 0, 390, 330)` | `605d09793f95e952dd28c78b16f15fe73e03c2983bf3c3a7f48db271bd572c01` | `78648cad10d1109e8013c353d375ffdac65a3927211e50fcb6792fdc63e25cf3` | `f028a9c660fbbcad5737282f2366079286863d6e78baa6f9aea9146de7f9b98b` |
| `03-decision-trees-07-decision-stump-imagegen.png` | `03-decision-trees-07-decision-stump.jpg` | `03-decision-trees-07-decision-stump-imagegen-crop.jpg` | `(110, 0, 390, 330)` | `02c6a6abe95ee203216040410cfc00a6b5bfe0e2f22f164873dd64d8fa4394b2` | `023a9c3c73ab95d3b6b490c099e5653a8849272a11a4081659649bb639149ebe` | `8d6546d7985d7259b2105be20952764d9a972418955c617dcbd8cf33bba0ca46` |
| `06-random-forest-01-board-of-experts-imagegen.png` | `06-random-forest-01-board-of-experts.jpg` | `06-random-forest-01-board-of-experts-imagegen-crop.jpg` | `(22, 16, 980, 690)` | `2161f109ad9ccce9c2bfa8b2cbb80b22050e6acf0e03bba3bcbda3d018c8c7f2` | `4985f31201233adaf386363f4555da26e6b285b8b7a246cfd3714d68fc9b6361` | `dbf4eb53a9b6957420ee1f66484967b4313a12b5ac8497be2490a2450c490b8e` |
| `06-random-forest-02-random-forest-imagegen.png` | `06-random-forest-02-random-forest.jpg` | `06-random-forest-02-random-forest-imagegen-crop.jpg` | `(0, 0, 1024, 724)` | `75f8d5658760dcdfaefea7c973b4cf8a746fd9c6e375d5ddfe0eccb4d4e12456` | `b1cceb35bebee384489d14b7327d09617b59f6b57b2678cb4f05cb42849d452c` | `d6e1789d6fbff579082d24d5eb5918b6b57c454a6528771bd4422468fb19cf58` |
| `07-boosting-01-boosting-vs-random-forest-imagegen.png` | `07-boosting-01-boosting-vs-random-forest.jpg` | `07-boosting-01-boosting-vs-random-forest-imagegen-crop.jpg` | `(22, 16, 980, 690)` | `865043939c7a052fec06ed06dc994e9c3d5058203c222eb797d77b01ff1f375a` | `31e31a0d364d275c4b22a4a56a9ddf4975f7ff5a35a11ed540bb70efc9f11f07` | `9cbaf92f0b4873c4f490ccbf156992bf64c4ba2812141835b00cf621d7eeed0c` |
| `07-boosting-02-gradient-boosting-trees-imagegen.png` | `07-boosting-02-gradient-boosting-trees.jpg` | `07-boosting-02-gradient-boosting-trees-imagegen-crop.jpg` | `(22, 16, 980, 690)` | `2dfcf562c63bd65aa96d3be0e72525562ef79be972323d7e07ab48db3bb338b0` | `bddd9f8e349170110548d7af16cfe05ce47e77ddb6bdad2659032ebfec7c7e09` | `a8619de22d048dbb82e6eaecb874fc0b411c91e3220b8e9bbb1bf1b7aa3394ff` |
| `10-summary-01-summary-slide-imagegen.png` | `10-summary-01-summary-slide.jpg` | `10-summary-01-summary-slide-imagegen-crop.jpg` | `(90, 135, 480, 125)` | `f040bfcfe6907dceaf329142ecb5de1683b8fab8412566154ad78a6ee9fcf58c` | `9ea172f06fed75a05ed857c7ccf0a323e81d92136d677464fa2328a555c04507` | `2acae31c29ac3efa6133c5a8e784bbf59eb6fb8503d51496b92464b74a0a9d29` |
| `10-summary-04-random-forest-imagegen.png` | `10-summary-04-random-forest.jpg` | `10-summary-04-random-forest-imagegen-crop.jpg` | `(90, 119, 480, 88)` | `ffac132afa9bfd82af2badefc39aba56764fa31171e572be2050b44ce9dddf8b` | `0696e80a8bf60017d6d6bcf9b849977cc737797eb083507d6e9bc7272723a826` | `d8e3c86b1db44f081c9bc46a0af68d83adcfe74c82c9a5841d6e39d185d99f62` |
| `10-summary-05-gradient-boosting-imagegen.png` | `10-summary-05-gradient-boosting.jpg` | `10-summary-05-gradient-boosting-imagegen-crop.jpg` | `(90, 112, 480, 100)` | `e683e67e1f523516b904e4352ca263d5f92562b88ab4e7c81643a9fddadec028` | `335bf92b80a656cca19a2ef3a98a56db133428acc29f1e01b189c55f116b6e51` | `8c1f0c5cc57c66a2dc61595ad24f9351a0df92fac3791c1add5b5d9812b8eeac` |
| `10-summary-06-xgb-parameters-imagegen.png` | `10-summary-06-xgb-parameters.jpg` | `10-summary-06-xgb-parameters-imagegen-crop.jpg` | `(90, 78, 465, 185)` | `cda4ecf0d53f519cf4a6a423e400fa5c774021ac590edbf024b76c7cc28bd509` | `49bece48d65fe5ddc2b0cb978def7bc65fbd20905964def263dcc07c132e36a2` | `f7ef946bcb3e94af5ef8961a00b8d7829fc60e6de2a6e6e9f7f2abbb3a8801a8` |

## Summary regeneration verification

Each regenerated PNG was created with the built-in imagegen tool from the
listed original JPG and bounded crop. Native output and a simulated 608px-wide
render were inspected. The C2PA check looks for the embedded `c2pa` manifest
markers and the `gpt-image`/`OpenAI` signer strings in the PNG bytes.

| Asset | Imagegen execution | Native | 608px render | Output SHA-256 | C2PA |
|---|---|---:|---:|---|---|
| `10-summary-01-summary-slide-imagegen.png` | `exec-57e53a3e-351e-4ff0-9a04-ce4467526661` | `1672×941` | `608×342` | `2acae31c29ac3efa6133c5a8e784bbf59eb6fb8503d51496b92464b74a0a9d29` | `gpt-image` / `OpenAI` markers present |
| `10-summary-04-random-forest-imagegen.png` | `exec-f401ea09-8eb2-4616-a02c-60178685a757` | `1672×941` | `608×342` | `d8e3c86b1db44f081c9bc46a0af68d83adcfe74c82c9a5841d6e39d185d99f62` | `gpt-image` / `OpenAI` markers present |
| `10-summary-05-gradient-boosting-imagegen.png` | `exec-c4e4c248-3b52-4b58-961c-9cba8d1a480f` | `1672×941` | `608×342` | `8c1f0c5cc57c66a2dc61595ad24f9351a0df92fac3791c1add5b5d9812b8eeac` | `gpt-image` / `OpenAI` markers present |
| `10-summary-06-xgb-parameters-imagegen.png` | `exec-4f510fe9-bc65-43bc-a6c6-a6f91fd9cbcb` | `1672×941` | `608×342` | `f7ef946bcb3e94af5ef8961a00b8d7829fc60e6de2a6e6e9f7f2abbb3a8801a8` | `gpt-image` / `OpenAI` markers present |

## Verification

Before committing, the eleven published PNG hashes above were captured from the
working tree. This commit adds only the crop JPGs, the reproducibility script,
and this ledger; it does not touch lesson Markdown or published PNG bytes.

The imagegen outputs remain subject to the independent visual verdict already
recorded in the strict audit: crisp and semantically correct. This ledger
supplies the previously missing durable source/crop/output chain; it does not
make a new claim that the crops themselves are imagegen outputs.

## XGBoost semantic repair

The strict audit found one semantic defect in the existing XGBoost parameter
illustration: it used equality wording for `min_child_weight` and
`min_samples_leaf`. The replacement below was generated with the built-in
imagegen tool from the original JPG and the bounded crop only. The old PNG was
not used as an input. The replacement says `MIN_CHILD_WEIGHT — ROUGH ANALOGUE
OF MIN_SAMPLES_LEAF IN RF`, preserves the four-stage error-feedback flow, and
retains the green `0.3` annotation.

The crop is reproducible with
[`2026-09-09-xgb-repair-crop.sh`](2026-09-09-xgb-repair-crop.sh), whose
SHA-256 is `56b2bcb0f3341c794b8ab62f9e548c6ac22559be7fa8fbc7ab2a81bf1e9517bb`.
The previous PNG hash is included to make the semantic replacement explicit.

| Asset | Source JPG | Crop JPG | Crop `(x, y, width, height)` | Source SHA-256 | Crop SHA-256 | Previous PNG SHA-256 | Replacement PNG SHA-256 |
|---|---|---|---|---|---|---|---|
| `08-xgb-tuning-01-parameters-imagegen.png` | `08-xgb-tuning-01-parameters.jpg` | `08-xgb-tuning-01-parameters-imagegen-crop.jpg` | `(22, 16, 980, 690)` | `e9b4f5de1afa5b2056e94fc982e3171868aa3ae22b284341b348f6f46b196c8c` | `689cc01254d5e09bbeebb3203cef168e3dea483e52f8f051eec1716830c446e8` | `c555d68c99aa89e70f04c77d094ac40faa5c1e2d617087230b2e6c3aef4732a4` | `d8ad1d617aa0483d4fa3cc3677fed84822e71c533f03d15696cab88760ff8b53` |

Imagegen execution: `exec-8f42295c-8408-42af-84ae-7ece5c751291`. The output
contains C2PA metadata identifying OpenAI image generation. Native dimensions
are `1495×1052`; a simulated `608px` render was inspected and kept all
parameter text, stages, arrows, and the `0.3` annotation readable. The
replacement changes the published PNG intentionally; the eleven previously
recorded provenance-only PNGs above remain byte-for-byte unchanged.

## XGBoost final-model semantic correction

An independent review found that the previous `10-summary-06` redraw called
baseline values (`eta=0.3`, `max_depth=6`, `num_boost_round=200`) settings from
the final model. The replacement was generated with the built-in imagegen tool
from the original JPG and the tracked bounded crop only; neither the previous
crisp PNG nor an enlarged version was used as an input.

The replacement uses the exact final-model values from `08-xgb-tuning.md`:
`eta=0.1`, `max_depth=3`, `min_child_weight=1`, and
`num_boost_round=175`. It was inspected at native `1672×941` and at a
simulated `608×342` render. The parameter cards and code panel remain readable,
and the output has C2PA metadata identifying `gpt-image` / OpenAI image
generation.

| Asset | Previous PNG SHA-256 | Replacement PNG SHA-256 | Imagegen execution |
|---|---|---|---|
| `10-summary-06-xgb-parameters-imagegen.png` | `7b1cd924614f2247e6bd1b5bae299e5f9a2e000b00f977dcb673145970f969e7` | `f7ef946bcb3e94af5ef8961a00b8d7829fc60e6de2a6e6e9f7f2abbb3a8801a8` | `exec-4f510fe9-bc65-43bc-a6c6-a6f91fd9cbcb` |

## XGBoost eta plot semantic repair

The previous published plot was crisp but contradicted the lesson: the source
JPG's red trajectory was labeled `eta=0.05` and sat slightly above the green
`eta=0.1` trajectory, while the lesson caption and prose say that `eta=0.1`
reaches the top and stays stable. The replacement follows the lesson's stated
label semantics while retaining the source plot's five trajectories, axis
bounds, ticks, colors, and exact parameter labels. No new numeric values or
curves were invented; the conflicting red/green label assignment is recorded
explicitly rather than silently treated as a crispness pass.

The original JPG and its bounded crop were the only image references supplied
to imagegen. The previous published PNG was not used as an input, and the
output is a redraw rather than an enlargement or sharpened crop. The crop is
reproducible with
[`2026-09-09-xgb-eta-repair-crop.sh`](2026-09-09-xgb-eta-repair-crop.sh),
whose SHA-256 is
`f81babe3822d0744354d1018ce3e78feedf555bcb17fa4d3778d22d08611d618`.

| Asset | Source JPG | Crop JPG | Crop `(x, y, width, height)` | Source SHA-256 | Crop SHA-256 | Previous PNG SHA-256 | Replacement PNG SHA-256 |
|---|---|---|---|---|---|---|---|
| `08-xgb-tuning-02-tuning-eta-imagegen.png` | `08-xgb-tuning-02-tuning-eta.jpg` | `08-xgb-tuning-02-tuning-eta-imagegen-crop.jpg` | `(35, 35, 680, 500)` | `262bf7aad0ab9d0c70075321ee297ac56a4a1d51564c88c2942da89203f44085` | `d938225f7ed47593d6f71782dc9cc492a116b9df836247c437879fb45f8f9734` | `76d5073a442e076832bf59352991639b24bd3ac167b86d75a8454ea41d7de702` | `25a3a81a27ef43b96635edd2cca6f9bc2bc97d07f5a90455f4006da64981bfdd` |

Imagegen execution: `exec-55f38be5-de6e-4622-8ed2-9c7c36c712fe`. The output
contains C2PA metadata with URN
`urn:c2pa:7c94cf0c-ba5a-4da2-853f-bc8ba592c53b`. Native dimensions are
`1463×1075`; a simulated `608×447` lesson render was inspected. OCR at both
sizes retained all five legend labels and all axis tick labels. The output
contains no camera, face, browser, cursor, selection, or decorative overlay.
The normalized comparison against the source crop after resizing was
`0.205028` RMSE, confirming that the result is not a simple enlargement.

## Remaining strict-audit provenance queue — 2026-09-09

The strict audit classified four current `06-trees` references as
`PROVENANCE-BLOCKED`. Three had original non-crisp JPG sources and were
regenerated with built-in imagegen using the original JPG plus a matching
bounded native crop. The remaining `11-explore-more` infographic was already a
direct imagegen illustration with C2PA metadata and no underlying JPG; it is
retained byte-for-byte and documented separately.

The checked-in
[`2026-09-09-provenance-crops.sh`](2026-09-09-provenance-crops.sh) script now
also reproduces these three crops. Its current SHA-256 is
`bd0219c40c9d4fe979ac2002d5268b4174270f68b49410b5e05d46add97fcd70`.
It uses only native `-crop WIDTHxHEIGHT+X+Y`; it does not resize, Lanczos,
sharpen, or otherwise enhance the source. The prior published PNGs were not
supplied as imagegen references. Native outputs and temporary simulated 608px
lesson-width renders were inspected; the temporary renders are not published.

`RMSE` below is the normalized ImageMagick comparison against a temporary
resized crop and is included only to show that the published output is not a
resize-only copy.

### Source-backed redraws

| Published PNG | Lesson reference | Source JPG | Crop JPG | Crop `(x, y, width, height)` | Source SHA-256 | Crop SHA-256 | Previous PNG SHA-256 | Current PNG SHA-256 | Native | 608px | Imagegen execution | C2PA | RMSE |
|---|---|---|---|---|---|---|---|---|---:|---:|---|---|---:|
| `01-credit-risk-02-historical-data-imagegen.png` | `01-credit-risk.md:32` | `01-credit-risk-02-historical-data.jpg` | `01-credit-risk-02-historical-data-imagegen-crop.jpg` | `(120, 0, 260, 330)` | `24427766041b29b14f199161c5d2205b0afcb8fa002034d61eb5166753fe1652` | `ead8304237a173181970ea199bda83698c591548a978f84ecef94b82818055fc` | `b20b77d18c5b3d9c2ad33de2140ad03e26acdd56277e86c171e31bacfaf1c4df` | `e517ab930e53cdb67ca5fc78cfd09087c00e7a61a5363cedfaaee234f1b0cd56` | `1024x1536` | `405x608` | `exec-35aaff53-3193-4a18-89c9-383354616612` | `urn:c2pa:bbb51f0d-6766-4f0f-a385-aab83aeed6fb` | `0.207549` |
| `01-credit-risk-03-probability-of-default-imagegen.png` | `01-credit-risk.md:60` | `01-credit-risk-03-probability-of-default.jpg` | `01-credit-risk-03-probability-of-default-imagegen-crop.jpg` | `(100, 0, 300, 330)` | `a098b20d62c5b8348c1d133764233863b44f81c078add1d9401ad247b6dd3b6a` | `417a26931c8f79b000a42c74411a72c6becfdcc0071503ae1f6544974b0f3e4f` | `223559a26a08366b31587be8d377741ee6743955592848062f4a264b57caa5c4` | `70259e761f8d477171dcd88fec22e4b21c0271d715f3f723922a48848336b917` | `1536x1024` | `608x405` | `exec-be7eb770-89fa-485e-87a8-b8a8257cd077` | `urn:c2pa:a6dbd073-1e72-4615-9dc0-c344f189e9f0` | `0.237373` |
| `09-final-model-01-comparing-validation-imagegen.png` | `09-final-model.md:19` | `09-final-model-01-comparing-validation.jpg` | `09-final-model-01-comparing-validation-imagegen-crop.jpg` | `(0, 38, 500, 322)` | `c34252012dcc810d04ba5d122600703536ec59ead2bf79f0b1f70eb15adea179` | `4d1c65604abeae8bb20ae6b6ec06112b1887e98e2d4bcefab1e6fc82a8183c1d` | `bf7b4a3556e16fdd72a435c22a614dc02aaf7e85fe1e9b70838a5f6dff7be0a5` | `2e10aa735c2a3c0c2cf1f977e710b24c13aba2cd9bfcdb94c1c96ddb3a300e63` | `1617x973` | `608x366` | `exec-6164d31d-9258-40a8-9bc6-599e779bc709` | `urn:c2pa:0595c755-54e8-48cb-9f35-310258ccc0d3` | `0.256670` |

### Preserved invariants and removed artifacts

- Historical outcomes remain exactly `OK`, `OK`, `DEFAULT`, `DEFAULT`, `OK`.
- The probability illustration retains `y`, `y ∈ {0,1}`, the `OK`/`DEFAULT`
  mapping, and `g(xᵢ) → PROB OF DEFAULT`.
- The final-model comparison retains the exact validation AUC values
  `0.7850802838390931`, `0.8249709379767989`, and `0.8360387251459157`, the
  exact tuned parameters, and the XGBoost winner callout.
- Webcam tiles, color-wheel controls, browser/editor chrome, cursors, play
  controls, selection overlays, and notebook framing were removed from all
  three redraws.

### Retained direct imagegen output

| Published PNG | Lesson reference | Current PNG SHA-256 | Native | 608px | C2PA | Decision |
|---|---|---|---:|---:|---|---|
| `11-explore-more-01-ensemble-experiments-imagegen.png` | `11-explore-more.md:4` | `ec08605928cb35a3cf3ad47e3517df2d4e5596523b7d4dd49bb7daa8608f153f` | `1672x941` | `608x342` | `urn:c2pa:bb311753-4a6f-4e4c-8d34-f63a69a2dc76` | Retained byte-for-byte. This is a brand-new conceptual infographic with no original non-crisp JPG in the module. Its embedded C2PA record proves direct imagegen; native/608px inspection found no face, camera tile, browser/editor chrome, cursor, play control, or selection overlay. The illustrated whiteboard frame and tray are part of the composition, not capture chrome. |

No source/crop pair is fabricated for this direct imagegen asset.
