# Deep-learning visual provenance repair — 2026-09-09

This ledger records the 28 provenance-blocked active refs in module 08 from
the strict visual audit (44 active image refs in this module; 56 across
modules 08–09). Before this repair, module 08 was `44 = 28 blocked + 16
accepted`; module 09 was `12 = 7 blocked + 5 accepted`; combined, `56 = 35
blocked + 21 accepted`. The 21 already accepted refs were left byte-for-byte
unchanged; their current evidence remains in
`2026-09-08-imagegen-repair-provenance.md` and the deterministic repair ledger
already tracked there. After the two independent-review repairs below, the
arithmetic is module 08 `44 = 0 blocked + 44 accepted`, module 09
`12 = 0 blocked + 12 accepted`, combined `56 = 0 blocked + 56 accepted`;
all 35 formerly blocked active refs are now accepted.

## Method

All source-backed imagegen repairs use this chain:

```text
original 592x360 JPG -> bounded native crop JPG -> imagegen PNG
```

The crop geometry and command are reproducible in
`2026-09-09-provenance-crops.sh`. It uses ImageMagick `-crop` and `+repage`
only: no resize, Lanczos, sharpen, or screenshot-derived PNG is supplied to
imagegen. Each imagegen call supplied both the original JPG and its crop; the
previous active PNG was never an input. The resulting PNGs carry the imagegen
C2PA marker (`jumdc2pa`). Native and simulated 608px renders were inspected
after generation.

## The 21 regenerated imagegen refs

Each row is `active output <- original JPG + native crop; imagegen execution`.
The crop geometry is in the reproducible script; the output names remain
stable so lesson Markdown did not need to change.

| Active output | Source chain | Execution |
|---|---|---|
| `01-fashion-classification-01-tabular-vs-images-imagegen.jpg` | `01-fashion-classification-01-tabular-vs-images.jpg` + `...-imagegen-crop.jpg` | `exec-dfab046b-e4a5-434c-9636-bb8ff0bd6196` |
| `01-fashion-classification-02-upload-service-imagegen.jpg` | `01-fashion-classification-02-upload-service.jpg` + `...-imagegen-crop.jpg` | `exec-3378fa41-6f76-4c80-a8fa-f60059c309a7` |
| `02-tensorflow-keras-01-keras-inside-tensorflow-imagegen.jpg` | matching JPG + crop | `exec-7d79e140-ddfd-43f6-84ba-20977b0b8b30` |
| `02-tensorflow-keras-05-image-sizes-imagegen.jpg` | matching JPG + crop; labels rechecked as `299x299` and `224x224` | `exec-d89c08c3-ba9c-40d2-a717-36f7ec2a35bc` |
| `02-tensorflow-keras-07-rgb-channels-imagegen.jpg` | matching JPG + crop | `exec-26b63940-050f-4473-87e2-9399d2912725` |
| `04-conv-neural-nets-01-cnn-overview-imagegen.jpg` | matching JPG + crop | `exec-66c6aa54-9239-46c0-a0c7-e95bfab05f3d` |
| `04-conv-neural-nets-02-feature-map-imagegen.jpg` | matching JPG + crop | `exec-98496d10-ff47-485d-9b02-872a867eda61` |
| `04-conv-neural-nets-03-one-feature-map-per-filter-imagegen.jpg` | matching JPG + crop | `exec-0239fd23-b66f-4679-b51f-0b8e5a9fbb62` |
| `04-conv-neural-nets-04-chained-conv-layers-imagegen.jpg` | matching JPG + crop | `exec-c9f5e8dc-82e9-436a-8a47-3afd236f5a3f` |
| `04-conv-neural-nets-05-vector-representation-imagegen.jpg` | matching JPG + crop | `exec-b27eaf56-559f-431b-a9de-c9e462946b43` |
| `04-conv-neural-nets-07-dense-layer-imagegen.jpg` | matching JPG + crop | `exec-c92f3370-621e-47d3-9eb8-8f2a2303d664` |
| `04-conv-neural-nets-08-summary-imagegen.jpg` | matching JPG + crop | `exec-18d7fb07-902c-47c7-a5e2-2091610e9de0` |
| `05-transfer-learning-01-transfer-learning-idea-imagegen.jpg` | matching JPG + crop | `exec-58c66dea-4151-4e54-b2fb-0a5b745a211a` |
| `06-learning-rate-01-book-analogy-imagegen.jpg` | matching JPG + crop; `VAL POORLY` retained | `exec-a01e930d-db32-4a57-a754-3a64121d48e4` |
| `07-checkpointing-02-callbacks-imagegen.jpg` | matching JPG + crop | `exec-8c0d41ec-a64e-4613-8a2e-a5d4e7902b48` |
| `08-more-layers-01-inner-layer-diagram-imagegen.jpg` | matching JPG + crop | `exec-566f64e5-cea8-4445-9890-f0877191232a` |
| `09-dropout-01-motivation-logo-imagegen.jpg` | matching JPG + crop | `exec-bb829227-5af0-436d-a388-fe6374c873b9` |
| `09-dropout-02-hiding-input-imagegen.jpg` | matching JPG + crop | `exec-48f8014b-0934-4273-a4cf-dd5c36998258` |
| `09-dropout-04-v3-diagram-imagegen.jpg` | matching JPG + crop | `exec-8f2c3f6a-2167-4c14-8074-7a9f895b6ff7` |
| `10-augmentation-01-generate-more-images-imagegen.jpg` | matching JPG + crop | `exec-450e15b9-26d7-4eed-b3de-204c68fa0589` |
| `13-summary-01-use-case-diagram-imagegen.jpg` | matching JPG + crop | `exec-46486b3a-6508-4cea-9f0d-9d7a4047e88b` |

