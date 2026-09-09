# Serverless visual provenance repair — 2026-09-09

This ledger records the 7 provenance-blocked active refs in module 09 from the
strict visual audit (12 active image refs in this module; 56 across modules
08–09). The five accepted refs in this module were left byte-for-byte
unchanged; their current API Gateway evidence remains in
`2026-09-08-ui-screenshot-removal-evidence.md`.

## Method

The four source-backed conceptual redraws use:

```text
original 592x360 JPG -> bounded native crop JPG -> imagegen PNG
```

`2026-09-09-provenance-crops.sh` records the crop-only operation. It uses
`-crop` and `+repage` only, with no resize, Lanczos, sharpen, or prior PNG as
input. Both the original JPG and its crop were supplied to each imagegen call.
The regenerated PNGs carry the imagegen C2PA marker (`jumdc2pa`). Native and
simulated 608px renders were inspected.

## Four regenerated imagegen refs

| Active output | Source chain | Execution |
|---|---|---|
| `01-intro-01-clothes-classification-use-case-imagegen.png` | matching original JPG + `...-imagegen-crop.jpg` | `exec-e37dd471-2981-44ac-86bf-58bc36afc966` |
| `01-intro-02-aws-lambda-deployment-imagegen.png` | matching original JPG + `...-imagegen-crop.jpg` | `exec-e1cd9e1f-c0a0-4dae-b647-4ecdda7084eb` |
| `01-intro-03-lambda-uses-tf-lite-imagegen.png` | matching original JPG + `...-imagegen-crop.jpg` | `exec-c1d070ff-85d5-4dd2-ad8e-9995880fb153` |
| `02-aws-lambda-07-serverless-vs-serverful-imagegen.png` | matching original JPG + `...-imagegen-crop.jpg` | `exec-897ed361-6a2c-4072-ad9d-837aec75968b` |

The redraws preserve the overview/Lambda/TF-Lite labels, arrows, clothing
icons, and the AWS Lambda plot while excluding presenter, face, camera,
browser/editor chrome, cursor, play/selection/recording UI, gauge overlays,
page counters, and black borders.

## One deterministic/native exact code artifact

`03-tensorflow-lite-02-03-predictions-to-tflite-crisp.png` is rendered from
the checked-in `2026-09-09-tflite-artifact.svg`, not from imagegen or a
resized screenshot. Its source evidence is retained as two native crops:

- `03-tensorflow-lite-02-keras-predictions-native-crop.jpg`, crop
  `500x330+0+30`, supplies the exact `preds = model.predict(X)` output and
  all ten float32 scores, including `9.887159`.
- `03-tensorflow-lite-03-convert-to-tflite-native-crop.jpg`, crop
  `500x330+0+30`, supplies the exact converter and
  `clothing-model.tflite` write code.

The SVG renderer preserves the code and values in a clean, bounded layout;
browser/editor/cursor/play/selection/camera overlays and transient warnings
are absent. The crop script regenerates the 1600x900 PNG directly from the
SVG without resizing.

## Two current direct-imagegen refs left unchanged

These refs have no same-stem source JPG in module 09. They are current clean
prompt-native imagegen assets with C2PA evidence, and were inspected natively
and at simulated 608px rather than regenerated from invented source material:

| Active output | Evidence |
|---|---|
| `09-explore-more-01-serverless-models-imagegen.png` | unchanged; 1672x941; C2PA `jumdc2pa`; clean serverless-models visual |
| `updates-01-runtime-compatibility-imagegen.png` | unchanged; 1672x941; C2PA `jumdc2pa`; clean runtime-compatibility visual |
