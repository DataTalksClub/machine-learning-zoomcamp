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

## Batch 2: AWS Lambda walkthrough

All five references below were removed from `02-aws-lambda.md`. The
lesson already preserves the Lambda service promise, function name,
runtime, architecture, deployed `PONG` behavior, printed event, pants
prediction response, and the API Gateway trigger example in native
prose and code.

| Reference | Source JPG SHA-256 | Bounded crop SHA-256 | Existing PNG SHA-256 | Disposition |
| --- | --- | --- | --- | --- |
| `02-aws-lambda-01-search-lambda-crisp.png` | `b05e2924bc92490eb20e9aebb61d513eed541a3c2a4fdd330ac138cb788bfc7d` | `4ab0fba26c4ce4b42ce5d1b0d44e56bb1d1b3e3a89432006566ee209ed4bdd72` | `86c65e458317da8e04616f3b493e67e1dd74e85ecfe00d0aa0bedfb00c5557d2` | Remove: exact AWS search UI; service promise is native prose |
| `02-aws-lambda-02-create-function-crisp.png` | `7d4a6c3b80d921719665f022434311e929b8757d744d391d355cf7d9c5877e58` | `7f13bb06237b6b4f590408796de9e326b843b34060ff340fdeec201826f907e3` | `00be660245930f05ab8e62cad24ef89853ab33ad3e6867420230eb59000456a8` | Remove: exact form UI; name, runtime, and architecture are native prose |
| `02-aws-lambda-04-test-pong-response-crisp.png` | `d2291c249b53df8719ac6c635dea101d6ff0d067c5eac6aa9b22bc027acc4735` | `f9d54f44aceaded08fbb642f2b6e85960d41a5b249eb0ba1fbfd1f68d1f290a0` | `bd247661b605cd8887c3dc80374225f6496c31448bd9d1d4886d6f07aac8b6cb` | Remove: exact test-console UI; `PONG` and event logging are native prose/code |
| `02-aws-lambda-05-pants-response-crisp.png` | `f0c906ed44329d99b7ddd9ce7113e835b40a733e33cf0d666aaa5a4a0d743fe0` | `b7dedabfba5acbc82bd19afa83405030fe720b142363f0fb700ce2ec0740919e` | `3d13a23ce712d1a71fd14442d374c78c82af991fc0c9aa5f73f851dfe5962248` | Remove: exact test-console UI; response is now a native JSON block |
| `02-aws-lambda-08-invite-link-function-crisp.png` | `541e02cd68547799fc4ff86d1b97a3670ed634970edb079a1e17413b34936796` | `f15dd32b8d93d0deb2ab84d9071aeede866f29c9ca2f7be01ede8bb69e28c442` | `8fde69edfc1fa83d7824db595d2c3ba15275ea9e546ab8d50cad36278495a7b6` | Remove: exact account UI; redirect and API Gateway trigger are native prose |