The redraw prompts explicitly preserved labels, metrics, model shapes, arrows,
and code/diagram meaning while excluding the presenter, face, camera,
browser/editor chrome, cursor, play/selection/recording UI, page counters,
and black borders.

## Three deterministic/native replacements

These are exact plots or screenshot artifacts, so imagegen was not used for
the published replacement:

| Active output | Native evidence and operation |
|---|---|
| `07-checkpointing-04-save-best-only-imagegen.jpg` | Direct native crop of `07-checkpointing-04-save-best-only.jpg`, `438x305+22+0`; exact `VAL ACCURACY`, `75%`/`80%`, curve, save annotations, ticks, and `EPOCH` retained. |
| `10-augmentation-02-flip-rotation-shift-grids-imagegen.jpg` | Native source regions `410x88+35+15`, `410x92+35+145`, `410x82+35+278`, appended without scaling; notebook controls excluded. |
| `12-using-model-03-load-img-pants-imagegen.jpg` | Direct native image crop `290x220+105+125`; only the exact pants result is retained, without notebook chrome. |

The three native PNG replacements are produced directly from source crops in
the crop script; the `*-native-crop.jpg` files are durable human-auditable
crop evidence. No resize or sharpening is involved. The two independent-review
targets below are deliberately excluded from this deterministic set: their
active PNGs are true imagegen outputs.

## Independent-review imagegen replacements (2)

These two active refs correct the independent review of `db44278`. Each call
supplied the original non-crisp JPG and the durable native crop only; the old
active PNG was not an input. The crop script now reproduces crop evidence only
and cannot overwrite either imagegen output.

| Active output | Source JPG — SHA-256; dimensions; bytes | Native crop — SHA-256; dimensions; bytes | Imagegen output — SHA-256; dimensions; bytes | Execution / C2PA | Byte equality / checks |
|---|---|---|---|---|---|
| `10-augmentation-03-zoom-grid-imagegen.jpg` | `10-augmentation-03-zoom-grid.jpg` — `f1496e64afc5fd5c32506fa5af40d3fd1c00c2cb65ef145e86b5dd2ac543dbb9`; `592x360`; `35309` | `10-augmentation-03-zoom-grid-native-crop.jpg` — `c30f7e941be939c01259446cf8f3199f7e01b6923aadfee2a4b4584cb0494d7e`; `410x156`; `25738`; native regions `410x78+35+100` and `410x78+35+225`, cleaned and appended without scaling | `d0845dd9053a32c99750a5524101826b0afb72c6ac4c77b9b5847c831c32f711`; `2033x773`; `1255310` | `exec-054f571f-d9dc-4871-9f96-ea318631b60d`; `urn:c2pa:03909910-8e89-491f-a082-222261f30420` | Active bytes equal the imagegen cache (`cmp=PASS`) and differ from the pre-repair target (`cmp=PASS`). Native and 608px overlay/semantic checks pass; blue/black selection-arrow residue absent; crop reproducibility passes; no resize/sharpen-only path. |
| `10-augmentation-06-val-stuck-077-imagegen.jpg` | `10-augmentation-06-val-stuck-077.jpg` — `1c63184adada36d3ccd9758d420c7dec25bf9f589245959aecad377365f9f100`; `592x360`; `24873` | `10-augmentation-06-val-stuck-077-native-crop.jpg` — `51e1d55e930fb537907478b0cb018fd92cc65d503a375272286c096d6045fca1`; `300x185`; `9195`; native crop `300x185+90+100` without scaling | `4c31b5b7958e60e3fe1c29d7726df69d762eab9714957580e9d2968526aebb24`; `1597x985`; `848383` | `exec-916545d5-e907-414b-a4e2-488cc0217961`; `urn:c2pa:86b5b33c-dbec-4fa3-b24c-fcc1d0485bf1` | Active bytes equal the imagegen cache (`cmp=PASS`) and differ from the pre-repair target (`cmp=PASS`). Native and 608px overlay/semantic checks pass; `val`/`train`, axes, ticks, and the 0.70–0.77 validation behavior retained; cursor absent; crop reproducibility passes; no resize/sharpen-only path. |

## Two current direct-imagegen refs left unchanged

These two blocked refs have no same-stem source JPG in the module. They are
already clean prompt-native imagegen assets with current C2PA evidence, were
inspected natively and at simulated 608px, and were therefore not regenerated
from invented source material:

| Active output | Evidence |
|---|---|
| `14-explore-more-01-learning-paths-imagegen.jpg` | unchanged; 1672x941; C2PA `jumdc2pa`; clean educational learning-path visual |
| `install-01-gpu-stack-imagegen.jpg` | unchanged; 1672x941; C2PA `jumdc2pa`; clean educational GPU-stack visual |
