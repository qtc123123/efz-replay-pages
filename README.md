# EFZ replay player

Browser playback for supported Eternal Fighter Zero Revival recordings, with original game artwork, stage music, effects, voices, exact restart seeking and an optional read-only training inspector.

## Watch and inspect a recording

[Open the replay player](https://qtc123123.github.io/efz-replay-pages/public/replay.html).

Set **First to** to the original battle's win target (1, 2 or 3; default 2), choose **Open replay**, select your local `.rep` file, then press **Play**. The recording does not store the win target. No resource key entry or local game installation is required. Your recording stays in your browser.

The neutral title/replay menu appears before full validation. After admission, the original character-select background, moving portrait strips, wings, nameplates and HUD textures surround the dominant 4:3 game image. Only the two recorded fighters and their palettes are shown. Invalid or replacement uploads clear the old identity immediately. Decorative artwork comes from original game resources; operational labels remain accessible HTML.

Use Play/Pause, Restart, Previous, Next, the timeline and Fullscreen. Space toggles playback, Right Arrow steps, Left Arrow moves back and Home restarts while paused. One displayed update means one complete engine update; this Pages profile runs at **64 complete updates per second**, distinct from its inner simulation steps. Timeline release starts a fresh-Worker resimulation with progress, cancellation and a deadline. Seeking is multi-second. Failed or cancelled same-replay seeks retain the previous valid display. Restart returns to preplay without inventing a battle frame; rewind remains available after completion.

The small player panels show raw HP, SP, RF/mode and wins. Open **Training inspector** for:

- **Hitboxes:** yellow fighter push/body, plus green hurt and red attack geometry for fighters and active children. Attack geometry can remain after a hit; it does not guarantee that contact is currently damaging.
- **Recorded inputs:** held directions and A–D buttons, with timestamped runs you can click to seek. History is reconstructed from the current cursor, so revisiting a segment cannot double-count it. This is recorded input, not a claim that the engine accepted a command.
- **Detailed state:** the raw combo counter, current/last combo damage, round maxima, next-hit scaling, untech/hitstop/freeze counters, state/pattern frame, position/facing and separate HUD counter/timer. Maxima reset each round. Internal timers do not establish frame advantage or general remaining blockstun.

The inspector labels actor-value and prepared-image origins separately. It reads existing state without adding input, RNG, update or render calls. It does not activate training mode or alter the recording.

Music and effects/voices have separate volume controls. Pause, Step, replacement and completion stop transient effects; Step is silent. Hidden seeking discards historical sounds, and BGM restarts on the next Play after seek. Audio failures are displayed without changing simulation results.

## Supported profile and resources

The local profile accepts all **25 character IDs**, **23 stages**, **six palettes**, and explicit win targets **1–3**. Supported files use the EFZ Revival marker-104 paired-input extension with a valid saved RNG state. Auxiliary-command high bytes must be zero. Files are bounded to 64 MiB and 1,000,000 updates. Unsupported or incomplete files are rejected; the chosen win target must reproduce the recording's natural battle end. Menus are skipped and battle intros run.

The unchanged encrypted manifest covers **506 resource paths and 450 unique ciphertext objects**: supported battle resources, 23 stage tracks, 59 effect paths and 222 voice paths. The presentation now uses 31 interface/portrait paths; its additional `system/object.dat` role reuses a resource already required by battle. No new resource bytes were added for this revision. Sparse original sound inventories are preserved without invented replacement clips.

Resources decrypt automatically through the public access module bound to the exact manifest. Original key files, plaintext media, private recordings and development history are excluded. Browser delivery necessarily supplies the information needed for decryption; it does not make public resources secret. `NOTICE.md` and `public/upstream-license.txt` preserve upstream notices. This repository does not relicense third-party code or game resources.

## Reviewed deployment

The site contains **483 files / 207,590,903 bytes**. Deployment reuses the unchanged nine base ZIP parts and original sound/art overlay. The third `game-faithful-overlay.zip` contains exactly **19 changed or added files / 389,994 ZIP bytes**. Its SHA-256 is:

```
a428c463b8621ce9a67857b82a11ed5c1835fb610f2502927330788107132d6f
```

The final `site-sha256.txt` SHA-256 is:

```
f3561f44a762e51e5d2056569893797ed602e8a10c309cbbb229958841e85d83
```

The pinned Actions workflow verifies the exact ordered nine-part set, all three archive commitments, safe exact ZIP member sets, the 197-file base, the 475-file sound/art result, the exact 19-file code delta and the complete 483-file final tree. It rejects extra files, symlinks, traversal, changed bases and unexpected overwrites. Encrypted resources and bound browser access must remain byte-identical. Only that verified tree is uploaded to Pages. Future updates must regenerate the code overlay and commitments together; do not reupload the unchanged base archive.

Implementation and detailed qualification are maintained on the isolated [source branch](https://github.com/Aquat1c/efz-replay-lab/tree/feat/game-faithful-replay-verified-20261027). Source main and the recovered working checkout are preserved.

## Qualification boundary

The fresh source regression passed **1,175 tests**, with no failures or skips. Original-recording and representative animated-stage/character probes compared **69,473 target/suffix boundaries**, including prepared images, raw statistics and training projection. The original observation trace and separate service engine remain unchanged. Source-art checks cover all 25 character identities and six palettes. Exact extracted-artifact and live browser reports are recorded separately with their own hashes, timings and publication status.

These are pinned-JavaScript/source agreement and browser checks. They do not establish native Windows parity, physical audibility, every matchup's correctness or actual mobile-device performance. The inspector does not infer frame advantage, generic throw boxes or cumulative match damage from unproven signals.

**T04 remains unimplemented and unqualified.** Local checkpoints remain refused. Restart seeking does not qualify portable restoration or continuous startup, selection, loading, battle, results and rematch resume. No results/rematch lifecycle is fabricated.
