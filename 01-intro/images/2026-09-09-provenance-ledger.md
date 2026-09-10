# Strict provenance audit — 20 active refs

Date: 2026-09-09

Scope: the 20 active image refs in cohorts/2026/01-intro that were outside the existing nine-entry repair ledger in 2026-09-08-imagegen-repair-provenance.md.

## Provenance method

Every accepted output in this ledger has the following durable chain:

1. The original non-crisp JPG in this directory was retained as the source.
2. A bounded native crop was made from decoded JPG pixels with 2026-09-09-provenance-crops.sh. The script uses ImageMagick -crop geometry +repage -strip only; it does not resize, use Lanczos, sharpen, or enhance.
3. The original JPG and the native crop were supplied to built-in imagegen. The previous crisp target was never supplied as an input.
4. The generated PNG was copied byte-for-byte from the imagegen output cache into the active target filename. The C2PA marker and imagegen run ID are recorded below.
5. Each target was inspected at native dimensions and in a temporary width-608 simulation. Simulated files are inspection-only and are not tracked.

The existing reviewed native crop for the VS Code reference was reused byte-for-byte at geometry 520x360+0+0; the crop script checks that it exists and does not recreate it.

## Active-file manifest

| Active target | Original JPG | Native crop and geometry | Imagegen run | Native → simulated 608 |
|---|---|---|---|---|
| 01-what-is-ml-01-price-field-imagegen-pilot.jpg | 01-what-is-ml-01-price-field.jpg | 01-what-is-ml-01-price-field-cropped.jpg; 380x190+115+100 | f8049755-0ea5-412a-b80a-55d897c2f52b | 1774x887 → 608x304 |
| 01-what-is-ml-03-expert-or-model-imagegen-pilot.jpg | 01-what-is-ml-03-expert-or-model.jpg | 01-what-is-ml-03-expert-or-model-cropped.jpg; 530x243+35+82 | 1c32f02a-830d-4897-8afd-96a045e9ae5c | 1853x849 → 608x279 |
| 02-ml-vs-rules-01-spam-examples-imagegen-pilot.jpg | 02-ml-vs-rules-01-spam-examples.jpg | 02-ml-vs-rules-01-spam-examples-cropped.jpg; 530x243+35+82 | 430e9775-0a15-4648-8d20-defe3ec31387 | 1853x849 → 608x279 |
| 02-ml-vs-rules-03-more-spam-imagegen-pilot.jpg | 02-ml-vs-rules-03-more-spam.jpg | 02-ml-vs-rules-03-more-spam-cropped.jpg; 530x243+35+82 | c9c9f8f5-babc-4795-a75d-5c361b00d2a2 | 1853x849 → 608x279 |
| 02-ml-vs-rules-05-encode-email-imagegen-pilot.jpg | 02-ml-vs-rules-05-encode-email.jpg | 02-ml-vs-rules-05-encode-email-cropped.jpg; 520x243+45+82 | fdf78796-93af-4c42-bb92-25f9395e0e99 | 1836x857 → 608x284 |
| 02-ml-vs-rules-07-rule-based-summary-imagegen-pilot.jpg | 02-ml-vs-rules-07-rule-based-summary.jpg | 02-ml-vs-rules-07-rule-based-summary-cropped.jpg; 510x243+55+82 | 3c64e197-6d19-4b33-a6a9-1cca597eb653 | 1816x866 → 608x290 |
| 02-ml-vs-rules-08-ml-summary-imagegen-pilot.jpg | 02-ml-vs-rules-08-ml-summary.jpg | 02-ml-vs-rules-08-ml-summary-cropped.jpg; 540x243+25+82 | c5d0ff54-5635-4438-8052-82e74dd0d9ec | 1871x840 → 608x273 |
| 03-supervised-ml-04-regression-imagegen-pilot.jpg | 03-supervised-ml-04-regression.jpg | 03-supervised-ml-04-regression-cropped.jpg; 545x243+20+82 | 92d91851-06f6-4ff1-920b-4cb9dac08ddb | 1880x837 → 608x271 |
| 03-supervised-ml-06-ranking-imagegen-pilot.jpg | 03-supervised-ml-06-ranking.jpg | 03-supervised-ml-06-ranking-cropped.jpg; 555x243+10+82 | 80defd55-1e99-4111-b06c-ef116a485482 | 1896x830 → 608x266 |
| 03-supervised-ml-07-summary-imagegen-pilot.jpg | 03-supervised-ml-07-summary.jpg | 03-supervised-ml-07-summary-cropped.jpg; 545x243+20+82 | b8e7c50c-dda3-4ea9-8d5c-8c965eb4bf02 | 1880x837 → 608x271 |
| 04-crisp-dm-02-process-diagram-imagegen-pilot.jpg | 04-crisp-dm-02-process-diagram.jpg | 04-crisp-dm-02-process-diagram-cropped.jpg; 545x243+20+82 | 63a426ef-324f-4c38-b9db-a978365a439f | 1617x973 → 608x366 |
| 04-crisp-dm-03-business-understanding-imagegen-pilot.jpg | 04-crisp-dm-03-business-understanding.jpg | 04-crisp-dm-03-business-understanding-cropped.jpg; 545x243+20+82 | d549d087-82c2-4cce-9dc2-75555e5b1d69 | 1617x973 → 608x366 |
| 04-crisp-dm-04-data-preparation-imagegen-pilot.jpg | 04-crisp-dm-04-data-preparation.jpg | 04-crisp-dm-04-data-preparation-cropped.jpg; 555x243+10+82 | 7e7a5539-32b1-4b08-9162-4cf13cd480c4 | 1897x829 → 608x266 |
| 05-model-selection-01-train-validation-imagegen-pilot.jpg | 05-model-selection-01-train-validation.jpg | 05-model-selection-01-train-validation-cropped.jpg; 530x243+35+82 | 08f7bf1b-d323-46cc-945e-3ab3088747a2 | 1853x849 → 608x279 |
| 05-model-selection-03-train-valid-test-imagegen-pilot.jpg | 05-model-selection-03-train-valid-test.jpg | 05-model-selection-03-train-valid-test-cropped.jpg; 545x243+20+82 | 1966232a-f866-47a7-976a-c33bc0e30c92 | 1774x887 → 608x304 |
| 05-model-selection-04-select-and-test-imagegen-pilot.jpg | 05-model-selection-04-select-and-test.jpg | 05-model-selection-04-select-and-test-cropped.jpg; 545x243+20+82 | 8c472e56-4b7e-4743-a2ce-e44808269474 | 1880x837 → 608x271 |
| 06-environment-03-vscode-desktop-crisp.jpg | 06-environment-03-vscode-desktop.jpg | 06-environment-03-vscode-desktop-cropped.jpg; 520x360+0+0 | a06d0643-ca7b-4fac-ae22-94b9592f363a | 1672x941 → 608x342 |
| 10-summary-04-supervised-g-x-y-imagegen-pilot.jpg | 10-summary-04-supervised-g-x-y.jpg | 10-summary-04-supervised-g-x-y-cropped.jpg; 545x243+20+82 | f4ede5fb-0db9-472c-8cd5-faf62632f2a7 | 1880x837 → 608x271 |
| 10-summary-05-crisp-dm-bigger-picture-imagegen-pilot.jpg | 10-summary-05-crisp-dm-bigger-picture.jpg | 10-summary-05-crisp-dm-bigger-picture-cropped.jpg; 545x243+20+82 | aac0efb5-f002-445a-bc39-867a9b0a28ac | 1617x973 → 608x366 |
| 10-summary-06-model-selection-split-imagegen-pilot.jpg | 10-summary-06-model-selection-split.jpg | 10-summary-06-model-selection-split-cropped.jpg; 545x243+20+82 | 65ffba39-8295-4fb8-a0be-37a4de0bebc2 | 1880x837 → 608x271 |

