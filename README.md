# EFZ Replay Theater

Experimental browser playback for supported Eternal Fighter Zero Revival recordings, with original game artwork, stage music, sound effects and character voices.

## Watch a recording

[Open the replay theater](https://qtc123123.github.io/efz-replay-pages/public/replay.html).

Choose a local `.rep` file, select the original battle's **Rounds to win**, and press **Open replay**, then **Play**. The win target supports 1, 2 or 3, with 2 as the default; the recording does not store this setting. No resource key entry or local game installation is required. Your recording stays in your browser.

The theater uses the game's decoded title, interface and character portrait artwork. Character portraits follow the recorded palette. Play, Pause, silent single-update Step, fullscreen, and separate stage-music and effects/voices volume controls are available. Space toggles playback; Right Arrow steps while paused.

The local replay profile accepts all 25 character IDs (0–24), all 23 stages (0–22), and six DAT palette colors (0–5). Supported files use the EFZ Revival marker-104 paired-input extension with a valid saved RNG state. Auxiliary-command high bytes must be zero. Files are bounded to 64 MiB and 1,000,000 updates. Unsupported or incomplete recordings are rejected explicitly; the chosen win setting must reproduce the recording's natural battle end.

Menus are skipped and battle intros run. The original engine's observed effect and voice calls drive page-owned audio output. The selected battle's sound resources are prepared before playback. Pause, Step, replacement and completion stop effect playback; Step remains silent. Stage music and effects/voices have separate volume controls. Audio failures are displayed without changing simulation results.

## Reviewed resource contents

The encrypted manifest covers 506 resource paths and 450 unique ciphertext objects: all supported battle resources, 23 stage tracks, 59 original effect paths, 222 original voice paths, and 30 interface/portrait art paths. Original sound inventories are sparse; absent IDs are not replaced with invented clips. The page loads only the selected battle's resources and requested artwork.

Resources decrypt automatically using the generated public access module bound to the exact manifest. The original key file, plaintext resource files, private recordings and development history are excluded. The access module deliberately supplies the information needed for browser decryption; obfuscation does not make published resources secret.

The packaged `NOTICE.md` and `public/upstream-license.txt` preserve the original source notices. Some NOTICE statements and paths describe the earlier private development layout. This repository does not relicense third-party code or game resources.

## Incremental deployment

The final site contains **475 files / 207,527,683 bytes**. Its base is the previously reviewed 197-file artifact, retained in the existing nine `replay-site.zip.part-000` through `replay-site.zip.part-008` blobs. Those parts reconstruct the original ZIP with SHA-256 `aed65571123ffffa0bf7faef47d78860c81ad277d99aefb9f570a11dbe0348ff`. They are reused unchanged.

`sound-art-overlay.zip` contains exactly **288 changed or added files / 20,586,785 ZIP bytes**, including 274 new encrypted objects. It does not repeat any of the original 176 encrypted objects. `base-site-sha256.txt`, `overlay-sha256.txt` and `site-sha256.txt` identify the original, overlay and complete final file sets.

Before deployment, the workflow verifies the exact ordered nine-part set, every part's SHA-256, both archive SHA-256 commitments, and both exact safe ZIP member sets. It extracts and verifies the original 197 files first. It then permits only the declared overlay additions and reviewed replacements, and verifies the complete 475-file result, every file's SHA-256, expected directories, and absence of symlinks or extra files. Only that verified result is uploaded to Pages. All four Actions remain pinned to reviewed commits.

For an update, retain the existing nine base-part blobs and their unchanged part/archive manifests. Publish the overlay, its checksum, the base/overlay/final file manifests, README and workflow as one reviewed revision. Updating the interface or runtime requires regenerating the overlay and its commitments. Do not reupload the 185 MB base archive. Confirm the successful deployment run before treating a prepared revision as live.

## Qualification boundary

Resource coverage does not establish original Windows-game correctness for every matchup. Verification includes authenticated original resource bytes, bounded media decoding, exact archive reconstruction, and a 7,637-update original recording whose complete observed trace matches the preserved service engine. This remains an experimental reconstructed player; those checks do not establish native parity or complete browser/audio qualification across all devices and matches.

Playback is direct battle playback. Seeking, checkpoint restoration, live spectating and continuous session resume are not provided by this page. **T04 service resume remains unimplemented and unqualified.** Separate battle recordings do not qualify startup, selection, loading, results and rematch as one continuous session. The separate Pages engine retains the original service engine and checkpoint admission identity unchanged.
