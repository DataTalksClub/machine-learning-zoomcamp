# Classification provenance repair — 2026-09-09

This ledger records the four previously provenance-unresolved illustrations
from the strict classification audit. The original non-crisp JPGs were left
unchanged. A bounded crop was created directly from each original with
`2026-09-09-provenance-crops.sh`; both the original JPG and the retained crop
were supplied to the built-in imagegen tool. The previous published PNG was
not supplied as an input.

The generated PNG was copied byte-for-byte into the published target. Each
asset was inspected at native resolution and at a simulated 608px lesson
width. The outputs contain C2PA metadata identifying `gpt-image` and the
OpenAI Media Service. C2PA is recorded as provenance evidence only; the
semantic checks below are also required.

## Reproducible crop commands

Run from this directory:

```bash
./2026-09-09-provenance-crops.sh .
```

The script uses ImageMagick `convert`, `+repage`, JPEG `-sampling-factor 2x2`,
and `-quality 90`. The crop coordinates are relative to the unchanged source
JPGs.

## Source, crop, and output ledger

| Published target | Original source | Crop `(x,y,width,height)` | Imagegen output | Source SHA-256 | Crop SHA-256 | Final SHA-256 | Final dimensions |
|---|---|---:|---|---|---|---|---:|
| `05-risk-03-difference-vs-risk-ratio-imagegen-pilot.jpg` | `05-risk-03-difference-vs-risk-ratio.jpg` | `(10,0,490,350)` | `exec-ae484b62-9986-4c3b-9999-c747e7ef0aeb.png` | `1e7f5d511bdd6780623065702a82f02dec57ab002f3ef16d83f8b79a0ea3efbe` | `56c155574e8778f92534b6f7c1dbca0549d2d0d1ae70b5dbedb8b6aa0a614dc0` | `12f2b1156249142115a6b1a922575e7eac77102194a4c7a35c09f45a4cd5b5b7` | `1619x971` |
| `06-mutual-info-01-mutual-information-wikipedia-imagegen-pilot.jpg` | `06-mutual-info-01-mutual-information-wikipedia.jpg` | `(105,65,440,270)` | `exec-ca46d1d9-63e8-42c4-9bf6-546310985c94.png` | `64c7d86a57e0899d5ee759b526cdaec17802bb5b405c72ce1952e80c79a1e60b` | `b4a26ffbf558ea6ddbbfbaf0d8d363cf80b82d87249fd9c0be12136eb02b29bf` | `9b93593622941301cbac9d08005b108f603b5dda1a1dbff841ea5e04de85af26` | `1536x1024` |
| `11-log-reg-interpretation-06-second-example-imagegen.jpg` | `11-log-reg-interpretation-06-second-example-slide.jpg` | `(15,0,490,300)` | `exec-f038c40d-be8b-4c8e-a297-1f39a87fe554.png` | `c59aced91bc0f594b433dd1ab7a1c3eaae113f0e7d3453ba48e68423315a8082` | `3387f67f83e28bdb216b1dcea296e9d12d872b4f10e068336910dd2bb6b3f75a` | `4cb3aae78f2de1965ed44d77f0b449c01ae088b49c6acff5e14e20de42d380c5` | `2172x724` |
| `13-summary-01-churn-prediction-imagegen.jpg` | `13-summary-01-churn-prediction-slide.jpg` | `(10,0,520,340)` | `exec-cfdf6aa4-d261-470e-9422-d31591a98c6d.png` | `6990dac4951ec303e71dfd997469a3181cbe3515a9596aebc0b73298b8cfada7` | `8ffb2de138d970ee6a4a98cafafd1f607b8a1408237858a605794537f54be9e2` | `050e5d9a2c91505c34aadf842cb2df18356f1acd76c4a1fc2f99a1f1a63d9f43` | `1617x973` |

## Dispositions and semantic checks

- `05-risk-03`: **REGENERATED / ACCEPT**. The redraw preserves `GLOBAL -
  GROUP`, the sign meanings for difference, and `RISK = GROUP / GLOBAL` with
  the correct `> 1` and `< 1` interpretations.
- `06-mutual-info-01`: **REGENERATED / ACCEPT**. The redraw preserves mutual
  information as the overlap between `X` and `Y`, with `H(X)`, `H(Y)`,
  conditional entropy, and joint entropy labels. It removes the Wikipedia
  browser capture while staying faithful to the lesson's concept.
- `11-log-reg-interpretation-06`: **REGENERATED / ACCEPT**. The equation
  preserves `-2.47`, the one-hot contract terms `1 × 0.97`, `0 × (-0.025)`,
  `0 × (-0.949)`, the values `50 × 0.027` and `5 × (-0.036)`, and the result
  `-0.33`. No unsupported probability was added.
- `13-summary-01`: **REGENERATED / ACCEPT**. The redraw preserves the Telco
  churn-scoring flow, all six source scores (`0.20`, `0.30`, `0.35`, `0.40`,
  `0.45`, `0.85`), and the promotional-email action for the selected high-risk
  customer. It removes the lecturer/camera and does not add an accuracy claim.

No image was enlarged or sharpened. No prior crisp PNG was used as an
imagegen input. The four source JPGs and four bounded crops remain tracked for
future independent verification.
