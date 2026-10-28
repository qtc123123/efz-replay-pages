# EFZ Replay Lab

[Open the replay player](https://qtc123123.github.io/efz-replay-pages/public/replay.html).

Watch supported Eternal Fighter Zero Revival recordings with original game artwork,
stage music, effects and voices, exact restart seeking, and optional read-only analysis.

## Open and watch

Choose **Open replay**, select a local `.rep` recording, and wait for loading to finish.
A random original NL illustration covers preparation of the battle, selected-stage
music, effects and fighter voices. The player pauses on the first game image
(including the original intro); press **Play** when ready. In
**Replay settings**, choose the original battle's win target (1–3; default 2).
The file does not store that target; changing it reloads the recording. No resource
key entry or local game installation is needed. Recordings remain in the browser.

The sharp 4:3 player has video-style overlay controls on desktop and phone. Tap or
click the image to show/hide them. They hide after 2.5 seconds of playback inactivity;
held gestures, keyboard control focus and open Sound/Settings menus keep them visible. Showing
controls never resizes the image. The **Settings gear** opens hitboxes, recorded
inputs, detailed state and restart/previous/next controls. The **Sound note** opens
mute and separate music/effects volume sliders. Both menus fit inside the image
and scroll when needed; closing restores focus.

Space plays/pauses, Right Arrow steps, Left Arrow moves back and Home restarts while
paused. F toggles fullscreen. Escape closes Settings, cancels a seek or exits
fullscreen as appropriate. Fullscreen retains one fitted 4:3 game/menu/hitbox plane
with black unused space. Browser Back exits hidden fullscreen safely. Changing
Replay/Watch routes pauses playback and retains the admitted session without
autoplay on return. The entry list reflects only the actual current session.

Seeking uses a fresh Worker and exact resimulation, with progress, cancellation
and a deadline. It can take several seconds. Failed or cancelled same-replay seeks
retain the committed display. Restart returns to preplay; rewind remains available
after completion. One displayed frame/update means a complete engine update:
**64 complete updates per second**, distinct from inner simulation steps.

## Read and inspect

Both players' numerical HP, SP, RF/mode and round wins remain visible together.
Missing values are shown as a dash. Values and prepared images retain their origin
labels, including final last-live values.

- **Hitboxes:** yellow push/body, green hurt and red attack geometry for fighters
  and active children. Attack geometry can remain after a hit and does not prove
  contact is currently damaging.
- **Recorded inputs:** compact P1-left/P2-right rows centered vertically on each side and scaled to the image. A held-frame
  count precedes plain direction/button symbols; neutral rows retain their count.
  Up to fourteen overlay runs come from a 512-update cursor window. `≥`
  marks a hold that began before that window. Timestamped history in Settings can
  seek to a run. This is recorded input, not command acceptance or a live input poll.
- **Detailed state:** source combo counters/damage, independent max hits/max damage
  since actor reset, next-hit scaling, untech/hitstop/freeze timers, state/pattern
  frame, position/facing and HUD counter/timer. Maxima can belong to different combos
  and persist across ordinary round transitions. Internal timers do not prove
  frame advantage or general remaining blockstun.

Analysis rebuilds from the cursor and cannot double-count revisited segments. It
adds no input, RNG, simulation update or render call and does not activate training
mode. Music and effects/voices retain separate volume settings. Steps and historical
seek catch-up are silent; BGM restarts on the next Play after seeking.

**Watch is unavailable on this static site:** no spectator service or global room
directory is connected. The UI does not invent live sessions.

## Supported profile and attribution

The local profile accepts all **25 character IDs**, **23 stages**, **six palettes**,
and explicit win targets **1–3**. Files use the EFZ Revival marker-104 paired-input
extension and a valid saved RNG state, with auxiliary-command high bytes zero.
Limits are 64 MiB and 1,000,000 updates. Unsupported/incomplete files are rejected;
the selected target must reproduce the recording's natural battle end.

The existing encrypted manifest still covers **506 paths / 450 unique ciphertext
objects**, including stage music, effects, voices and interface resources. Resources
and the bound public browser access module are reused byte-for-byte. A separately
bound catalog adds all 175 original NL loading illustrations; only the selected
illustration is fetched for each open. Browser
delivery supplies the information needed for decryption; public resources are not
secret. Plaintext media, original key files and private recordings are excluded.

Browser engine by **Mu-Tsun Tsai**. Existing `NOTICE.md` and
`public/upstream-license.txt` are retained. This repository does not relicense
third-party code or game resources. The app uses a typographic EFZ Replay Lab
wordmark and existing source artwork; no image generation was used.

## Reviewed deployment

This release publishes source commit
[`9ef2ef5ba49209e96647472ad0e725b066e01d54`](https://github.com/Aquat1c/efz-replay-lab/commit/9ef2ef5ba49209e96647472ad0e725b066e01d54).
The loading correction updates page HTML/CSS/controller, audio owners and deployment
configuration, adding the loading-art owner and 176 encrypted loading-pack files.
The engine, replay/seek/training implementations, original battle media and bound
access bytes are unchanged.

The final site has **662 files / 214,400,398 bytes**. The unchanged
nine base ZIP parts and sound/art overlay are reused. `game-faithful-overlay.zip`
contains the exact **199-file delta from the sound/art base**, is
**7,191,387 bytes**, and has SHA-256:

```
4dc56376802408c1b7d700d5689fc3c8aead52234968e89d9f1bbc92e492df7f
```

The final `site-sha256.txt` SHA-256 is:

```
ef5ef853d36647e27c1ca3516512231f00aa741e2dbd5a29c1674c88bd5c236a
```

The pinned Actions workflow verifies the exact ordered parts, all archive
commitments, safe ZIP member sets, base/delta relationships and complete final
file hashes. Extra files, symlinks, traversal, changed bases and unexpected
overwrites are refused. Only that verified tree is uploaded to Pages.

## Evidence and remaining qualification

Prepublication source regression passed **1,207/1,207 tests**, with zero failures,
skips or cancellations. The exact candidate passed **19 shell interaction groups**
and **six loading/menu groups** in actual Chromium, including phone, landscape,
fullscreen, silent audio preparation, first-frame pause and replacement ownership.
Independent review found and retested a hidden-route initial-step race, volume
label grouping and a scrolling Close control. Detailed evidence and limits are in
the [source qualification report](https://github.com/Aquat1c/efz-replay-lab/blob/9ef2ef5ba49209e96647472ad0e725b066e01d54/docs/qualification/PLAYER_LOADING_2026-10-28.md).

This UI release was explicitly requested for publication. Its fresh browser evidence
uses labeled synthetic recordings. All 175 original NL illustrations were supplied
through the user's Drive folder and hash-verified. No original `.rep` was supplied
for this correction. Prior engine/native receipts retain their original scope;
native Windows parity, physical-device behavior, audibility and every matchup's
correctness are not established by these checks.

**T04 and portable local checkpoints remain unqualified/refused.** Exact restart
seeking does not qualify continuous startup/selection/loading/battle/results/rematch
restoration. No results or rematch lifecycle is fabricated.
