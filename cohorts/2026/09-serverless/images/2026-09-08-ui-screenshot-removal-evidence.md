# Serverless UI screenshot removal evidence

This record covers the AWS-console screenshot decisions after
`bc153ae`. The source JPGs and bounded crops were inspected together
with the current `*-crisp.png` files. Batches 1 and 2 below document
removals: those old PNGs were enlarged versions of the bounded crops,
not imagegen redraws. Batch 3 documents a separate, successful imagegen
redraw of the five API Gateway references.

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

## Batch 3: API Gateway redraws

The five remaining references in `07-api-gateway.md` were inspected with
their original JPGs and bounded crops. Each source contained a webcam
inset or low-resolution console capture. Imagegen was tested with both
inputs, with the crop treated as the authoritative instructional region.
All five redraws below preserved the lesson facts without copying the
camera inset, browser chrome, or uncertain request IDs and timestamps.
They are genuine redraws, not enlarged or sharpened screenshots, and
contain C2PA metadata identifying the OpenAI image-generation service.

| Reference | Source JPG SHA-256 | Bounded crop SHA-256 | Imagegen PNG SHA-256 | Disposition |
| --- | --- | --- | --- | --- |
| `07-api-gateway-01-create-rest-api-crisp.png` | `333e3a90976ff6cae69e3d73d91bab8a2e06c98f30d6680e8fb0c9581679ff45` | `2edac7e09527e6443a764117513c09100a1c25341899d0ac6fb647f0aff24136` | `5155d18d1757da023ced5bddc499602d1a31ac61d230379ee3d7b33a963af462` | Keep: clean redraw preserves the REST API choices, Settings form, and Regional endpoint |
| `07-api-gateway-02-create-resource-crisp.png` | `fc58b24df98f1f32621e369f6c3d9fc00e1f458247eb0199e2025a1f3dc` | `0e719e37ee598cbb26f356e17e1176e99009c8d3814c1c4934b96d050f8a447c` | `977d13ea4a6b038c532453be5666517722e8c1527320d59fc89b1051595a871b` | Keep: clean redraw preserves the `predict` resource, `/predict` path, and unchecked proxy/CORS controls |
| `07-api-gateway-04-method-test-crisp.png` | `810292ea5e06d780520f80d25021057be5d6fd129479135d550f19591afdb4bc` | `f228f9076fbf3a7f789c8eaf2f1d2c46aa7da70788fca391b71245cf6ee4bf4a` | `e5b9408059ce65f1a2947f99610752a5a382c783c2b46fc3242f1a927d46ce8b` | Keep: clean redraw preserves `POST /predict`, the test form, and the exact pants request body |
| `07-api-gateway-05-test-response-crisp.png` | `ec556c6addd08614104a9fe51bc8beba24f9ce715ccde45db62767d99348ee89` | `2e4ae52f141d77fcd5c854989fc0e9de3f979613d3fa9cba0c9c7c0ddbbcfbc2` | `17427b85e7adcd37341c5f46d2d48bfef8e71e4092fd85f6edbcdbbcdd927fef` | Keep: clean redraw preserves all ten class scores, `pants` as the highest score, response headers, and `/predict` logs |
| `07-api-gateway-06-deploy-stage-crisp.png` | `c23a55f392f3132ffef54866385b6903afc2c17f327d477654d70c2c4ae84435` | `248c24a19e1f22cb52652b5b9f987291ef9bbc25a389e69cf88db6bd662f6ded` | `3a970abce3eb3137b9add273c9e199072e636a9686416db4d3e8e5a36586b7d1` | Keep: clean redraw preserves the new stage form and exact stage name `test` |