## Hash and C2PA manifest

All hashes are SHA-256. “Previous” is the active target at the audit starting point; “current” is the accepted replacement.

| Active target | JPG SHA-256 | Crop SHA-256 | Previous target SHA-256 | Current target SHA-256 | C2PA urn |
|---|---|---|---|---|---|
| 01-what-is-ml-01-price-field-imagegen-pilot.jpg | 896d01de5b17c1752b6646dfed88cc8b2f57349a1b7dd87ae1e545fac3b7c1d9 | 9be2022088ca3803d890385a7c575797ab381dc46ff33f767bf1ede77f5ee04d | a6efe54ffc8168955a80aad3ce185341decdae875b9dd17f5ad391a264763edb | 3d91796f49bf60be527aabbc0975ebd8222a9fa5e8641f16644622512e6daa71 | urn:c2pa:55320464-8f76-4a2d-b24a-f66a517f8e58 |
| 01-what-is-ml-03-expert-or-model-imagegen-pilot.jpg | 3c2cbb86093bd0fc326e916e17aaecf3df79e738d6092a21a5538d6f431f0bd8 | 4a742ee0a2e847ce3e4b58dc8e0fd499ed28c8c2d871e10c14b0fd288bb75342 | 54e8e2e215d8d507ec09c651d44cd800567364a2a3cc6f54eacfae7ff7c827a6 | e943c987c17edc6868db6445799d7f6e21bf89ef4f8ca2eedc0e2bd5410e2ce8 | urn:c2pa:ae690e22-8b2a-4614-8b14-6ed861c3c75e |
| 02-ml-vs-rules-01-spam-examples-imagegen-pilot.jpg | af5d47b147cb5f3ca64b5b28a4394a54be926ca7aeb469d0c84513b446e216e8 | 72d1c185bb5ef0698ce99cfc344ab565fb5a8adb58c0e0ed63c05742677aa601 | c16e316bb7d0f83549fb4d934676dce0336f5e48412d48a9247a1fb234262d66 | 23ee0a00629ebf2083d760b0be4eb82296fdf8334ce9a8b608f6d8dcaa298335 | urn:c2pa:4ee92605-16b3-4fba-8a18-69ddc8cda1d0 |
| 02-ml-vs-rules-03-more-spam-imagegen-pilot.jpg | 5166cc329b73a7a2a39da4cf832f47c157fe840f4e2fa083d546bfce8c4df34f | 535bf1ee8ad91d51b320c79989c2a395bb026d10a61c2ffb94348e7d998de042 | a8bdffa12b044f359e7751ca7406455c0fa47353190997ffa430375fbea5d794 | ee6ee898753da41fdc938587ce700b9241db730ce39964fae8325459d193228f | urn:c2pa:19dc2296-49bf-4510-8ddb-f16e17eca05f |
| 02-ml-vs-rules-05-encode-email-imagegen-pilot.jpg | f08d2605ba313e115ab10ad5c232bdcc725622d8dcd6fa13e5eb1afa8e21eb0e | 154a6467ac42ab09b3192c5a7e0d26b2fd0543553c768ce2ca57b0977123ec0b | e149c8b4918efefcbbc8a0f9750874c3a702be314f1170c38cbe86a665e886a8 | eddfa3ccaf5b4de933b13bc674502010313ba22b52cdf1d26b96f4941510df89 | urn:c2pa:75f3e1dd-04c5-4ac7-891a-5bfc09327227 |
| 02-ml-vs-rules-07-rule-based-summary-imagegen-pilot.jpg | b568548a544c0c502cc9636a8ecbbbb86ade32a3c069b416ecce9f8861ac074c | a33b3dc983bfb01ee9e907fb09745e641210ca4b0a91443f77ceb2454a5b6b2f | 3ad7f61448fbae4e7a7ef5b793d4428683b5b42022ad1aadce72dc7b5ff2e7a8 | 95eb50a726700b08b600e0c934356ba89c5676f7ba76e430cad2cf30dfdff381 | urn:c2pa:6cfdd770-7726-4034-94c5-9a319344d05d |
| 02-ml-vs-rules-08-ml-summary-imagegen-pilot.jpg | bf69ac85f802211baee83894bff65a641e635560f1509d084c1f2c7c846acbc0 | 16c4b8489cf71a6ee44c4ffc1d8b9fd4252815465789e2602c893278d734dfec | d5f10bc2eb20dda838234bfda331f98fae16212f5928b50358dbba559febdac8 | c52a8e5cbf9a9d5a625ac4c7a2a8149542400e943caf9516d4e14a95cacdf48f | urn:c2pa:17c8e2f7-dcec-4541-888e-96dd2fffca44 |
| 03-supervised-ml-04-regression-imagegen-pilot.jpg | 30c201f3a354b485ac0154402675c1bd01ed6dd352c3f0188c059dad55e4d057 | 1e0e12d979559de85656fc6fb91353a261e214cf65f4cf5d5581925429d0e167 | 138d5dcce5cfb78684515b57de0416bc955253d2301a842067bc5f1df2157f92 | e585be3e9656f06a2656f8eeb610f9a5efaa895ebfe2aeb79cf2349cc2d06b29 | urn:c2pa:aeae2b07-fae6-4708-aa70-a98a52ed502d |
| 03-supervised-ml-06-ranking-imagegen-pilot.jpg | 9f5ecb7dcc3060290f875c07481da3e56a0c79598de09bee6b420e4ef3d3fcc9 | 62175b7643dfc255d384579e9533c33b5ca932af1a76edb1283a0605860bdd3a | 53958cb468148cdbbc1d6065bec605c8309744119d896b79a2ade66300eac5b0 | e32aee347424bfe224e25a1cd2d96f1116bc402d01ecf7ea3c2f753007a5bd1b | urn:c2pa:a0461316-49f7-46fd-9201-f189056ac215 |
| 03-supervised-ml-07-summary-imagegen-pilot.jpg | 5d63a81bd501c3df7a589e3b48c746e6d16eb6205afbcce2cbd9d88a4ddfe69c | d471d5799c0baadef9e70199fb37d8534047f62f2e73d8e45bfc8c8324fb8a40 | 139c19edec9d9d9019877778c1ad74d39c6f664cc2131a301054ca2ee4d687d3 | dc979e95b8f1af79f41127dd7a301df37b16afa9a6435ff80336f64aedc344d4 | urn:c2pa:b6acfa43-6271-4efc-8e9e-34566055fbb3 |
| 04-crisp-dm-02-process-diagram-imagegen-pilot.jpg | 232e397db35bc99d24407f6b9ba141ffb1032a657c78eee293064601e4ea0fe6 | 83a85b3ea2af00d6dfa32d899456230b416ccc1eb7e8d3ece3801336fc26262a | a41b373de37ee55e19c18c62c85ad13af5d5743a37b329bd638de1c8dc667b94 | cd8bd5c26a3052442e7b743b55b35da92828ab01475b42137f846beec440f43c | urn:c2pa:bef87c3b-1272-4f98-b76e-668aaa17bea4 |
| 04-crisp-dm-03-business-understanding-imagegen-pilot.jpg | 95912cf4152bfc56d4e8080fe555da38fed4f6a7a1b57ab834dfb2a60e18fb4e | af44ef39c8b440dec434a624e3d6fae29a58553d45c0a3ef9fe5421d36a87b4a | 867e7620554420a135a134acb0c6510be5e81ba5495bb4094fb64b9f8774748d | 925aeedb9e6c145c5b745a1237728c6534693dd725c62c89ceba46f515a9da4f | urn:c2pa:48d33d0d-89a5-438c-816f-727cb8fa7b69 |
| 04-crisp-dm-04-data-preparation-imagegen-pilot.jpg | 08a3fd7886d1ef1a107fb435b60ca2d3b90782e569bdc3656f7b41366a161bd2 | 0fe0f5f25cc740bc8e3e291c92bc82fb1245ae75e4e73c1553cb08c7d2cf8a5d | ee660da9fbcb8ce527e6987b9634afb9b36c5cf036761d5fe26065df8ec11af4 | 8898180f0eafa2bd14025a4d2c60e1f39013edee74fadfbcaa27eaea22ebce66 | urn:c2pa:819ac0ff-c48d-4854-bb15-b6de4a9b1ceb |
| 05-model-selection-01-train-validation-imagegen-pilot.jpg | 8233c36ee0cd7b30175433f7914e6233432b20610426d7507df7492a6022a8a0 | d6ed798f9f5ba0c8ca6522a45f3cac9d8cf80c9c6e0d9c63cc17dd2fb9afc8f2 | 40d8cf2d3207980329b7dfa0e45e0587048e5cd85091231c9ca2cc5031405905 | a0d548dadca015151bc9bc19fc39d81b0b6153b77eae1de190d866f0ae939395 | urn:c2pa:7ac7dcd0-8a08-4b17-b338-547734f496e8 |
| 05-model-selection-03-train-valid-test-imagegen-pilot.jpg | 4332a9690fda4c6b8c722a4cb7305a76743c91422a8c75bbcb6609f00018f1a4 | 52f0a4cbbb404bad274bcde33d476ffd5555013ba77492e22f4496b328e284d6 | b195f1489907228787f07ee04f4e78598f1a39d7f4e77a9d7c67a4338eeb3a04 | 44382970c3326c821eb87b11c66943ddfcf6351d25d25e05a7b0ed5b33d225ae | urn:c2pa:88be278f-1d41-444a-b86c-56a0264b7315 |
| 05-model-selection-04-select-and-test-imagegen-pilot.jpg | 2c9fc79073381894c38e8dfd9509479e431539db8ae199f4c3f9fb8452529bdd | f6cdbcd99d540bb47b367c04fb3ae6990e14c65ec6c587d9769ef1ae527c76c6 | 626fd2b92da3738715a5c8cf045fb64e3b27d61e10b7b9e5a13fe3301ccfeef5 | 4014de357a062c971272b76e705c80c068ef213355ab44492564dfe0f950b927 | urn:c2pa:66870c17-992e-4be3-b0c2-5622cfa88d34 |
| 06-environment-03-vscode-desktop-crisp.jpg | 2ea080ed2f4bb39553a40136c9afc201f9d67d18c1396a1d7a88e0cd9803204b | 2bae49dad5f5a1e317f9cfed70c7e361bf64ac2bad1a10a5b68e7d97d18c6a56 | 9e3b22cfd90d8f15c15421e331e748aa8e1541625fcd40368360ad30d993586b | 9e15a3c3c0772dc97ebeb8817148caaa9b23e3382e314b4fe7cf656e97c68a8f | urn:c2pa:8f45380f-d9c5-4d47-9c93-04125a936e92 |
| 10-summary-04-supervised-g-x-y-imagegen-pilot.jpg | 0151eb979629f64a66bfcee4cd45913dd2c908db00fc0e350a369085d3393830 | 6323680f6fc473ec7882d2a1baa924361383798030bc73211361d85193e573d6 | 0942cec416cb043c5a3ec43341579027e63cd420c480b49dd630bf1c425ad5e7 | 1533bc3e434f09e13880d6168dfa161f6ddf76f7903a85a5109715e815f76321 | urn:c2pa:d8f1cb67-d320-40d9-846c-0cf1a0867076 |
| 10-summary-05-crisp-dm-bigger-picture-imagegen-pilot.jpg | 1bdf1cbef352e66e9a3678f6fdac61ae90f989d81de014e60b1359a61ed39dfe | 3eb05e13ba250cf2e4e7b5e48f124ab7893280b7ee0912bda4c16b933f2d3a38 | 4ec1e44514272507b4294a54ab9fa7031c89b4058d2c8f35d236602aac5c9a1e | 377a60d590d842b5c0915f8e71265de94b803d4a8ee96ab86f80ad009176a0fd | urn:c2pa:5f1a25c4-2624-4b91-9e5d-6e82448fcfc8 |
| 10-summary-06-model-selection-split-imagegen-pilot.jpg | 00b539967d33d30771c8ebebd5c91e0d8c792742b8d673b27e9f1c20ea5ba0e1 | 59c7230d24abe1a2a833bc70d094285645ceeb3d389b4bdabe089a1c7e281ebc | 9b5aa425c8dc4127126a73c6873974484a1c939236efad65578aeb2a9cd53671 | 7549d34b922c39ee9f64a3b5781b814818e8d888a872a489c50661892ac1bffc | urn:c2pa:1c6a94e1-06c5-41da-8f9b-869dccfc2c57 |

