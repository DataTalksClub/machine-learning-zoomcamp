# Kubernetes visual repair provenance — 2026-09-08

This ledger records the strict follow-up to the Herschel audit of the 49
active image references in `cohorts/2026/10-kubernetes`. Earlier crispness
claims are withdrawn. The independently accepted 11 assets were left byte-for-byte
unchanged.

## Native cleanup

Commit `c613aa7` removed the 33 `REMOVE-NATIVE` image references from the
lesson Markdown. After inspecting the unresolved references, commit
`d679ff8` also removed the duplicate Docker command screenshot. The
corresponding source binaries remain in `images/` for historical/source
inspection. One unresolved AWS console reference remains active.

## Imagegen repair batch

Each repair used the original non-crisp JPG and a bounded crop as reference
inputs. The generated result was inspected at native size and after a 608px
render. No output was accepted if it was only resized/sharpened, retained a
camera/overlay artifact, or changed the lesson semantics.

| Target | Original JPG SHA-256 | Bounded crop SHA-256 | Final SHA-256 | Final size | Method and result |
| --- | --- | --- | --- | --- | --- |
| `05-kubernetes-intro-04-external-internal-ingress-imagegen.png` | `0d5d1e3a27003f9740ec8e63d8d4bcc9f63ffcb9eaed056e208ed7d5a35d4108` | `6ee2ce50f46a72a8424a405794ddc004216f83172ea1731a9155bc61892f71b9` | `be6dd20c163ff4062225639e4ca60da9a83016293a5092aeef7c02abec85b93d` | 1614×975 | Follow-up imagegen redraw from the original JPG and bounded crop; native and 608px review confirmed the exact User → Ingress → external Gateway Service → Gateway pod → internal Model Service → TF-Serving pod flow, with no camera/overlay artifacts. |
| `05-kubernetes-intro-05-definitions-imagegen.png` | `95e50001a296373cd57506d21b7a3a1cd4adb3d0f2ed41de59d0fc0d75ba76ab` | `e1924137355016b9bb893d2bba83c251a4c3d8de4af24f77de14981517f3d2c5` | `49b317270d98e95052627e594d570106a4f108f486def43a63f2991ee162ae71` | 1800×1120 | Imagegen candidate from the original JPG and bounded crop was inspected, then replaced with the deterministic SVG render in `2026-09-08-kubernetes-definitions-render.svg` to guarantee exact `LoadBalancer`, `ClusterIP`, and `same image and configuration` text. Native and 608px renders were inspected. |
| `05-kubernetes-intro-06-scaling-imagegen.png` | `3ea3155a7773393f96812103e49c2e55295bcd25f1ec8d022970a5d633cc031e` | `622b030f08fe70cec29a2e191477dc9b4360c9b91760298982401ac65ce8c0fa` | `5b14fe6ab51034d6f71f76e911eaea2b4440636103c070590b16b0ff37876477` | 1619×971 | Follow-up imagegen redraw from the original JPG and bounded crop; native and 608px review confirmed the exact request chain and multiple TF-Serving replicas, with no camera/overlay artifacts. |

## Focused semantic repair batch — 2026-09-09

These five outputs supersede the prior published PNGs for the same targets.
Each was generated with the original non-crisp JPG **and** the retained
bounded crop as imagegen inputs. The final PNGs were inspected at native
resolution and at a simulated 608px lesson width. C2PA metadata was checked
in each published output; the URN is recorded below.

