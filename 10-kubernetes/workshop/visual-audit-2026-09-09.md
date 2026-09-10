# Kubernetes workshop visual audit

Date: 2026-09-09

Scope: `cohorts/2026/10-kubernetes/workshop/README.md` and source video
`c_CzCsCnWoU` only.

## Outcome

No visual asset cleared the publish gate. The workshop README remains unchanged
and still has zero instructional image references. No image was added because
the recording could not be acquired or decoded, so no source frame could be
visually inspected, cropped, or validated.

This is a conservative audit result, not a claim that the recording contains
no useful teaching visuals. The transcript identifies useful moments, but a
transcript cannot establish frame readability, exact UI state, or crop bounds.

## Source and acquisition provenance

- Source URL: `https://www.youtube.com/live/c_CzCsCnWoU?si=fgQ56JwunM3NoiWm`
- Cached transcript: `/home/alexey/.cache/youtube_transcripts/c_CzCsCnWoU.txt`
  (648 timestamped cues; read-only input).
- Disposable workspace: `cohorts/2026/.tmp/kubernetes-workshop-audit/`,
  covered by the repository's local `.git/info/exclude` rule for
  `cohorts/2026/.tmp/`.
- The documented sticky-session `yt-dlp` route was attempted. It returned
  `407 Proxy Authentication Required` from the configured proxy.
- The documented Piped/Invidious mirror route was attempted against the
  available instance lists. Responses were shutdown, bot-check, `403`, `404`,
  `500`, `502`, or empty; no valid media URL was obtained.
- A local Chromium/Playwright check reached the YouTube page but the player
  remained at “Sign in to confirm you’re not a bot”; the video element had no
  media source, `readyState=0`, and `duration=NaN`.
- The title thumbnail was inspected and excluded: it is branding/presenter
  art, not a workshop teaching surface.
- No `.mp4` was obtained, so `ffmpeg` extraction was not run. There are no
  candidate frames, native crops, generated outputs, or output hashes to
  publish. Imagegen was not invoked because its required original frame plus
  native crop were unavailable.

## Candidate ledger

Scores are in rubric order `instructional contribution / relevance /
readability and focus / complementarity / durability / caption and
accessibility`, followed by the total. Because no frame was available,
readability and caption/accessibility are scored `0`; the crop field is
explicitly `N/A` rather than inferred.

| Candidate | Timestamp | Workshop section | Teaching point | Crop coordinates | Score | Decision |
| --- | --- | --- | --- | --- | ---: | --- |
| C01 | `33:40–34:06` | Testing Locally | FastAPI `/docs` shows the example request and a clothing prediction, with pants scoring highest. | `N/A — source frame unavailable` | `2/2/0/1/1/0 = 6/12` | Reject; exact UI/output would need a deterministic crop and visual review. |
| C02 | `43:08–43:34` | Docker Containerization | The Dockerized service answers `/health` and still returns a prediction. | `N/A — source frame unavailable` | `2/2/0/2/1/0 = 7/12` | Reject; exact terminal/UI evidence could be useful, but cannot be made readable or verified. |
| C03 | `47:58–49:47` | Kubernetes Deployment — Understanding Kubernetes Resources | Replicated Pods sit behind a Service/load balancer, while HPA decides how many replicas are needed. | `N/A — source frame unavailable` | `2/2/0/2/1/0 = 7/12` | Reject; conceptual-diagram candidate, but imagegen requires the original frame and native crop. |
| C04 | `50:34–55:42` | Create Deployment Manifest | The Deployment starts with two replicas and binds the image, resources, liveness probe, and readiness probe. | `N/A — source frame unavailable` | `2/2/0/1/1/0 = 6/12` | Reject; exact YAML is already available natively in `k8s/deployment.yaml`, so a screenshot would hit the rubric hard gate. |
| C05 | `59:17–1:00:22` | Kubernetes Deployment | `kubectl get pods`/`get deployments` demonstrates two Pods and two available replicas. | `N/A — source frame unavailable` | `2/2/0/2/1/0 = 7/12` | Reject; exact terminal output needs a deterministic source crop that could not be made. |
| C06 | `1:04:42–1:07:58` | Testing the Deployed Service | Port-forwarding lets a host request reach the Service, which routes it to one of the Pods. | `N/A — source frame unavailable` | `2/2/0/2/1/0 = 7/12` | Reject; useful state transition, but no source pixels were available for validation. |
| C07 | `1:13:48–1:15:08` | Testing Autoscaling | Under load, HPA increases the deployment to four replicas; the test reaches 20 requests/second with all requests successful. | `N/A — source frame unavailable` | `2/2/0/2/1/0 = 7/12` | Reject; strongest candidate in principle, but its exact values and UI cannot be published without the source frame. |

## Publish decision

The minimal accepted set is empty for this pass. Do not add an image reference
until the recording or an equivalent local source is available and the
candidate frames can be inspected at lesson size. If access is restored, C03
is the only conceptual-diagram candidate eligible for imagegen; C02, C05, C06,
and C07 must use deterministic/native treatment, while C04 should remain native
YAML rather than become a screenshot.
