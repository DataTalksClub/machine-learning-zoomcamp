# Course repository webhook

The `course-repository-webhook.yml` workflow notifies the course platform after
every push to `main`. Configure these repository secrets in GitHub Actions:

- `COURSE_REPOSITORY_WEBHOOK_URL`: the complete website webhook endpoint URL
  (ending in `/api/webhooks/github`).
- `COURSE_REPOSITORY_WEBHOOK_SECRET`: the same shared signing secret configured
  by the website.

The workflow signs the exact GitHub event payload with `X-Hub-Signature-256`,
sets `X-GitHub-Event: push` and a unique `X-GitHub-Delivery`, and retries failed
requests. Keep both values in repository secrets; do not put them in the source
tree or workflow logs.
