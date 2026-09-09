# FastAPI workshop visual audit - 2026-09-09

## Outcome

I audited only the [FastAPI and uv workshop](README.md) plus its source video,
[jzGzw98Eikk](https://www.youtube.com/watch?v=jzGzw98Eikk). I couldn't acquire a
source video file or source frame through the documented local-video, yt-dlp,
Piped, or Invidious routes. Therefore no candidate has verifiable frame
provenance, no candidate clears the source-backed illustration rubric, and no
image or README image reference was added.

Transcript timestamps below are navigation anchors only. They don't establish
what's visible in a frame or provide frame provenance.

## Source and temporary materials

These are the source references and temporary paths used for the audit:

- Source URL: `https://www.youtube.com/watch?v=jzGzw98Eikk`
- Video ID: `jzGzw98Eikk`
- Cached transcript: `~/.cache/youtube_transcripts/jzGzw98Eikk.txt`
- Cached transcript SHA-256: `ad491d4780a9aff8b47a1e3038ebc5834324e9ed0b801c2e0942f7884b007610`
- Intended ignored source directory: `cohorts/2026/.tmp/ml-fastapi-workshop/videos/`
- Intended ignored candidate directories: `cohorts/2026/.tmp/ml-fastapi-workshop/illustrations/candidates/` and `cohorts/2026/.tmp/ml-fastapi-workshop/illustrations/crops/`
- Acquired source video: none
- Extracted candidate frames: none

The temporary mirror responses and failed acquisition logs remain only under
`cohorts/2026/.tmp/ml-fastapi-workshop/` and aren't part of this commit. No
thumbnail, transcript, or mirror metadata was promoted to a lesson asset.

I ran the documented acquisition checks as follows:

- YouTube rejected direct `yt-dlp` with the documented JavaScript runtime/client
  options and returned "Sign in to confirm that you're not a bot".
- The documented sticky proxy route returned HTTP 407
  (`Proxy Authentication Required`).
- Piped metadata endpoints returned the same upstream sign-in failure for the
  target video, or were unavailable with 502/403 responses.
- Invidious instances didn't return usable video API metadata for the target.
- A local search found no matching video file.

## Candidate audit

I kept the smallest set of useful teaching moments from the cached transcript.
We use a source-gate score: `0/12` means the candidate
isn't publishable because its source frame can't be verified. This score isn't
a claim about the visual quality of an unseen frame. Crop coordinates are
`N/A` for every candidate.

Candidate 1: service boundary

- Timestamp: `00:36:16–00:36:42`
- Workshop section: FastAPI
- Score: `0/12` - source gate
- Crop coordinates `(x, y, width, height)`: `N/A`
- Teaching point: A marketing client sends a request to the prediction service
  and receives a response.
- Decision: Reject. There's no source frame, so this is a transcript-only
  anchor.

Candidate 2: interactive API docs

- Timestamp: `00:42:03–00:42:42`
- Workshop section: FastAPI
- Score: `0/12` - source gate
- Crop coordinates `(x, y, width, height)`: `N/A`
- Teaching point: FastAPI's `/docs` page exposes the endpoint and lets the
  learner try a request.
- Decision: Reject. There's no source frame, so the exact UI can't be claimed.

Candidate 3: client request and prediction response

- Timestamp: `00:51:20–00:53:19`
- Workshop section: FastAPI
- Score: `0/12` - source gate
- Crop coordinates `(x, y, width, height)`: `N/A`
- Teaching point: A client sends JSON to `/predict`, receives a churn decision,
  and acts on it.
- Decision: Reject. There's no source frame, and the teaching point overlaps
  the service-boundary explanation.

Candidate 4: invalid input

- Timestamp: `00:55:09–00:56:01`
- Workshop section: Pydantic and Validation
- Score: `0/12` - source gate
- Crop coordinates `(x, y, width, height)`: `N/A`
- Teaching point: Invalid input should be rejected instead of silently
  producing a prediction.
- Decision: Reject. There's no source frame. The exact errors and values belong
  in native text.

Candidate 5: remote deployment state

- Timestamp: `01:32:06–01:34:23`
- Workshop section: Deployment
- Score: `0/12` - source gate
- Crop coordinates `(x, y, width, height)`: `N/A`
- Teaching point: Fly.io changes the local service into a reachable deployment,
  and the client calls its remote `/predict` endpoint.
- Decision: Reject. There's no source frame, and deployment URL/state is
  ephemeral.

Other workshop moments use exact code, commands, configuration, or values
already in the README. The rubric requires us to keep those explanations in
native markup instead of screenshots. I retained only these five candidates.
Each one could have shown a service relationship, interactive API state,
validation behavior, or deployment state. A verifiable source frame would have
been required.

## Publication decision

We publish the following decision:

- We accepted no assets.
- We added no README references, so we leave the workshop image-free.
- We made no native markup changes.
- We didn't run imagegen because a conceptual redraw requires an original source
  frame and its native crop, and neither exists here.
- We stop at the source gate rather than infer a frame from the transcript or
  thumbnails.
