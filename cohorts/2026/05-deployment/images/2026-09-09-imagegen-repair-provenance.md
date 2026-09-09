# Imagegen repair provenance — deployment

## `05-pipenv-02-version-conflict-imagegen.png`

- Lesson reference: `cohorts/2026/05-deployment/05-pipenv.md:21`
- Repair reason: the previous redraw contained an unlabeled yellow mark and omitted the source annotation `INSTALLS THE LATEST`.
- Original source JPG: `05-pipenv-02-version-conflict.jpg`
- Source dimensions: `598x360`
- Source SHA-256: `6f579e3ac4154e9aeb56536e6b29f001b3be442fafd7bbd66270902ce195910c`
- Retained bounded crop: `05-pipenv-02-version-conflict-imagegen-crop.jpg`
- Crop coordinates: `555x300+23+0` (`x=23`, `y=0`, `width=555`, `height=300`)
- Crop SHA-256: `e5f10b6ee2f18f6857129841a068b4be888c63dad18966f89ff944536e3bb231`
- Imagegen output: `05-pipenv-02-version-conflict-imagegen.png`
- Output dimensions: `1706x922`
- Output SHA-256: `64e6751a8bd29772b7209767927ba47b98c899ea7ab9433312d974544a11fce3`
- C2PA metadata: present; URN `urn:c2pa:8cfcb601-1235-4936-bfed-e98bb58fbe30`
- Generation method: built-in imagegen with the original JPG and the retained bounded crop supplied as references. This is a redraw, not an upscale or sharpened crop.
- Resize-only comparison: normalized RMSE `0.349921` against the bounded crop resized to `1706x922`, confirming that the output is materially regenerated rather than a resize-only copy.

### Preserved invariants

- The shared system-Python dependency conflict remains explicit: `CHURN SERVICE` uses `scikit-learn == 0.24.2`, while `LEAD SCORING SERVICE` uses `scikit-learn == 1.0`.
- The shared installation path and package flow remain visible: `$PATH`, `~/anaconda3/bin/pip`, `python`, `pypi.org`, and `.wheel`.
- The source annotation `INSTALLS THE LATEST` is restored verbatim.
- The title `5.5 ENVIRONMENT & DEPENDENCY MANAGEMENT` is retained.

### Removed artifacts

- Presenter face/camera inset
- Screen-recording cursor and controls
- Black frame borders and lower-right gauge
- Unexplained yellow scribble/mark

### Verification

- Native output inspected at `1706x922`.
- Lesson-width render inspected at `608x329`.
- Required labels and version values were checked in both views.
- No face, camera inset, browser/recording chrome, cursor, watermark, or unlabeled yellow mark remains.

## Remaining strict-audit provenance queue — 2026-09-09

The strict audit classified the eight non-repair deployment references below
as `PROVENANCE-BLOCKED`. Seven had original non-crisp JPG sources and were
regenerated with built-in imagegen using the original JPG plus the matching
bounded native crop. The remaining `09-explore-more` infographic was already
a direct imagegen illustration with C2PA metadata and no underlying JPG; it is
retained byte-for-byte and documented separately.

The reproducible crop script is
[`2026-09-09-remaining-provenance-crops.sh`](2026-09-09-remaining-provenance-crops.sh),
with SHA-256
`1641fb5702a321e5c74f73a2e44a5aec2d32f43ec5affbc1a731edc63df1b2a9`.
It uses only native ImageMagick `-crop WIDTHxHEIGHT+X+Y`; it does not resize,
Lanczos, sharpen, or otherwise enhance the source. The previous published
PNGs were not supplied as imagegen references. Native outputs and temporary
simulated 608px lesson-width renders were inspected; the temporary renders
are not published.

### Source-backed redraws

`Crop` is `(x, y, width, height)` in source-JPG pixels. `RMSE` is the
normalized ImageMagick comparison against a temporary resized crop and is
included only to show that the published output is not a resize-only copy.