## Semantic and artifact checks

- Price-field redraw: Price, Exchange, Price *, blank input, UAH, and Required field; no suggested price or numeric value was introduced.
- Expert/model redraw: both DATA → faceless expert → PATTERNS and DATA → ML → PATTERNS, plus the exact caption If an expert can, so can a model!
- Spam redraws: exact visible subject/from/body/URL content, including the tax URL, prize language, $10, SPAM, and the encoded vector [1, 1, 0, 0, 1, 1]; no operational overlay or capture artifact.
- Rule/ML summaries: exact DATA, CODE, SOFTWARE, OUTCOME, SPAM/NOT, ML, MODEL, and DATA + MODEL ⇒ OUTCOME relationships.
- Supervised-learning redraws: regression $50k, ranking score axis and recommendations, and g(X) ≈ y with feature, model, and target.
- CRISP-DM redraws: all six stage labels, arrows, data cylinder, exact business-understanding sentence, blue Modeling emphasis, and exact data-preparation table values.
- Model-selection redraws: TRAIN/VAL notation, validation/test split and NN, exact LR/DT/RF/NN percentages, and TEST arrow.
- VS Code redraw: exact project title, repository name, README code, terminal path/branch, and lesson UI; no face, cursor, caret, or selection overlay.
- Summary redraws: exact supervised equation, CRISP-DM cycle, Modeling annotation, numbered model-selection list, and train/validation/test rectangle.

The first VS Code candidate was rejected because it retained a terminal caret and code-selection highlight; the accepted run is a06d0643-ca7b-4fac-ae22-94b9592f363a. The first spam-vector request was safety-blocked; it was not used. The accepted fdf78796-93af-4c42-bb92-25f9395e0e99 run used neutral classroom framing and was visually checked. No active output in this 20-ref set was retained unchanged: all 20 active targets now have current JPG → native crop → imagegen evidence. The prior nine accepted refs remain covered by the 2026-09-08 ledger and were not modified.

## Reproducibility checks

- Crop script SHA-256: 0de093d4f046c04b5f4e210ddf7f974c51cd37b226b09f2d3cba75c834456c39
- Aggregate SHA-256 of all 20 crop files before and after rerunning the crop script: a39992e27c109046f7804295f1330f109c91f3fe1c00b99da6605d7bb302ab67
- All 20 accepted targets contain a C2PA urn:c2pa: marker.
- The 20 current target hashes differ from their recorded previous hashes.
- Native and simulated-608 visual passes were completed; simulated files were kept only under .tmp/ and are not part of the deliverable.
