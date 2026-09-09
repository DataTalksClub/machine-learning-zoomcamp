# AUC and cross-validation illustration provenance — 2026-09-09

This focused ledger closes the provenance gaps for the three existing
evaluation illustrations below. The published PNGs were not regenerated or
otherwise modified in this batch.

- `06-auc-02-auc-values-imagegen.png`
- `06-auc-05-auc-interpretation-imagegen-v2.png`
- `07-cross-validation-01-kfold-diagram-pilot.png`

Each original non-crisp JPG is retained. The bounded crop is recreated from
that JPG by `2026-09-09-auc-cv-crops.sh`, and the tracked crop is the exact
byte-for-byte result of that command. The reference crops intentionally retain
the source recording artifacts; they are audit evidence for the source-to-crop
chain, while the published imagegen outputs remove those artifacts.

## Reproduce the crops

Run this from the `images` directory, or invoke the script by path with no
argument:

```bash
./2026-09-09-auc-cv-crops.sh
```

The script uses ImageMagick `convert`, `+repage`, JPEG sampling factor
`2x2`, and quality `90`. Coordinates are relative to the unchanged `598x360`
source JPGs.

| Published target | Original JPG | Crop `(x,y,width,height)` | Tracked crop |
|---|---|---:|---|
| `06-auc-02-auc-values-imagegen.png` | `06-auc-02-auc-values.jpg` | `(10,0,500,350)` | `06-auc-02-auc-values-imagegen-crop.jpg` |
| `06-auc-05-auc-interpretation-imagegen-v2.png` | `06-auc-05-auc-interpretation.jpg` | `(10,0,500,350)` | `06-auc-05-auc-interpretation-imagegen-crop.jpg` |
| `07-cross-validation-01-kfold-diagram-pilot.png` | `07-cross-validation-01-kfold-diagram.jpg` | `(10,0,500,350)` | `07-cross-validation-01-kfold-diagram-imagegen-crop.jpg` |

## Hash and validation ledger

| Target | Source JPG SHA-256 | Crop SHA-256 | Published PNG SHA-256 | Native | Simulated 608px |
|---|---|---|---|---:|---:|
| `06-auc-02-auc-values-imagegen.png` | `da29ae05753eede39cc22e2d11eecf0f8465fa335f81d05f4ae0498004c4cc5e` | `06f1a007b353b5157877b99eb094482173e9182314df339acae6a57856a000ee` | `c253c5be4dd16c13eed85d9e30ca8ace12036a41225d087c4c51b9231af87d51` | `1536x1024` | `608x405` |
| `06-auc-05-auc-interpretation-imagegen-v2.png` | `28f93877c6827ed0d37bc43955f8e38c2e9e0327263ca8eadf7055a9c4e92a90` | `21dce63fa706a8016738e2158e066b1af92b095b5bf70e99a50003a73087fd92` | `8fa7125e9377a527db08a9ace4edc4362683abdba1a2a30cf3a77778ac753f2f` | `1536x1024` | `608x405` |
| `07-cross-validation-01-kfold-diagram-pilot.png` | `be4a0491f5819eb3549c42c6be435630c18f162043bc46588ebdbf69e5dd9289` | `53db61fa6ae6d929c4833bec53b9513135688905f5d72988d243b2319627b5d4` | `f938c052d7f8994483b01bc97bc7b158f4d7e1a26bf4458fbd9124b25d45d9fd` | `1647x955` | `608x353` |

The 608px renders were generated with `convert target.png -resize 608x608`
for inspection only; they are not published. All three native PNGs remain
semantically faithful to their lesson captions and were readable in the
simulated 608px renders.

## C2PA check

All three published PNGs contain C2PA payload markers identifying `gpt-image`
and `OpenAI Media Service`. The check used for this batch was:

```bash
strings -a target.png | rg -q 'gpt-image'
strings -a target.png | rg -q 'OpenAI Media Service'
```

This records presence of the C2PA generator markers together with the exact
published output hash; it does not replace a semantic visual review.