| Target | Original JPG SHA-256 | Bounded crop SHA-256 | Final SHA-256 | Final size | Method, semantic repair, and C2PA |
| --- | --- | --- | --- | --- | --- |
| `01-overview-05-cpu-gpu-imagegen.png` | `87dbe2e8a72ec1bc89615cd3407c5377f40071a22de35521dfbf7017773209a0` | `243e74a87c059ef534d842a0dc7ab34c2c0a7ba4343b6923a2147e809d39ee79` | `17d74fcdaf9626dea93745158b5aa09f4e9cac697e25e3da25d0db3ae7a5d79b` | 1611×976 | Imagegen redraw; corrected the gateway label to `5 CPU`, added explicit `DOWNLOADING IMAGES`, `RESIZING THEM`, and `PREPARING INPUT` processing, preserved post-processing and the request/response flow, and removed capture artifacts. C2PA `urn:c2pa:06a51f90-5d10-4874-93ec-19e491c9cc6c`. |
| `04-docker-compose-03-isolated-containers-imagegen.png` | `32dcfa3e6eb390610e06ceac339eab15213bf7ec4521d84b4972c4c56b8e70f2` | `d4c9ab950bac40a8d5d9b7ad5241f0adfcab7514bf5f001f9673b643032e1271` | `09d294b11b1ff4a4d2906cc6a7e9c6babac4c7045d50fd3b79f4e6f1d43d3e9b` | 1612×976 | Imagegen redraw; shows separate gateway and TF-Serving containers, both host-port mappings, and the failed `localhost:8500` path with `NO DIRECT CONNECTION`/`CONNECTION ERROR` before Compose. C2PA `urn:c2pa:37cacdb3-af8d-49a8-b9f3-3e92730acf10`. |
| `05-kubernetes-intro-03-services-crisp.png` | `893104fcec6a51dffc72cd1ad928e66d6d6805e57ff7cbe2440ddfd9e760c972` | `498241af3fcacb5692a72d576413023e774544692bab6f0fb2e43ec76c0445d7` | `a661f79f118b9a71a2806a3c93080a15750af521755e77e34a179808b2a97be2` | 1614×974 | Imagegen redraw; makes the complete `USER → GATEWAY SERVICE → GATEWAY POD → MODEL SERVICE → TF-SERVING POD` routing explicit and keeps the replica pods visible. C2PA `urn:c2pa:4e0fce40-ea97-44aa-92b2-905e700a693b`. |
| `05-kubernetes-intro-06-scaling-imagegen.png` | `3ea3155a7773393f96812103e49c2e55295bcd25f1ec8d022970a5d633cc031e` | `622b030f08fe70cec29a2e191477dc9b4360c9b91760298982401ac65ce8c0fa` | `cc58404b4e743e2febb9e60ff5493003d3be5c7e80b1e835ee6f33e8e96cd13b` | 1614×975 | **Superseded.** This redraw incorrectly showed four Gateway replicas and three TF-Serving replicas. The lesson source of truth requires five Gateway instances and two TF-Serving instances (see `01-overview.md:77-81`). |
| `09-summary-01-architecture-imagegen.png` | `24bff239d26d4b0f501a738ccf5b085497536f971838f83db2682abf75791196` | `e13f5c1ffb4482b01fa362e8a61f25e1fb94d51779f456629b03809aa08d844` | `cbe8248072a7f769c4a229e1afd47f6f3a82101cea35eb33b19dee6f3a17bfe6` | 1614×975 | Imagegen redraw; corrected the gateway to `5 CPU`, TF-Serving to `2 GPU`, and retained the four preprocessing/post-processing labels with no capture artifacts. C2PA `urn:c2pa:9073adb7-f9d5-40dc-a9f8-22536276a0c7`. |

## Corrected scaling topology — 2026-09-09

The previous scaling redraw is superseded because it used the wrong concrete
replica counts. The source-of-truth lesson text says: “five instances of the
gateway on CPU machines and two instances of TensorFlow Serving on GPU
machines” (`01-overview.md:77-81`). The replacement below was generated from
the original non-crisp JPG and the retained bounded crop, without using the
incorrect redraw as an input.

| Target | Original JPG SHA-256 | Bounded crop SHA-256 | Final SHA-256 | Final size | Method, semantic repair, and C2PA |
| --- | --- | --- | --- | --- | --- |
| `05-kubernetes-intro-06-scaling-imagegen.png` | `3ea3155a7773393f96812103e49c2e55295bcd25f1ec8d022970a5d633cc031e` | `622b030f08fe70cec29a2e191477dc9b4360c9b91760298982401ac65ce8c0fa` | `db14cf32b4adeb0d7d953bdef7a2bcd75c3106acc99d365b61f6cef3bc32abe4` | 1536×1024 | Imagegen redraw from the original JPG and retained crop. Corrected topology: exactly five Gateway PODs (2+2+1) and exactly two TF-Serving PODs. Preserved the single `INGRESS → GATEWAY SERVICE → GATEWAY → MODEL SERVICE → TF-SERVING` request path, scaling annotations, and deployment boundaries. Native and simulated 608px inspection confirmed legible labels, exact counts, and no face, camera, browser, cursor, playback, or other capture overlays. C2PA `urn:c2pa:42258215-ae89-48d2-ab4f-fcf9a9828a61`. |