| Published PNG | Lesson reference | Source JPG | Crop JPG | Crop | Source SHA-256 | Crop SHA-256 | Previous PNG SHA-256 | Current PNG SHA-256 | Native | 608px | Imagegen execution | C2PA | RMSE |
|---|---|---|---|---|---|---|---|---|---:|---:|---|---|---:|
| `01-intro-02-model-deployment-diagram-imagegen.png` | `01-intro.md:29` | `01-intro-02-model-deployment-diagram.jpg` | `01-intro-02-model-deployment-diagram-imagegen-crop.jpg` | `(20, 10, 430, 330)` | `1f0815984949b48a85c7f2c390c2981ad2f3e6ce480aeed532e6521449ae96c6` | `ccfe5763c47680ed6b9d02208bce5bb1eaa8cd850ce74b7c0e8439ff1a010818` | `c945dbc1cc07bf12deda18ef518c359c0b989058b3bf9db477fb8ffbbe2946ea` | `112018141d685aa9eb4df4e53757e832ec9c99491f65f5fdc59f8c55d72cec15` | `1536x1024` | `608x405` | `exec-fa955f65-56dc-449a-828a-feaa09f7b9e2` | `urn:c2pa:42dee4d3-5718-4ecc-9830-6d4da71a82a7` | `0.253346` |
| `01-intro-05-environments-imagegen.png` | `01-intro.md:53` | `01-intro-05-environments.jpg` | `01-intro-05-environments-imagegen-crop.jpg` | `(20, 10, 430, 330)` | `647357fe288431f542cbf342b3374493191247faaa8f63ad36a8ca256cb18ac7` | `6331d35940beb53cf06ebec91f0e34ebf7444ab1c331e920fe6ab10071057fce` | `01692c845b397f009694dda20c79149125f4e1a8cdac584550135452f2fb8fbf` | `a763c89e085440a8b72bb8ab97b517a3c1ff79328e726b7c02a68129352b3973` | `1536x1024` | `608x405` | `exec-eb0499e7-b1a3-445f-ad79-74f5b128ba59` | `urn:c2pa:74b99fc6-31fc-40f1-bfed-a17776c5d8d7` | `0.270182` |
| `03-flask-intro-02-request-response-imagegen.png` | `03-flask-intro.md:19` | `03-flask-intro-02-request-response.jpg` | `03-flask-intro-02-request-response-imagegen-crop.jpg` | `(25, 10, 450, 330)` | `8e5dff072baf56ad3846c929aaa692a124037a51efc84949d1910899cfb24fd4` | `082e79da8431669c813335d2aafd3ab520ebc5712e8b61bb5d38104a0e03a55c` | `6d4825726690f2b9c7f328e3341208c0f1170db2298033a2663bfc859108bc` | `8030ba17e3b8c534ef78ff4a7096a1821f38ac1605e3f933150e60bd0cb8dc29` | `1617x973` | `608x366` | `exec-d6ecd660-1ae1-4ae4-8be6-d35f6ded627c` | `urn:c2pa:386272e9-719f-414d-ab3f-9d28dcb234d4` | `0.208263` |
| `05-pipenv-03-isolated-environments-imagegen.png` | `05-pipenv.md:27` | `05-pipenv-03-isolated-environments.jpg` | `05-pipenv-03-isolated-environments-imagegen-crop.jpg` | `(8, 5, 475, 335)` | `2e409d6d3d8694253d616be362e05c146faf101c718a05d0e51206f5dd3b0d3c` | `8b519dab1932d8a3bc8dccc43ebe76baa7df34a76fd02bab1b88cd020c4af079` | `2fb501d045b462980c9ae79c267c4a3dcc7e7fc96cfd1950df1d67f8c29e1cf4` | `7a4022a90b3fb40511ef9f4f933c90f2498e1aefec0b88bf21f5c05668978e4f` | `1536x1024` | `608x405` | `exec-cdba492d-a64f-474d-8d23-e5f571fe31d9` | `urn:c2pa:95356c54-44fa-42ab-97ee-4f0968b7e2da` | `0.318491` |
| `06-docker-02-containers-on-host-imagegen.png` | `06-docker.md:49` | `06-docker-02-containers-on-host.jpg` | `06-docker-02-containers-on-host-imagegen-crop.jpg` | `(15, 5, 455, 335)` | `5a9d8eb7f6fe20da378cf8e0a4fd97ba6962f8c4928876a6eeef302921d647cf` | `92f6830c9343dec60cac3fdfddc2ac081cce7818727bf90335efbe6979b18a3e` | `284950d40d34c85640b52b0cd29c33f9c8758b44e89c1485eda099b6a365484f` | `efdb8e1a66b2c5d712d808f978fda00957c3ae8fb0af809785b0bead3c918ce1` | `1616x973` | `608x366` | `exec-07574b49-88b3-4e7b-8a32-0731467c4c6c` | `urn:c2pa:1691bed8-65ff-4ddd-b88e-4a3ee1b3acda` | `0.310580` |
| `06-docker-05-port-mapping-imagegen.png` | `06-docker.md:127` | `06-docker-05-port-mapping.jpg` | `06-docker-05-port-mapping-imagegen-crop.jpg` | `(25, 10, 430, 320)` | `13ef781550bfb1acb83ca149d00eadcb975084358b41aa4bec11fa887e1c6bf2` | `a637247b1bd030658c04c5457ddcd70ff2174a22c60d47501fded355e51fa493` | `bda48ba4b5fa19861ae6285da3ef00e8a51bd766ac736a4feb99aa61fda94282` | `305c67a4c2a6ca7196d6fb460aeb1fb70a6f6bf7f0cc9226cfad057324c9bd8d` | `1617x973` | `608x366` | `exec-43160290-6473-4bb8-b0a8-1a145653cd35` | `urn:c2pa:747ed203-092a-46c7-85a8-f1405aa628fd` | `0.288315` |
| `07-aws-eb-02-eb-architecture-imagegen.png` | `07-aws-eb.md:29` | `07-aws-eb-02-eb-architecture.jpg` | `07-aws-eb-02-eb-architecture-imagegen-crop.jpg` | `(25, 0, 430, 340)` | `472f8939e324ca9a52aa3161605458e5738c0e4f60b1a2ab979022512453e008` | `54d8a0560cf758406f1721a63635a160cdd9f4f932d8a0141516d8440b1a8918` | `6869b17e15363be29a3e0b972c54c869f30cebc951363f37fd6ab49cce20d99e` | `ef01c5f7c52d80453c6238a758dbb00683785907287ea24b0485900a72188e87` | `1617x973` | `608x366` | `exec-23878f94-6994-4840-b31b-5c8625983e8a` | `urn:c2pa:f643cc35-c541-49cf-a7d8-622ffd49d457` | `0.251506` |

