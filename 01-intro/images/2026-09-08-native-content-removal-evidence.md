# Native-content illustration removal evidence: 2026-09-08

This focused cleanup removes three image embeds from `06-environment.md`.
The lesson text remains unchanged. The source JPEGs, bounded crops, and prior
PNG derivatives remain in the repository for auditability; only the Markdown
references to the three published PNGs were removed.

## Decision

Each target duplicated commands, code, or a transient notebook interface that
the lesson already explains in native Markdown. The homework screenshot also
exposed a Jupyter token URL. These are native-content or sensitive capture
artifacts, not useful instructional illustrations, so regenerating them would
not improve the lesson. The correct action is to remove the embeds while
preserving the surrounding instructions.

## Exact file hashes

SHA-256 values were recorded before removal. No binary in this table was
deleted or modified by this cleanup.

| Target group | Original video frame | Bounded crop | Published PNG removed from Markdown | Reason |
|---|---|---|---|---|
| Push and install | `06-environment-04-push-pip-install.jpg`<br>`c0c2ea7cd26e7711d4fe023804bdfde4afc4ac66c0e67b910cbf577b097f5370` | `06-environment-04-push-pip-install-cropped.jpg`<br>`e659806d985d6e3d34f1600e51277415b12d6c7ebcd26508163b0ff322552d8e` | `06-environment-04-push-pip-install-crisp.jpg`<br>`55b7dea42ce5a7fce83f3969d405dac36a6dbabcfd2ed07e326c9be33a2ff4a2` | Duplicates the native Git/pip commands immediately above. |
| Jupyter notebook | `06-environment-05-jupyter-notebook.jpg`<br>`b6c0d43be8132bf043841c45c7d91b203a0fdf44a1d1b4439ee34a1e1138ed79` | `06-environment-05-jupyter-notebook-cropped.jpg`<br>`c9785269522fc531cae781881c6b2d2fe4550ea3f3add33209f02b5a870d08f4` | `06-environment-05-jupyter-notebook-crisp.jpg`<br>`c2bf030702b315d9dbc6668a2b73e5840fe8bb610f9be5f41072a5d71eeddc65` | Shows a transient notebook UI rather than adding instructional content; the text already explains how to start and open Jupyter. |
| Homework notebook | `06-environment-06-homework-notebook.jpg`<br>`2e2f2fdb02581d337a7616951b3ef648882cd619f10d8fcaec96daff259ec12e` | `06-environment-06-homework-notebook-cropped.jpg`<br>`2107f0e5fe548448904ba59070bda3471cce40a9a6ba1309dbf98926f7b0dea1` | `06-environment-06-homework-notebook-crisp.jpg`<br>`260b831d92161e795f1f4e11e01258d6897bd12ce5024bf701ad02b64dae8c87` | Duplicates notebook/code content and exposes a Jupyter token URL, so it must not be published as an illustration. |

## Scope check

- Removed exactly three image-reference lines from `06-environment.md`.
- Preserved all lesson prose, commands, and section structure.
- Preserved all nine source/crop/PNG binaries listed above.
- No other module or image reference was changed.