Validation details for the replacement:

- Native render: `1536×1024`; simulated lesson render: `608×405`.
- Targeted OCR of each pod interior returned `POD` for all five Gateway
  pods and both TF-Serving pods at both native and simulated lesson sizes
  (`7/7` labels at each size).
- Visual and color-component checks independently counted five yellow
  Gateway boxes and two green TF-Serving boxes; no additional pod boxes were
  present.
- Native and 608px visual inspection confirmed the single request path and
  found no face, webcam, browser, cursor, playback, or selection overlays.

### Checkpoint status

All three requested assets are now checkpointed. The ingress and scaling
outputs are imagegen redraws from their original JPGs and bounded crops. The
definitions image uses the inspected imagegen candidate as the semantic/style
reference, followed by a deterministic SVG render because exact Kubernetes
term casing could not be trusted in generated text.

The ingress and scaling final PNGs carry C2PA metadata identifying the
built-in image-generation service. The definitions final PNG is the
deterministic render described above; its imagegen candidate carries the C2PA
metadata. The scaling crop was created only to bound the board content before
generation; it is not used as a lesson reference.

## Unresolved-reference inspection

### `02-tensorflow-serving-03-docker-run-crisp.png`

The original, bounded crop, and current target are a terminal/code capture
with handwritten annotations. The lesson already includes the complete
`docker run` command and explains the model name/version mapping in prose.
This is native command content rather than a useful conceptual visual, so its
Markdown image reference was removed in `d679ff8` while preserving the JPG,
crop, and existing PNG source binaries.

### Removed `08-eks-06-aws-console-crisp.png` reference

The Markdown embed was removed from `08-eks.md` because this is a factual AWS
console evidence screenshot, not a conceptual diagram. The source contains
browser/camera capture artifacts, and the current PNG is an enlarged screenshot
rather than a verified redraw. Regenerating it with imagegen would require
inventing AWS interface text and therefore would not be faithful to the lesson.
The surrounding lesson explanation remains and still describes the EKS node,
EC2 instances, and load balancer.

The source and preserved output files were not deleted. Their exact hashes at
removal time are:

| File | SHA-256 |
| --- | --- |
| `08-eks-06-aws-console.jpg` (original source) | `852acf5139771b097cd11bbf47336c7f63dc6dafbb07e3b6bed7844de64e469a` |
| `08-eks-06-aws-console-cropped.png` (bounded crop) | `958342ba36a6a42f43f23f1396dbed55bca0356c7835e77d6d4db0976a514320` |
| `08-eks-06-aws-console-crisp.png` (preserved prior output) | `d1837f297698b2ce324edac008cd6c93662127a2da5075644043e3e8cbff4011` |

No replacement image was generated. This is an intentional removal of the
Markdown reference only; the original, crop, and prior PNG remain available
for historical/source inspection.

## Remaining strict-audit provenance queue — 2026-09-09

The strict audit classified seven visually usable active references as
`PROVENANCE-BLOCKED`. Six were screenshot-derived diagrams whose prior
imagegen outputs had no durable native bounded crop recorded in this module.
They were regenerated with built-in imagegen using only the original
non-crisp JPG and the matching native crop below. The seventh reference is a
direct conceptual imagegen illustration with no underlying JPG; its C2PA
record and native/608px evidence were already valid, so it remains
byte-for-byte unchanged.

The checked-in crop script is
[`2026-09-09-kubernetes-remaining-provenance-crops.sh`](2026-09-09-kubernetes-remaining-provenance-crops.sh),
with SHA-256
`b6f069162da08cc39c633ecfbd6ef673178dc53102250711691ca98597c3c4d5`.
It uses only ImageMagick `-crop 475x360+23+0` and `+repage` on the original
JPGs. It performs no resize, Lanczos pass, sharpening, or other enhancement.
The previous published PNGs were not supplied as imagegen references.

`RMSE` is the normalized ImageMagick comparison against a temporary crop
resized to the published output dimensions. That resize exists only for the
comparison and is not a generation step. Native outputs and temporary
simulated 608px lesson-width renders were inspected; the temporary renders
are not published.

