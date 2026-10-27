# EFZ replay player

[Open the player](https://qtc123123.github.io/efz-replay-pages/public/replay.html).

Choose the battle's **First to** setting (1–3, default 2), then open a local `.rep` file and press **Play**. The recording does not store that win target. No resource key entry or game installation is required. Recording bytes stay in the browser.

## Playback and navigation

The original EFZ title/replay artwork supplies the neutral opening screen and selected menu states. Fighters appear only after full replay validation, using the two recorded characters and palettes. Replacement clears the old match immediately. The complete game image keeps its 4:3 proportions, with nearby controls and small fighter/stat panels.

Play/Pause, single-update Step, Previous update, Restart, a release-to-seek timeline and fullscreen are available. **Space** toggles playback, **Right/Left Arrow** move one update, **Home** restarts and **Escape** cancels a seek. Volume controls for music and effects/voices are independent.

The cursor counts complete battle updates at 64 per second. Boundary N means inputs `[0,N)` have been consumed. Seeking starts a fresh Worker and executes all normal updates and stateful renders to the target. It hides only historical external images and sounds. Progress and Cancel remain available; cancellation or a failed same-replay seek keeps the previous valid position. Later targets can take several seconds, and a 120-second deadline bounds long seeks. Rewind remains available after natural completion.

Restart displays the identified preplay state without generating an extra battle image. The image's actual origin and the statistics boundary are labelled separately. HP, SP, RF/mode and round wins follow the cursor, with no accumulated damage/combo totals. HP can be negative at KO or reach 10000 for Makoto. SP is the sole super meter (0–3000); RF retains fractional values (0–1000) and normal/blue mode. Final carried values keep their original live update label. No per-frame history is retained or counted twice.

Seeking stops effects/voices and resets music. Historical sound events are discarded; the next Play restarts the selected stage track. Step is silent. This is a defined browser audio policy, not sample-accurate native audio restoration.

## Supported input and resources

The local profile retains all 25 character IDs, 23 stages, six recorded DAT palettes and explicit win targets of 1–3. It accepts the existing marker-104 paired-input extension with a valid saved RNG state and zero auxiliary-command high bytes, bounded to 64 MiB and 1,000,000 updates. Unsupported and malformed files fail clearly. Playback validates the exact natural battle end rather than treating a valid header as sufficient.

The unchanged authenticated encrypted pack contains 506 resource paths and 450 unique ciphertext objects: supported battle resources, 23 tracks, 59 effects, 222 voices and 30 interface/portrait paths. The player loads the selected battle and requested artwork. The generated browser access module remains bound to the exact manifest; published obfuscation does not make browser-delivered resources secret. Original plaintext files, raw operator keys, private recordings, full native decompilations and development history are excluded.

Original source notices remain in `NOTICE.md` and `public/upstream-license.txt`. This repository does not relicense third-party code or game resources.

## Reviewed incremental deployment

The final site contains **480 files / 207,554,697 bytes**. The original nine base archive parts and the existing sound/art overlay remain unchanged. `game-faithful-overlay.zip` adds exactly **15 changed or new code/configuration files / 378,283 ZIP bytes**, with SHA-256 `326d24b09cc717ea3bcff251e9f0da78637b9ea95574ea1a6975e5f4f977abf5`. It contains no resource payloads.

`base-site-sha256.txt`, `overlay-sha256.txt`, `sound-art-site-sha256.txt`, `game-faithful-overlay-sha256.txt` and `site-sha256.txt` identify each archive stage and the complete final tree. The final file manifest has SHA-256 `736cf369e219776c72f25b240aa8c60ac4fe06a6583b1c81db077f133461d393`.

The pinned workflow verifies every archive commitment, exact safe member inventory, prior file identity before overwriting, and every final file digest. It refuses extra files, symlinks, unreviewed replacements and changes to the existing encrypted resources or bound browser access module. Only the fully verified result is uploaded to Pages.

## Qualification boundary

Fresh checks compare the original 7,637-update recording and representative animated-stage/character probes against sequential execution in the pinned JavaScript engine. Source-derived menu samples are compared with the original pinned JavaScript routines and actual resources. Browser checks cover cursor-relative output, transport, races and desktop/narrow/touch-emulated layouts. These checks establish scoped JavaScript agreement and observed browser behavior; they do not establish native Windows parity, every matchup, physical audibility or performance on actual mobile hardware.

The separate service engine SHA-256 remains `7d5a8e117394ca29fea3a139eadc95cab88e7f6b0427078d1dc64584ed676f3c`. General local checkpoints remain refused. **T04 is unimplemented and unqualified**: finite battle rewind does not qualify continuous startup, selection, loading, battle, results and rematch resume. No native results/rematch lifecycle is fabricated. Long recordings can exceed the restart-seek deadline; qualified checkpoint acceleration and advanced replay history are future work.
