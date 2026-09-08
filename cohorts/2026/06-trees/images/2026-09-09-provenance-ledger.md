# 06-trees durable provenance — 2026-09-09

This ledger closes the provenance-only queue from the strict visual audit. It
covers the eleven published illustrations that were already visually crisp and
semantically accepted, but did not have a durable source-to-crop record. The
published PNGs were not regenerated or modified in this commit.

## Method

The original non-crisp JPG is the source of truth. Each crop is made directly
from that JPG with the checked-in
[`2026-09-09-provenance-crops.sh`](2026-09-09-provenance-crops.sh) script and
ImageMagick's `-crop WIDTHxHEIGHT+X+Y` geometry. The camera tile, recorder
controls, browser chrome, and unrelated notebook cells are outside the crop
where applicable. The source JPG, crop JPG, and already-published imagegen PNG
are all retained together.

The seven diagram crops use the coordinates recorded in the original rollout
notes. The four summary crops are bounded reconstructions from the original
notebook screenshots: the earlier rollout recorded the source/output pairing
but not the crop coordinates, so this commit makes the selected content region
durable without rewriting the existing PNG. That distinction is recorded here
instead of treating a newly reconstructed crop as proof of an unavailable
historical temporary file.

No sharpening, upscaling, or imagegen operation is performed by the crop
script. It only preserves the source content region needed to audit the
existing redraw. The crop-script SHA-256 is
`6b4abd9aed9ae0b9ccd49a7018dc8bd07158e0b1f407ea8c6ca2252d33d6077d`.

## Published assets and hashes

`Crop` is `(x, y, width, height)` in source-JPG pixels. The output hash is the
hash of the PNG already present before this commit.

