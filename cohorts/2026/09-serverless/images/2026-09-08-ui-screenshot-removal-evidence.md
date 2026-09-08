# Serverless UI screenshot removal evidence

This record covers the remaining AWS-console screenshots after
`bc153ae`. The source JPGs and bounded crops were inspected together
with the current `*-crisp.png` files. The current PNGs are enlarged
versions of the bounded crops, not imagegen redraws: the crop dimensions
are exactly one third of the PNG dimensions for every target in this
batch.

The decision rule is strict: retain a visual only when it adds useful
instructional information that cannot be represented clearly in native
Markdown, and only regenerate it when imagegen can preserve every
visible fact and label. Exact AWS console screens contain dense UI text,
controls, and version-specific layout. Imagegen cannot be trusted to
reproduce those details faithfully, so these references are removed and
their instructional facts remain in the lesson prose and code blocks.

## Batch 1: creating the Lambda function

All four references below were removed from `06-creating-lambda.md`.
The lesson already preserves the container-image choice, image digest,
`x86_64` architecture, timeout error, `1024 MB` memory, `30` second
timeout, warm invocation timing, and `270 MB` maximum memory natively.

| Reference | Source JPG SHA-256 | Bounded crop SHA-256 | Existing PNG SHA-256 | Disposition |
| --- | --- | --- | --- | --- |
| `06-creating-lambda-03-create-function-crisp.png` | `750fc72373e39fbef9759b62cb525f3c07138118439267976c05d9608f4a0c84` | `169aafd044a9d0afd3256ac472021d15cf423623fdc96126f47e16ba15c95243` | `40de78332726026d30b7df1d1a7140f7244bc1fe7286c5853f1ab1eb4b126014` | Remove: exact console UI; no faithful imagegen redraw |
| `06-creating-lambda-04-timeout-error-crisp.png` | `b6cbeb111b43551ac8913d35f3851f1f9434207d8df2016efadc8c165a7b0399` | `917a14c9a36e34edebd8abf077d81364570fdf905f7ebbe048f98f20970975bf` | `83f7d1cab61324ec69a78a2e458d51d755c29ee6d0d105dbcc18bc099f06f955` | Remove: exact console UI; timeout is already native text |
| `06-creating-lambda-05-configure-timeout-memory-crisp.png` | `cfabca229dad38d9a6b553f3819fc4ccaca2ba25ef72dd92fa17ccc41d3ce66e` | `e0957f65c9ff60c172df10ec1cbb9c9af7161e7afdec708e47178c9fac3e8ee8` | `9f1bee6d951ea1ddd87edcf46803052994caaa2b094e6c7893816245cfa040c4` | Remove: exact console UI; settings are already native prose |
| `06-creating-lambda-06-test-success-crisp.png` | `42c58849fd7d2b96930396c525116482c8bb50dd2c535ef6293e79cac7079c4f` | `e9d7708d971bfcb42fb058d68b8db6aed675e1edea50c2990a331b82a106f80f` | `470a8ec40635cf9f67b9e9adf6edd55335e1124e567137e615909fdc8121401d` | Remove: exact console UI; warm-run facts are native prose |
