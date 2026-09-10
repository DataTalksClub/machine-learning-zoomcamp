# Serverless workshop visual audit

Audit target: `cohorts/2026/09-serverless/workshop/README.md`  
Source video: [sHQaeVm5hT8](https://www.youtube.com/watch?v=sHQaeVm5hT8)  
Audit date: 2026-09-09

## Decision

The source video was acquired through the documented DataImpulse route and
validated with `ffprobe`. Two clean conceptual illustrations are published:

1. a customer event invoking an AWS Lambda function and receiving a prediction
   response;
2. the framework-to-ONNX-to-ONNX Runtime interoperability relationship.

The raw screenshots are not published. They contain transient AWS/browser/
editor state, exact code or values, presenter/Zoom overlays, or a misleading
web search panel. Exact code, commands, URLs, JSON, tables, and numeric output
remain native README content.

## Source and workflow provenance

- Source file: `/home/alexey/git/.tmp/ml-workshop-videos/sHQaeVm5hT8.mp4`
- Source SHA-256:
  `06fb0c38bede2f7e98aae97c1e5095be7ade0cfb7f2745eb0d1acedcf027786e`
- Source properties: `640x360`, H.264/AAC, `5528.903401` seconds,
  `184016612` bytes
- Transcript: `/home/alexey/.cache/youtube_transcripts/sHQaeVm5hT8.txt`
  (SHA-256 `26c7964e50743faae5ad39803a1f55cfac4054253e726bdd53d427b88ed51f06`)
- Scratch audit: `/home/alexey/git/.tmp/workshop-processing/ml-2026-serverless-kubernetes/serverless/AUDIT.md`
- Independent review:
  `/home/alexey/git/.tmp/workshop-processing/ml-2026-serverless-kubernetes/INDEPENDENT-REVIEW.md`

The Lambda source frame is `s02-lambda-prediction.png` at `00:17:07`, with
SHA-256
`21e86b4709fc57b3073f614737df3b297eaa95a6f7f3ce793fb319e860d07cfc`.
The focused crop uses `(x=0, y=70, width=640, height=245)` and has SHA-256
`ac572b7c5151270c3d47c07774044be1cdd7862313dea8232b1fa6debce43afb`.
The original frame and crop were both supplied to imagegen. The generated
asset has SHA-256
`85ecab48466ebca2ba1a2e395a223864aaaae4d91fe203457c4529e689b90884` and is
`images/aws-lambda-invocation-prediction-imagegen.jpg`.

The ONNX source frame is `s09-onnx-framework-diagram.png` at `00:52:15`, with
SHA-256
`b865b3d7d80bf314bb94ea5cd2ff3840a0760afff6796e9ffbdeaeafd90126fe`.
The focused crop uses `(x=350, y=100, width=270, height=190)` and has SHA-256
`fce33e375c4b9710da95e21a38b14ac9d6c5bcc5f3c9a2202479a14558e6cb1c`.
The original frame and crop were supplied to imagegen as source context, but
the published diagram is explicitly a prompt-native conceptual illustration,
not a literal redraw of the crop: the crop is a Google results page and ONNX
knowledge panel, not a framework-flow diagram. The generated asset has
SHA-256
`ff97513fcfbc8a569eceb31ce6b430e3bb052775a84542c14ea25c93ca381a28` and is
`images/onnx-framework-interoperability-imagegen.jpg`.

Generation guardrails for both assets: remove presenter/webcam, Zoom/browser/
editor chrome, cursor, account/workspace identifiers, exact code, URLs,
numbers, and transient UI; use only durable concepts supported by the workshop
README and the reviewed source context. The imagegen outputs carry their own
C2PA generation assertions; the output hashes above are the repository-file
checksums.

## Candidate register

The six-part rubric scores contribution, relevance, readability,
complementarity, durability, and accessibility from 0 to 2 each. A raw frame
must pass the source and cleanliness gates before it can seed a regeneration.

| ID | Timestamp | Visible source state | Raw decision | Published treatment |
| --- | --- | --- | --- | --- |
| S01 | `00:14:53` | Lambda starter code/test-event chooser | Reject: exact transient UI/code | None |
| S02 | `00:17:07` | Lambda editor and JSON prediction response; raw `4/12` | Reject as screenshot: exact code/values and overlay | Keep conceptual flow; `aws-lambda-invocation-prediction-imagegen.jpg` passes independent review |
| S03–S08 | `00:25:14`–`00:47:58` | Dockerfile, ECR commands, Lambda console, cold/warm invocation states | Reject: exact code/commands/values or transient UI | Native README/code only |
| S09 | `00:52:15` | Google results page and ONNX knowledge panel; preliminary crop candidate | Reject crop: small/misdescribed web panel | Keep only a separate prompt-native ONNX concept, with provenance correction recorded above |
| S10–S15 | `00:59:04`–`01:26:55` | Conversion code/logs, image input, exact prediction values and tables | Reject: native exact material and overlays | Native README/code only |
| S16 | `01:28:44` | GitHub `keras_image_helper` code view with presenter/Zoom overlay | Reject: code screenshot; earlier audit label corrected | Native README/code only |

## Review gate

Independent review result:

- Lambda conceptual diagram: **PASS**. It is crisp at lesson width, source/
  README-supported, and contains no face, webcam, Zoom, browser, or editor
  overlay.
- ONNX conceptual diagram: **PASS after provenance correction**. Its visual
  content is supported by the README's Keras/PyTorch → ONNX → ONNX Runtime
  flow, but it must not be described as a literal redraw of S09.
- S09 raw crop: **FAIL** and not published.
- Kubernetes workshop: no image; the independent reviewer confirmed that
  native YAML, commands, JSON, and status tables are the correct treatment.

The rejected source frames remain in ignored scratch storage for traceability;
none is a final lesson asset.