| Published PNG | Source JPG | Crop JPG | Crop | Source SHA-256 | Crop SHA-256 | Published PNG SHA-256 |
|---|---|---|---|---|---|---|
| `03-decision-trees-01-risk-rules-tree-imagegen.png` | `03-decision-trees-01-risk-rules-tree.jpg` | `03-decision-trees-01-risk-rules-tree-imagegen-crop.jpg` | `(25, 0, 480, 260)` | `14353b2d6cb259dde5b8243b6db9cc6e28d4e3a44bc34d66840bc09b26cdddab` | `c4d1b8034f874a5abcb6036b5852ca29de15cf58a312591514900e49fa602dd5` | `726ff359fa548a53f8d66d6e1daae2de2b7bf61f06a73c282a63bb9cc9cf3024` |
| `03-decision-trees-05-memorizing-imagegen.png` | `03-decision-trees-05-memorizing.jpg` | `03-decision-trees-05-memorizing-imagegen-crop.jpg` | `(110, 0, 390, 330)` | `605d09793f95e952dd28c78b16f15fe73e03c2983bf3c3a7f48db271bd572c01` | `78648cad10d1109e8013c353d375ffdac65a3927211e50fcb6792fdc63e25cf3` | `f028a9c660fbbcad5737282f2366079286863d6e78baa6f9aea9146de7f9b98b` |
| `03-decision-trees-07-decision-stump-imagegen.png` | `03-decision-trees-07-decision-stump.jpg` | `03-decision-trees-07-decision-stump-imagegen-crop.jpg` | `(110, 0, 390, 330)` | `02c6a6abe95ee203216040410cfc00a6b5bfe0e2f22f164873dd64d8fa4394b2` | `023a9c3c73ab95d3b6b490c099e5653a8849272a11a4081659649bb639149ebe` | `8d6546d7985d7259b2105be20952764d9a972418955c617dcbd8cf33bba0ca46` |
| `06-random-forest-01-board-of-experts-imagegen.png` | `06-random-forest-01-board-of-experts.jpg` | `06-random-forest-01-board-of-experts-imagegen-crop.jpg` | `(22, 16, 980, 690)` | `2161f109ad9ccce9c2bfa8b2cbb80b22050e6acf0e03bba3bcbda3d018c8c7f2` | `4985f31201233adaf386363f4555da26e6b285b8b7a246cfd3714d68fc9b6361` | `dbf4eb53a9b6957420ee1f66484967b4313a12b5ac8497be2490a2450c490b8e` |
| `06-random-forest-02-random-forest-imagegen.png` | `06-random-forest-02-random-forest.jpg` | `06-random-forest-02-random-forest-imagegen-crop.jpg` | `(0, 0, 1024, 724)` | `75f8d5658760dcdfaefea7c973b4cf8a746fd9c6e375d5ddfe0eccb4d4e12456` | `b1cceb35bebee384489d14b7327d09617b59f6b57b2678cb4f05cb42849d452c` | `d6e1789d6fbff579082d24d5eb5918b6b57c454a6528771bd4422468fb19cf58` |
| `07-boosting-01-boosting-vs-random-forest-imagegen.png` | `07-boosting-01-boosting-vs-random-forest.jpg` | `07-boosting-01-boosting-vs-random-forest-imagegen-crop.jpg` | `(22, 16, 980, 690)` | `865043939c7a052fec06ed06dc994e9c3d5058203c222eb797d77b01ff1f375a` | `31e31a0d364d275c4b22a4a56a9ddf4975f7ff5a35a11ed540bb70efc9f11f07` | `9cbaf92f0b4873c4f490ccbf156992bf64c4ba2812141835b00cf621d7eeed0c` |
| `07-boosting-02-gradient-boosting-trees-imagegen.png` | `07-boosting-02-gradient-boosting-trees.jpg` | `07-boosting-02-gradient-boosting-trees-imagegen-crop.jpg` | `(22, 16, 980, 690)` | `2dfcf562c63bd65aa96d3be0e72525562ef79be972323d7e07ab48db3bb338b0` | `bddd9f8e349170110548d7af16cfe05ce47e77ddb6bdad2659032ebfec7c7e09` | `a8619de22d048dbb82e6eaecb874fc0b411c91e3220b8e9bbb1bf1b7aa3394ff` |
| `10-summary-01-summary-slide-imagegen.png` | `10-summary-01-summary-slide.jpg` | `10-summary-01-summary-slide-imagegen-crop.jpg` | `(90, 135, 480, 125)` | `f040bfcfe6907dceaf329142ecb5de1683b8fab8412566154ad78a6ee9fcf58c` | `9ea172f06fed75a05ed857c7ccf0a323e81d92136d677464fa2328a555c04507` | `f9087032532993fba784c1b6a5bc10c62d8f64f257d18ffe74166e2348e4ab15` |
| `10-summary-04-random-forest-imagegen.png` | `10-summary-04-random-forest.jpg` | `10-summary-04-random-forest-imagegen-crop.jpg` | `(90, 119, 480, 88)` | `ffac132afa9bfd82af2badefc39aba56764fa31171e572be2050b44ce9dddf8b` | `0696e80a8bf60017d6d6bcf9b849977cc737797eb083507d6e9bc7272723a826` | `13be16cd3710a309b94ed85290c67aa26e05d124ec086bf6ddf35b0dfd473952` |
| `10-summary-05-gradient-boosting-imagegen.png` | `10-summary-05-gradient-boosting.jpg` | `10-summary-05-gradient-boosting-imagegen-crop.jpg` | `(90, 112, 480, 100)` | `e683e67e1f523516b904e4352ca263d5f92562b88ab4e7c81643a9fddadec028` | `335bf92b80a656cca19a2ef3a98a56db133428acc29f1e01b189c55f116b6e51` | `65d9564776a5655b8b2e62d964d8a795d003ea52eeac1070764177dd6eed2c6a` |
| `10-summary-06-xgb-parameters-imagegen.png` | `10-summary-06-xgb-parameters.jpg` | `10-summary-06-xgb-parameters-imagegen-crop.jpg` | `(90, 78, 465, 185)` | `cda4ecf0d53f519cf4a6a423e400fa5c774021ac590edbf024b76c7cc28bd509` | `49bece48d65fe5ddc2b0cb978def7bc65fbd20905964def263dcc07c132e36a2` | `cd72aee95feb68e91c1ae663bbe75856a2bca33e7449d84d02c07c5d6b342d3e` |

## Verification

Before committing, the eleven published PNG hashes above were captured from the
working tree. This commit adds only the crop JPGs, the reproducibility script,
and this ledger; it does not touch lesson Markdown or published PNG bytes.

The imagegen outputs remain subject to the independent visual verdict already
recorded in the strict audit: crisp and semantically correct. This ledger
supplies the previously missing durable source/crop/output chain; it does not
make a new claim that the crops themselves are imagegen outputs.