### Source-backed redraws

`Crop` is `(x, y, width, height)` in source-JPG pixels. The accepted imagegen
execution is the final generation after any rejected punctuation/count
candidate; no prior PNG was used as an input.

| Published PNG | Lesson reference | Source JPG | Crop JPG | Crop | Source SHA-256 | Crop SHA-256 | Previous PNG SHA-256 | Current PNG SHA-256 | Native | 608px | Imagegen execution | C2PA | RMSE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `01-overview-01-tf-serving-inference-imagegen.png` | `01-overview.md:32` | `01-overview-01-tf-serving-inference.jpg` | `01-overview-01-tf-serving-inference-imagegen-crop.jpg` | `(23, 0, 475, 360)` | `52bc165a6f5ff7ebdeb6b500305c99539fe377ddcee267e82b04b08b82d391df` | `8fa51cd9dcf205e4ef2186d9646be430f1d509a77b20db08497079593a5a5eb8` | `e8b58f08b7f062601d87af6f1adbf57f25134a8089fd12eddb8fbfc26ffc0a3a` | `c4f0273103c931235407144edb01a3481bcc82d442fb6232fb2b6d53e57347e1` | `1611x976` | `608x368` | `exec-a4b98d91-1f8c-4a73-baf9-69b20cdca23a` | `urn:c2pa:5e5f9f3f-9fd0-4967-b0a8-c3a691570ae6` | `0.171616` |
| `01-overview-02-architecture-imagegen.png` | `01-overview.md:50` | `01-overview-02-architecture.jpg` | `01-overview-02-architecture-imagegen-crop.jpg` | `(23, 0, 475, 360)` | `19d43fa5991cb5b015fcca856c52944d43d3689a157f5632b450ebba661bc393` | `009f947ca9ab47a95426ba9e8135e61b077e7edc194c3bb45065f5a6423cf352` | `db231786c8faf838b8631512af7ded392cfe8f5775b6037ee554c5aecc086ae6` | `c1e7944c16fb528af49a04409525662cb051cb9f02c5f7feb34e04532c380da9` | `1734x907` | `608x318` | `exec-89dbd4bd-8327-4e15-8ae0-62dbd6d4fed5` | `urn:c2pa:89dc36ce-aecb-4e9a-9e3e-921852e146cd` | `0.240921` |
| `01-overview-03-grpc-imagegen.png` | `01-overview.md:56` | `01-overview-03-grpc.jpg` | `01-overview-03-grpc-imagegen-crop.jpg` | `(23, 0, 475, 360)` | `3a4263e5b798ad0c9e88d59fb01abcafb5449a926ff612899129ecfdb6321d69` | `2745d42c733a5c5c570205d56684843ac340b1242b5de0e8712ebded6900f0db` | `2e244f01603f884a6dc50836f1b8e3cda64bd9ac0c6e119b836a5f1a53e3b534` | `53fc0a2a9a0e219d785fd14a0beba4ae3f063c343644240f349fbe491dad3403` | `1615x974` | `608x367` | `exec-c5de28b5-4395-43ea-be54-9d04d01811b2` | `urn:c2pa:c217274b-d43c-427d-830b-149ef81684f5` | `0.234913` |
| `01-overview-04-kubernetes-imagegen.png` | `01-overview.md:84` | `01-overview-04-kubernetes.jpg` | `01-overview-04-kubernetes-imagegen-crop.jpg` | `(23, 0, 475, 360)` | `fadcba2ea3d41aacd0431409188cd9b2f4718defb26bce993a025391533ef530` | `58bf950ba1c69ac6879057b75606032d79bae2e51632bfc6aaba461f74968288` | `208697c52d7abd8a9c8b9539ae1f3ad7f7c089c3302ef0b2a272b49d4715a80d` | `055379857302dcb924a38375ee3b6d3ffc01f06d5a04025df1ebc4a18bf89977` | `1615x974` | `608x367` | `exec-69a5b988-9d5a-4335-b0bc-a14b0c2d8393` | `urn:c2pa:8b04e4f2-2879-4964-b41c-6fd7cc1a5fd6` | `0.264473` |
| `05-kubernetes-intro-01-cluster-nodes-pods-imagegen.png` | `05-kubernetes-intro.md:34` | `05-kubernetes-intro-01-cluster-nodes-pods.jpg` | `05-kubernetes-intro-01-cluster-nodes-pods-imagegen-crop.jpg` | `(23, 0, 475, 360)` | `58cd777b900a3be4f7ace1c831c2f41146dd129aca8d150ff928c8c76cc094e3` | `8536ec5a7d912af194c03cda3fc122e4bc816e97d20514aa20f5e0b5410f339f` | `aeaee13aaefad5df9948aa283853073aef825fb8a7e71c2bd717a367d34c7137` | `1c99dd9488aa5a83a928e0c3127d42747e82872989e2970ffe984ae2b0b29f98` | `1441x1092` | `608x461` | `exec-81033f07-303e-4000-a08b-2f509f748f82` | `urn:c2pa:9468c0c9-4322-47ef-a436-5b9ac3b45129` | `0.215700` |
| `05-kubernetes-intro-02-deployments-imagegen.png` | `05-kubernetes-intro.md:48` | `05-kubernetes-intro-02-deployments.jpg` | `05-kubernetes-intro-02-deployments-imagegen-crop.jpg` | `(23, 0, 475, 360)` | `dee2c002ba15a9987a92b4302fb0917e11e97f830b1e28cbfbace31672c0f52f` | `52d7e6a2f90856c4a07c6a8e458e800dc6b86cd3eb02450c171f658bec048435` | `53f3a9271ded0fe0fb8de5d5f6f4500fb47ce8d0f45e0d5624a94431cb045c08` | `3c226f2d03d6ee30fe372a1317120cb647495b298f0d193b33ef9adee8931ff7` | `1441x1092` | `608x461` | `exec-94ab12dc-7733-4e30-b211-4c2e8f94a87b` | `urn:c2pa:ce868a1f-3926-43c1-892b-eb664fe2a70b` | `0.313808` |

