# Evaluation provenance repair — 2026-09-09

This ledger covers the 15 evaluation illustrations that remained unresolved
after the strict visual audit. Every original non-crisp JPG is retained. A
bounded crop is recreated directly from that JPG by
`2026-09-09-provenance-crops.sh` and is tracked beside the source.

Disposition rules for this batch:

- conceptual visuals are redrawn with the original JPG and bounded crop as
  imagegen inputs;
- exact confusion counts already represented by native lesson tables/output
  are removed from Markdown rather than turned into generated text;
- ROC charts are rebuilt deterministically from the lesson/notebook logic, not
  generated from a screenshot, because their curve points are instructional
  data; their crops remain reference evidence;
- no previous crisp PNG is supplied as an imagegen input, and no source is
  enlarged or sharpened.

## Crop reproduction

Run from this directory:

```bash
./2026-09-09-provenance-crops.sh .
```

The script uses ImageMagick `convert`, `+repage`, JPEG
`-sampling-factor 2x2`, and `-quality 90`. Coordinates below are relative to
the unchanged source JPGs.

## Asset ledger

| Published target | Original source | Crop `(x,y,width,height)` | Source SHA-256 | Crop SHA-256 | Disposition |
|---|---|---:|---|---|---|
| `01-overview-02-churn-scenario-crisp.png` | `01-overview-02-churn-scenario.jpg` | `(10,0,490,350)` | `cc9e70c271e6dc28e0e6b0bf55992f946727acce02bbec601a9c1a4c53b3115f` | `6ad75a35769c0ad2496037b31ecdb9c3c2fc3a997fd0c3e561b7296c348bd94c` | imagegen — pending output |
| `02-accuracy-08-class-imbalance-crisp.png` | `02-accuracy-08-class-imbalance.jpg` | `(10,0,500,350)` | `1eb6b87db34c62028e305109c6a81a2a1e671363b329821dfc91b7d2fd08a6d7` | `0ef99b504469b73ddc0f3873d6872ec3c313ec734e57fd8d98bfb4eb10e2a827` | imagegen — pending output |
| `03-confusion-table-01-four-outcomes-crisp.png` | `03-confusion-table-01-four-outcomes.jpg` | `(10,0,500,350)` | `b1930d3330a469f90615eddba7be04b55e33439661fe7e7474885c06c21deec3` | `69832542a0ee0f5801df44c9c874d6feb05acd4e8f4911e21b835fba2186cb41` | imagegen — pending output |
| `03-confusion-table-04-confusion-counts-crisp.png` | `03-confusion-table-04-confusion-counts.jpg` | `(10,0,500,350)` | `5bd9df275d2afed47a8bb5f2612e452bf52e9465b3bd3988396c9540c0f97527` | `52726bf52229a82b77388343bc1e7122fe99a7009b35a7ffb1248dfeb1e25410` | remove embed; native counts/table remain |
| `04-precision-recall-03-precision-pie-crisp.png` | `04-precision-recall-03-precision-pie.jpg` | `(15,0,500,350)` | `0e7a6085a9be56f30a7b4024ecf1be6ed0dd1e236ad857eb9058f68d49b3700b` | `27fbed72ca7e9755e24e32dd6a4615bba888d2a08122643b14cc4da9ca22f542` | imagegen — pending output |
| `04-precision-recall-05-recall-example-crisp.png` | `04-precision-recall-05-recall-example.jpg` | `(10,0,500,350)` | `7cbd46c699efd4e6ca6f639045e5db312cec9df119720ffd04d6316dc315e960` | `1673e4609c6779595229eb8d074d2fb28c8e1a3a1e6787d528cf44fdaef5073f` | imagegen — pending output |
| `05-roc-01-tpr-fpr-vs-threshold-crisp.png` | `05-roc-01-tpr-fpr-vs-threshold.jpg` | `(4,4,364,238)` | `39ffa6dbe8f4d84a34230c295e9015e8536b3270f0f697712d0837b2cefe4d06` | `e8f13e75ca5266d87e9f689e673df411d0eaebe5b02d1e3a4ac7db417852111e` | deterministic native chart — pending output |
| `05-roc-02-random-model-tpr-fpr-crisp.png` | `05-roc-02-random-model-tpr-fpr.jpg` | `(4,4,364,238)` | `a7f2c2cf457dacbfaee988596642fc0fb103619ee3b14bcaf9d6346dbb3e29bc` | `7eae8c5dfc446977ea135e52ce10cf6a5857f302f4a9cd8878ddd0922d4b22ef` | deterministic native chart — pending output |
| `05-roc-03-ideal-model-tpr-fpr-crisp.png` | `05-roc-03-ideal-model-tpr-fpr.jpg` | `(4,4,364,238)` | `abffffe11b9cfc7f7e6c554933c99ac1da6458db263f7fc4cffffd3204535933` | `3e33e1af9ba349a3baa5fa75ffa66ac6233f5fd5ec3e50eb0f6fbaa224beca0c` | deterministic native chart — pending output |
| `05-roc-04-model-vs-ideal-tpr-fpr-crisp.png` | `05-roc-04-model-vs-ideal-tpr-fpr.jpg` | `(4,4,364,238)` | `0533987b275ec0b1118887441d0af3482eeebe5ade41bb272a66f07820696cc4` | `d250df2320e28e2c4476882cc6bc6a59466014c6c5b5b437e926119cb9fa353c` | deterministic native chart — pending output |
| `05-roc-05-roc-curve-manual-crisp.png` | `05-roc-05-roc-curve-manual.jpg` | `(4,4,322,309)` | `1addce45368858d5a96dafa1e07d7dcd659e8eeca29bf4bc109695704b1f5c84` | `76c83c102e475276533c930d24cd3f16b3cb36a5a153423837a0149630cf973c` | deterministic native chart — pending output |
| `05-roc-06-roc-curve-sklearn-crisp.png` | `05-roc-06-roc-curve-sklearn.jpg` | `(4,4,322,309)` | `2d2e3c6325a5c28828a4df66db56243ce62015060679f038b1c484a27c8e7c36` | `b6a97ac99930c325dcaf0b2858bd670c198cb560b72902aad9deac60a774af54` | deterministic native chart — pending output |
| `06-auc-02-auc-values-imagegen.png` | `06-auc-02-auc-values.jpg` | `(10,0,500,350)` | `da29ae05753eede39cc22e2d11eecf0f8465fa335f81d05f4ae0498004c4cc5e` | `06f1a007b353b5157877b99eb094482173e9182314df339acae6a57856a000ee` | imagegen — pending output |
| `06-auc-05-auc-interpretation-imagegen-v2.png` | `06-auc-05-auc-interpretation.jpg` | `(10,0,500,350)` | `28f93877c6827ed0d37bc43955f8e38c2e9e0327263ca8eadf7055a9c4e92a90` | `21dce63fa706a8016738e2158e066b1af92b095b5bf70e99a50003a73087fd92` | imagegen — pending output |
| `07-cross-validation-01-kfold-diagram-pilot.png` | `07-cross-validation-01-kfold-diagram.jpg` | `(10,0,500,350)` | `be4a0491f5819eb3549c42c6be435630c18f162043bc46588ebdbf69e5dd9289` | `53db61fa6ae6d929c4833bec53b9513135688905f5d72988d243b2319627b5d4` | imagegen — pending output |

The output hash, generation ID, C2PA marker, and native/608px validation are
added to each row immediately after the corresponding asset is completed.