### Preserved invariants and removed artifacts

- The model-deployment diagram keeps the notebook → `model.bin` → churn
  service flow and the marketing-service arrows.
- The environment diagram keeps the nested Flask, Pipenv, and Docker layers
  and the exact phrases `ENVIRONMENT FOR PYTHON DEPS` and
  `ENVIRONMENT — SYSTEM DEPENDENCIES`.
- The Flask illustration keeps the request/response arrows and the exact
  `ml+zoomcamp` / `q = web service` annotations.
- The Pipenv illustration keeps both exact executable paths and `NO CONFLICTS`.
- The Docker illustrations keep the exact OS versions, service names, ports,
  `9696:9696`, `host : container`, and the full `docker run -it -p 9696:9696
  churn-prediction:latest` command.
- The AWS illustration keeps `190`, `100`, `100`, both `S3` boxes, the Docker
  churn service, and the marketing-service request/response paths.
- Webcam tiles, color-wheel controls, black capture bars, browser/editor
  chrome, cursors, play controls, and selection overlays were removed from all
  seven redraws.

### Retained direct imagegen output

| Published PNG | Lesson reference | Current PNG SHA-256 | Native | 608px | C2PA | Decision |
|---|---|---|---:|---:|---|---|
| `09-explore-more-01-deployment-choices-imagegen.png` | `09-explore-more.md:6` | `b3c35230788a9dc861b6f96d65bf127fc98b4e988e553f7e02d75b8742b29b75` | `1672x941` | `608x342` | `urn:c2pa:04369cae-5b1e-467a-b459-fb9099728d8d` | Retained byte-for-byte. This is a brand-new conceptual infographic with no original non-crisp JPG in the module. Its embedded C2PA record proves direct imagegen; native/608px inspection found no face, camera tile, browser/editor chrome, cursor, play control, or selection overlay. |

No source/crop pair is fabricated for this direct imagegen asset. The existing
semantic-repair asset `05-pipenv-02-version-conflict-imagegen.png` is also
unchanged; its separate provenance and semantic-repair record above remains
authoritative.