### Preserved invariants and removed artifacts

- The inference diagram keeps the one input arrow, `X`, `INFERENCE`,
  `TF-SERVING`, `C++`, and `CLOTHING MODEL`.
- The architecture and gRPC diagrams keep the exact website → gateway →
  TF-Serving routing, both return arrows, `URL`, `X`, `gRPC`, `10 NUMBERS`,
  and the visible response notation `"pants": 9.88,...`.
- The Kubernetes-boundary diagram keeps the website outside one Kubernetes
  boundary, the gateway/Flask and TF-Serving/C++ boxes inside it, and the
  request/response arrows and labels.
- The nodes/pods diagram contains exactly two nodes and four pod boxes.
- The deployments diagram contains exactly two nodes, two deployment
  boundaries, and exactly four pods: two Gateway pods and two TF-Serving pods,
  with both `SAME IMAGE & CONFIG` arrow relationships.
- Faces, webcam/camera tiles, black capture bars, browser/editor/recorder
  chrome, cursors, play controls, page indicators, selection overlays, and
  watermarks were removed from all six redraws.

### Retained direct imagegen output

| Published PNG | Lesson reference | Current PNG SHA-256 | Native | 608px | C2PA | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| `10-explore-more-01-cluster-options-imagegen.png` | `10-explore-more.md:4` | `216afd9b895871b913de353aa95858b8d0eef87bad4f14916da2a7179a7054f1` | `1672x941` | `608x342` | `urn:c2pa:dfb0341e-c583-42dd-9340-a15611ab0e60` | Retained byte-for-byte. This is a brand-new conceptual local/managed-cloud Kubernetes infographic with no original non-crisp JPG. Its C2PA record proves direct imagegen; native/608px inspection found no face, camera tile, browser/editor chrome, cursor, play control, selection overlay, or watermark. |

No source/crop pair was fabricated for this direct imagegen asset.

### Verification checkpoint

- All seven audited active references resolve from the lesson Markdown.
- All six source-backed outputs carry C2PA metadata and have a durable
  original JPG → native crop → imagegen output chain.
- All six source-backed output/crop comparisons are materially different
  from a resized crop (`RMSE` `0.171616`–`0.313808`), so no resize-only,
  Lanczos-only, or sharpen-only output was accepted.
- Native and simulated 608px visual inspection confirmed legible labels,
  routing/arrows, exact pod counts, and no capture overlays. The temporary
  608px renders are not committed.
