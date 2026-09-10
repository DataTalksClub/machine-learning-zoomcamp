# FastAPI workshop visual audit - 2026-09-09

## Outcome

I audited the [FastAPI and uv workshop](README.md) and its source video,
[jzGzw98Eikk](https://www.youtube.com/watch?v=jzGzw98Eikk). The source was
acquired through the documented DataImpulse route, validated with `ffprobe`,
and reviewed frame by frame at the relevant teaching moments.

Two source-backed conceptual illustrations are publishable:

- a client-to-`/predict` request and prediction response;
- the durable deployment flow from a Docker image through Fly.io to a
  reachable application endpoint.

The generated illustrations deliberately do not reproduce exact code, URLs,
probability values, terminal output, or transient UI. Those details remain in
the native Markdown and code blocks. The original source video, source frames,
and crops remain in the ignored scratch directory for provenance and review;
they are not committed as lesson assets.

## Source and temporary materials

These are the source references and temporary paths used for the audit:

- Source URL: `https://www.youtube.com/watch?v=jzGzw98Eikk`
- Video ID: `jzGzw98Eikk`
- Cached transcript: `~/.cache/youtube_transcripts/jzGzw98Eikk.txt`
- Cached transcript SHA-256: `ad491d4780a9aff8b47a1e3038ebc5834324e9ed0b801c2e0942f7884b007610`
- Acquired source video: `/home/alexey/git/.tmp/ml-workshop-videos/jzGzw98Eikk.mp4`
- Source video SHA-256: `8c20deeb5c0552f9c28198643882c83a3c6d1d42077c6b9901c238124ffdfb2a`
- Source video properties: `640x360`, `30 fps`, `6083.674558` seconds,
  `178855244` bytes
- Candidate directory:
  `/home/alexey/git/.tmp/ml-workshop-frames/jzGzw98Eikk/`
- Final output directory: `images/`

The response candidate was extracted as `response.jpg` at `00:53:11` and
cropped to `response-crop.png` with `(x=45, y=15, width=540, height=300)`.
The original frame SHA-256 is
`f9a87c95c8cf31e81ab748a9d06a5cd090feddcdf5ae187e03573609edfb7c1c`; the
crop SHA-256 is
`4f9c7d0823c7514d4fbfeaaa47a8e5a2188dc36f4affb63b2b56cc4c90f467e2`.

The deployment candidate was extracted as `fly-deployed.jpg` at `01:33:22`
and cropped to `fly-deployed-crop.png` with
`(x=155, y=195, width=470, height=155)`. The original frame SHA-256 is
`1facd7c23eaa443b9938b3fecdd57214184ca208bb6de5c592fd8644f06dba68`; the
crop SHA-256 is
`e66d670e3aff47ba6af6a1ce0d0e69ab355f0bca7871fabdfb979ae3efb17f96`.

For each accepted illustration, the image-generation input included the
original non-crisp frame and the focused crop. The generated output hashes
are:

- `images/fastapi-request-response-imagegen.jpg`:
  `4892a2e5ce31e5e75b759c2eeb4f846e39a64ceec104fc181820c77d91449e0e`
- `images/docker-fly-deployment-flow-imagegen.jpg`:
  `ca20b6ae853e47d997a5f44a13d413a0029062f2c69231323d0970eced3ddf07`

The source acquisition check passed with DataImpulse: `yt-dlp` using the
Android client and 360p format completed a non-zero MP4, and `ffprobe`
confirmed the duration and dimensions. No thumbnail or transcript-only claim
was promoted to a lesson asset.

## Candidate audit

The rubric scores contribution, relevance, readability, complementarity,
durability, and caption/accessibility from 0 to 2 each, for a maximum of 12.
The source frame must first be verifiable. Exact code, commands, URLs, values,
tables, and transient UI stay in native Markdown or deterministic rendering;
imagegen is used only for a durable conceptual relationship.

### Candidate 1: service boundary

- Timestamp: `00:36:30`
- Source frame: `service-boundary.jpg`
- Score: `4/12`
- Decision: Reject. The frame mainly shows implementation code and does not
  add a readable service relationship beyond the nearby prose and code.

### Candidate 2: interactive API docs

- Timestamp: `00:42:20`
- Source frame: `api-docs.jpg`
- Score: `3/12`
- Decision: Reject. It is generic `/ping` Swagger UI; the exact UI is
  transient and the endpoint details are already represented by native text.

### Candidate 3: client request and prediction response

- Timestamp: `00:53:11`
- Source frame: `response.jpg`; focused crop: `response-crop.png`
- Score: `11/12`
- Decision: Keep. The frame visibly supports the teaching point that a client
  sends JSON to `/predict` and receives a churn prediction. Imagegen converted
  that source-backed relationship into a crisp, durable diagram without
  inventing the source's exact code or numeric output.
- Published asset: `images/fastapi-request-response-imagegen.jpg`
- README reference: immediately after the `curl /predict` example

### Candidate 4: invalid input

- Timestamp: `00:55:40`
- Source frame: `invalid-input.jpg`
- Score: `3/12`
- Decision: Reject. The captured frame does not clearly show the validation
  error; the exact error payload belongs in the existing native code/text.

### Candidate 5: remote deployment state

- Timestamp: `01:33:22`
- Source frame: `fly-deployed.jpg`; focused crop: `fly-deployed-crop.png`
- Score: `10/12`
- Decision: Keep. The frame supports the durable relationship between a
  containerized service, Fly.io, and a reachable deployment. Imagegen removed
  the ephemeral deployment URL and editor/Zoom overlays while preserving that
  relationship.
- Published asset: `images/docker-fly-deployment-flow-imagegen.jpg`
- README reference: immediately after the Fly.io deployment URL discussion

### Candidate 6: deployment response

- Timestamp: `01:36:51`
- Source frame: `deploy-response.jpg`
- Score: `4/12`
- Decision: Reject. It duplicates the deployment candidate and is dominated by
  transient terminal/URL output; the durable flow is already covered by the
  accepted deployment illustration.

## Publication decision

- Accepted exactly two source-backed assets.
- Added both references to `README.md`.
- Used the original non-crisp frame plus a focused crop as image-generation
  inputs for each accepted asset.
- Removed faces/camera and editor/Zoom overlays from the published visuals.
- Kept exact code, commands, URLs, numeric values, and validation payloads in
  native Markdown instead of asking imagegen to recreate them.
- Rejected generic, duplicate, transient, and non-diagnostic screenshots.
