# Serverless visual provenance repair — 2026-09-09

This ledger records the 7 provenance-blocked active refs in module 09 from the
strict visual audit (12 active image refs in this module; 56 across modules
08–09). Before this repair, module 09 was `12 = 7 blocked + 5 accepted`, and
the combined 08–09 arithmetic was `56 = 35 blocked + 21 accepted`. The five
accepted refs in this module were left byte-for-byte unchanged; their current
API Gateway evidence remains in
`2026-09-08-ui-screenshot-removal-evidence.md`.
After the repair, module 09 is `12 = 0 blocked + 12 accepted`, while the
combined set is `56 = 0 blocked + 56 accepted`; all 35 formerly blocked active
refs are now accepted.

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
| `01-intro-01-clothes-classification-use-case-imagegen.jpg` | matching original JPG + `...-imagegen-crop.jpg` | `exec-e37dd471-2981-44ac-86bf-58bc36afc966` |
| `01-intro-02-aws-lambda-deployment-imagegen.jpg` | matching original JPG + `...-imagegen-crop.jpg` | `exec-e1cd9e1f-c0a0-4dae-b647-4ecdda7084eb` |
| `01-intro-03-lambda-uses-tf-lite-imagegen.jpg` | matching original JPG + `...-imagegen-crop.jpg` | `exec-c1d070ff-85d5-4dd2-ad8e-9995880fb153` |
| `02-aws-lambda-07-serverless-vs-serverful-imagegen.jpg` | matching original JPG + `...-imagegen-crop.jpg` | `exec-897ed361-6a2c-4072-ad9d-837aec75968b` |

The redraws preserve the overview/Lambda/TF-Lite labels, arrows, clothing
icons, and the AWS Lambda plot while excluding presenter, face, camera,
browser/editor chrome, cursor, play/selection/recording UI, gauge overlays,
page counters, and black borders.

## One deterministic/native exact code artifact

`03-tensorflow-lite-02-03-predictions-to-tflite-crisp.jpg` is rendered from
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
| `09-explore-more-01-serverless-models-imagegen.jpg` | unchanged; 1672x941; C2PA `jumdc2pa`; clean serverless-models visual |
| `updates-01-runtime-compatibility-imagegen.jpg` | unchanged; 1672x941; C2PA `jumdc2pa`; clean runtime-compatibility visual |

## Audit fields for the valid serverless set

These fields were added for the independent review only. No serverless image,
SVG, source JPG, or crop bytes were changed; every output below is byte-equal
to its `db44278` version. Dimensions and byte counts are native values.

| Active output | Source SHA-256; dimensions; bytes | Crop SHA-256; dimensions; bytes | Output SHA-256; dimensions; bytes | Output equality / C2PA |
|---|---|---|---|---|
| `01-intro-01-clothes-classification-use-case-imagegen.jpg` | `34b622cac0f9520c8eb630c501c44a14edd400850d48b1c056ce15322be908f5`; `592x360`; `20567` | `dc558752d1cd58aa899b59ce13321010de5ac931773df584f0704d4842519d4c`; `478x315`; `20187` | `9d749daf6e02f2222bbf7f60fc33d5f00998cfec192000cf8c58090298588ea6`; `1545x1018`; `1002669` | `db44278 cmp=PASS`; `urn:c2pa:3ea44b41-3436-44b8-ba49-c3bc1397df9e` |
| `01-intro-02-aws-lambda-deployment-imagegen.jpg` | `a89283d03a6b4cba0554d9caa018ff9e7d69a8ff529684824cec011252e337b9`; `592x360`; `31174` | `de217321c715cb5f2004e93c18c1b81bf949901264690a3418e94411726f0cd9`; `478x315`; `31442` | `d488a9bfb50460b2db7cd3c5bf1c8db2bb16efa7b0ac427368b4c6de28abea04`; `1545x1018`; `1212209` | `db44278 cmp=PASS`; `urn:c2pa:b0d3fb74-9272-4c3f-90fc-d2a99e2d2adf` |
| `01-intro-03-lambda-uses-tf-lite-imagegen.jpg` | `5bfc43a94f14b84d96dc788a34c5bd55b91c33b319b5d5ccb5ece5fe79a51d3b`; `592x360`; `31744` | `c7e7e15c64a47675234a6f4982e503db301b09c57e627b32a6a6e52329cc8e95`; `478x315`; `31464` | `aed109bba163f9e830a396eafabf1b88ad3f4c0981a13a561c5b7cd7ad0d1129`; `1609x977`; `1185783` | `db44278 cmp=PASS`; `urn:c2pa:42d523e6-98eb-48a6-a879-ba499e333a41` |
| `02-aws-lambda-07-serverless-vs-serverful-imagegen.jpg` | `9cbda461b2f5cc65a235dfb2f5d3936246283e85fe323d443a43214a84e227b7`; `592x360`; `20552` | `7fa2ae28b15dbbcb962778dab1a34ac4523deb35860e7fc3c19a419399b51119`; `478x315`; `19009` | `24557d2f3ce691c5a40b06116fdc0b24e5517d219397775566208e266a6b9336`; `1545x1018`; `1007975` | `db44278 cmp=PASS`; `urn:c2pa:4bd2abc9-965c-4fbf-9f41-cea3c358de0e` |
| `03-tensorflow-lite-02-03-predictions-to-tflite-crisp.jpg` | `2026-09-09-tflite-artifact.svg` — `d03f2eff843c494794334942760af739bffbd0b16188851272c5e2a4bfa80cf3`; `1600x900`; `2718` | `03-tensorflow-lite-02-keras-predictions-native-crop.jpg` — `306e9b1e734c51cfcc3aa5f9b68777860c3956c7641401f7ac61479effb10da6`; `500x330`; `30945`; plus `03-tensorflow-lite-03-convert-to-tflite-native-crop.jpg` — `5d799a529764c873968bee13a4ef486844462efefa085ce2e8610d6df651c2dc`; `500x330`; `51264` | `acb643242c215248d29d2d0b93e9be1ef3cf74cfd2f40e94ea815b5cafe087ae`; `1600x900`; `168517` | `db44278 cmp=PASS`; deterministic SVG render, no C2PA expected |
| `09-explore-more-01-serverless-models-imagegen.jpg` | N/A — direct prompt-native asset; no source JPG | N/A — no source crop | `12b6ca0ba8116d7a8cfd80bd28f5bc3c7b0447b8fffb9c9323f847ff11503330`; `1672x941`; `1259401` | `db44278 cmp=PASS`; `urn:c2pa:63662376-7839-4bb0-95b4-694ac95c7fad` |
| `updates-01-runtime-compatibility-imagegen.jpg` | N/A — direct prompt-native asset; no source JPG | N/A — no source crop | `0fdb45038902fc3380381267d46e42c740e2f25ba59f4e1907fcec91330468d0`; `1672x941`; `1350532` | `db44278 cmp=PASS`; `urn:c2pa:b19776f8-2263-4d32-8c7a-08a514484d37` |
