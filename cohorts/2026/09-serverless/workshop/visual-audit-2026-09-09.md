# Serverless workshop visual audit

Audit target: `cohorts/2026/09-serverless/workshop/README.md`  
Source video: [sHQaeVm5hT8](https://www.youtube.com/watch?v=sHQaeVm5hT8)  
Audit date: 2026-09-09

## Decision

No image was accepted and no image reference was added to the workshop README.
The transcript contains useful teaching moments, but the source video could not
be downloaded or mirrored in this environment. Without a source frame, there is
no defensible crop, readability check, or source-backed visual score. The
accepted set is therefore empty.

For the candidate table below, `0/12 (hard-gated)` is an audit score, not a
claim that the underlying video scene has no instructional value: an absent
source frame cannot pass the rubric's crop, readability, caption, or provenance
gates. Crop coordinates are recorded as `N/A` rather than guessed.

## Source and workflow provenance

- Transcript: `/home/alexey/.cache/youtube_transcripts/sHQaeVm5hT8.txt`
  (SHA-256 `26c7964e50743faae5ad39803a1f55cfac4054253e726bdd53d427b88ed51f06`).
- Scratch root: `.tmp/ml-serverless-audit/` (gitignored through the local
  repository exclude). The source-video destination was
  `.tmp/ml-serverless-audit/videos/sHQaeVm5hT8.mp4`; no video was written.
- Route A, the documented `yt-dlp` + Oxylabs workflow, failed with HTTP `407`
  (`Tunnel connection failed: Proxy Authentication Required`).
- Route B, the documented Piped/Invidious workflow, was probed against the
  documented and current public instances. Responses were `LOGIN_REQUIRED`,
  `403`, Cloudflare challenge, gateway errors, or unavailable hosts; no valid
  stream metadata or downloadable media was obtained.
- A direct `yt-dlp` run, YouTube Innertube client variants, and available local
  video search were also checked. They produced no usable local source.
- YouTube title/auto-thumbnail files were retained only in scratch for source
  checking. They show a title card, presenter/browser chrome, repository
  navigation, or AWS chrome; they are not candidate teaching assets and have no
  reliable video timestamps.
- No imagegen regeneration was run. The only conceptual candidate (the ONNX
  framework relationship) had no original frame and native crop to provide to
  imagegen. Exact UI, code, commands, values, and outputs remain native README
  material rather than generated pixels.

## Candidate register

The timestamps are transcript-backed ranges. A candidate is a teaching moment
that would have been frame-extracted and scored if the source video had been
available. Every candidate is rejected at the source-frame hard gate; none was
published.

| ID | Timestamp | Workshop section | Score | Crop coordinates | Teaching point | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| S01 | 00:10:09–00:11:20 | Scikit-Learn Models | 0/12 (hard-gated) | N/A — no source frame | Training produces `model.bin`, the model artifact later packaged for Lambda. | Reject: exact artifact/file state is already stated in the README; no frame to verify. |
| S02 | 00:15:01–00:15:09 | AWS Lambda | 0/12 (hard-gated) | N/A — no source frame | A first Lambda test succeeds and returns a response. | Reject: exact test response is already native JSON in the README; no frame to verify. |
| S03 | 00:17:05–00:17:29 | AWS Lambda | 0/12 (hard-gated) | N/A — no source frame | The simple handler returns `0.56` and `churn: true` before the real model is installed. | Reject: exact values are already native JSON/code; no frame to verify. |
| S04 | 00:21:19–00:25:08 | AWS Lambda with Docker: Running Locally | 0/12 (hard-gated) | N/A — no source frame | Docker packages the Lambda handler, model, and dependencies; `CMD` identifies the handler entry point. | Hold only as a possible conceptual visual; no original frame/crop for a faithful regeneration. |
| S05 | 00:26:57–00:30:45 | AWS Lambda with Docker: Running Locally | 0/12 (hard-gated) | N/A — no source frame | The first local invocation exposes the virtual-environment dependency mistake and the system-install fix. | Reject: exact error and commands belong in native code/terminal text; no frame to verify. |
| S06 | 00:31:07–00:31:35 | AWS Lambda with Docker: Running Locally | 0/12 (hard-gated) | N/A — no source frame | The model works inside the local Docker container after dependencies are installed correctly. | Reject pending a clean, readable result frame; no frame to verify. |
| S07 | 00:32:49–00:40:58 | AWS Lambda: Deployment | 0/12 (hard-gated) | N/A — no source frame | The image moves from a local Docker tag through ECR authentication and push. | Reject: commands and registry values are exact material already represented natively; no frame to verify. |
| S08 | 00:46:25–00:48:12 | AWS Lambda: Deployment | 0/12 (hard-gated) | N/A — no source frame | A container-backed Lambda has a slower cold start, then faster warm invocations because the image/model remains loaded. | Hold as the strongest state-change candidate; no frame to verify readability or caption match. |
| S09 | 00:52:00–00:52:42 | AWS Lambda: TensorFlow Models | 0/12 (hard-gated) | N/A — no source frame | Keras, PyTorch, and other frameworks converge on ONNX, which ONNX Runtime serves. | Reject: conceptual diagram would require the original frame plus native crop for imagegen; neither is available. |
| S10 | 00:54:06–01:00:22 | AWS Lambda: TensorFlow Models | 0/12 (hard-gated) | N/A — no source frame | Keras model → SavedModel → ONNX conversion, isolated in Docker to control dependencies. | Reject: process can be expressed natively and no original frame is available for a faithful visual. |
| S11 | 01:01:17–01:08:29 | AWS Lambda: TensorFlow Models | 0/12 (hard-gated) | N/A — no source frame | ONNX Runtime receives a preprocessed clothing image and produces ten class scores, with pants highest. | Hold as a possible result visual; no frame to verify the image, scores, or legibility. |
| S12 | 01:19:19–01:20:04 | AWS Lambda: PyTorch Models | 0/12 (hard-gated) | N/A — no source frame | PyTorch exports directly to ONNX and can reuse the ONNX serving path. | Reject: relationship is concise native prose/code and no source frame is available. |
| S13 | 01:26:55–01:27:08 | AWS Lambda: PyTorch Models | 0/12 (hard-gated) | N/A — no source frame | After the input-size fix, the PyTorch-backed classifier again predicts pants with the highest score. | Hold as a possible result visual; no frame to verify the output. |

## Review gate

Implementer pass: transcript-only candidate register completed; no candidate
was promoted without a local source frame, native crop coordinates, and a
normal-size readability check.

Independent adversarial review: **REJECT / NO ASSET**. The proposed set would
either duplicate exact README material, rely on an unverified screenshot, or
require inventing pixels and crop coordinates. Publishing nothing is the only
rubric-compliant outcome until a valid local video or mirror is available.

