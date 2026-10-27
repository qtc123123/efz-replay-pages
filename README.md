# EFZ replay player

Experimental browser playback for supported Eternal Fighter Zero Revival recordings.

## Use

[Open the replay player](https://qtc123123.github.io/efz-replay-pages/public/replay.html).
Choose a supported local `.rep` file, select the original battle's **Rounds to win**, and press **Open replay**, then **Play**. The win target supports 1, 2 or 3, with 2 as the default; the recording does not store this setting. No resource key entry or local game installation is required. The recording stays in your browser. Pause, Step and stage-music volume controls are available.

The local replay profile admits all 25 character IDs (0–24), all 23 stages (0–22), and six DAT palette colors (0–5). Supported files use the EFZ Revival marker-104 paired-input extension with a valid saved RNG state. Auxiliary-command high bytes must be zero. Malformed or unsupported recordings are rejected. Files are bounded to 64 MiB and 1,000,000 updates. The selected win setting must reproduce the recording's natural battle end; a mismatch is reported as an error.

Menus are skipped and battle intros run. This is direct battle playback, with no local checkpoint restore, seeking, or live spectator connection. Effect and voice audio is absent. Only the selected stage's music loads on Play; music failure does not stop simulation.

## Deployment contents

The prepared site contains 197 files totaling 187,340,404 bytes, including 176 ciphertext objects and all 23 stage-music payloads. The repository stores its ZIP as nine ordered parts, `replay-site.zip.part-000` through `replay-site.zip.part-008`, each at most 20 MiB. These are pieces of one ZIP, not individual archives. The complete ZIP is reconstructed only by the deployment workflow.

The workflow verifies the exact part list and order, each part's SHA-256, the reconstructed archive's SHA-256, the safe and exact 197-file ZIP member set, and every extracted file's SHA-256. It also checks the extracted file count and absence of symlinks. Only the extracted site is published.

The browser loads the selected characters and stage from the full manifest, and decrypts their resources automatically using a generated access module bound to that manifest. The original key file, plaintext resource files, private recordings and development history are not included. The public access module intentionally supplies the information needed for browser decryption; its obfuscation does not guarantee secrecy or prevent resource extraction.

The packaged `NOTICE.md` and `public/upstream-license.txt` preserve the original source notices. Some NOTICE statements and paths describe the earlier private development layout, including its Git contents and private provenance documents. This repository distributes the generated Pages runtime within the split archive and does not relicense third-party code or game resources.

## Qualification

Resource coverage and admission across these ranges do not establish native correctness for every matchup. This remains an experimental reconstructed engine. Successful artifact verification or hosting does not establish complete browser gameplay, audible audio, Windows-native parity, or whole-session correctness.

Verification for this candidate: the complete Node regression passed 1,055/1,055 tests; a separate campaign passed 150 fresh engine cases using real resources across the supported character/palette coverage; and the original supplied recording completed 7,637 updates with matching local- versus service-engine results. The regression includes synthetic fixtures. The 150 cases are initialization/update checks, not 150 complete recorded matches. These results do not establish native parity or live browser/audio qualification.

T04 service resume remains unimplemented and unqualified. Separate battle recordings do not qualify a continuous startup, selection, loading, results and rematch session. Local playback uses a separate generated engine; the original service engine and its checkpoint admission identity remain unchanged.

## Publishing

In repository Settings, select **Pages → Source → GitHub Actions**. The workflow runs on pushes to `main` and can also be started manually. It needs no custom token or resource-key secret.

Upload all nine parts and the accompanying manifests, README and workflow as one reviewed revision. When replacing the package, update all three checksum manifests and the workflow's expected part and file counts together. Confirm the successful deployment run before treating the new package as live.
