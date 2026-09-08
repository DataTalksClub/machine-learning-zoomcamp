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
