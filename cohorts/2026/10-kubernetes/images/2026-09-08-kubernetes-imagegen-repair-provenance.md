# Kubernetes visual repair provenance — 2026-09-08

This ledger records the strict follow-up to the Herschel audit of the 49
active image references in `cohorts/2026/10-kubernetes`. Earlier crispness
claims are withdrawn. The independently accepted 11 assets were left byte-for-byte
unchanged.

## Native cleanup

Commit `c613aa7` removed the 33 `REMOVE-NATIVE` image references from the
lesson Markdown. The corresponding source binaries remain in `images/` for
historical/source inspection. The remaining two unresolved references were
inspected separately below.

## Imagegen repair batch

Each repair used the original non-crisp JPG and a bounded crop as reference
inputs. The generated result was inspected at native size and after a 608px
render. No output was accepted if it was only resized/sharpened, retained a
camera/overlay artifact, or changed the lesson semantics.

| Target | Original JPG SHA-256 | Bounded crop SHA-256 | Final generated SHA-256 | Final size | Method and result |
| --- | --- | --- | --- | --- | --- |
| `05-kubernetes-intro-04-external-internal-ingress-imagegen.png` | `0d5d1e3a27003f9740ec8e63d8d4bcc9f63ffcb9eaed056e208ed7d5a35d4108` | `6ee2ce50f46a72a8424a405794ddc004216f83172ea1731a9155bc61892f71b9` | `12c8a76d875e2b030150319b86c49411257c64943740ec92d219d565bbf8681d` | 1614×975 | Imagegen redraw, followed by a structural correction to enforce exactly two deployment boundaries; camera, overlay, and rough whiteboard artifacts removed. |
| `05-kubernetes-intro-05-definitions-imagegen.png` | `95e50001a296373cd57506d21b7a3a1cd4adb3d0f2ed41de59d0fc0d75ba76ab` | `e1924137355016b9bb893d2bba83c251a4c3d8de4af24f77de14981517f3d2c5` | `dc400b6824b8120d705edcae7ae9079a4b2d4350b0a8037daf7262603ae50b0e` | 1536×1024 | Imagegen typeset redraw; exact definitions preserved and stray `H`, camera, overlay, and handwriting removed. |
| `05-kubernetes-intro-06-scaling-imagegen.png` | `3ea3155a7773393f96812103e49c2e55295bcd25f1ec8d022970a5d633cc031e` | `622b030f08fe70cec29a2e191477dc9b4360c9b91760298982401ac65ce8c0fa` | `944eec0b71fc6e078c55e8ff2baf2fb8693f1bdf6d0bf1890841d2ba57514f32` | 1536×1024 | Imagegen redraw, followed by a structural correction; multiple users and scaled gateway pods are shown, with exactly two deployment boundaries and no camera/overlay artifacts. |

The final PNGs carry C2PA metadata identifying the built-in image-generation
service. The scaling crop was created only to bound the board content before
generation; it is not used as a lesson reference.

## Unresolved-reference inspection

### `02-tensorflow-serving-03-docker-run-crisp.png`

The original, bounded crop, and current target are a terminal/code capture
with handwritten annotations. The lesson already includes the complete
`docker run` command and explains the model name/version mapping in prose.
This is native command content rather than a useful conceptual visual, so its
Markdown image reference should be removed while preserving the JPG, crop,
and existing PNG source binaries.

### `08-eks-06-aws-console-crisp.png`

The original, bounded crop, and current target show the EC2 Instances page,
but the source includes browser/camera capture artifacts and the current PNG
is an enlarged screenshot rather than a verified redraw. It is a factual UI
evidence screenshot, not a diagram that can safely be regenerated without
inventing AWS interface text. It remains unresolved pending either a
faithful source-backed redraw or an explicit decision to remove the image;
no new imagegen asset was substituted.

