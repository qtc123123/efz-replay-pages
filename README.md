# EFZ Replay Lab

[Open the replay player](https://qtc123123.github.io/efz-replay-pages/public/replay.html).

Watch supported Eternal Fighter Zero Revival recordings with original game artwork,
stage music, effects and voices, exact restart seeking, and optional read-only analysis.

## Open and watch

Choose **Open replay**, select a local `.rep` recording, then press **Play**. In
**Replay settings**, choose the original battle's win target (1–3; default 2).
The file does not store that target; changing it reloads the recording. No resource
key entry or local game installation is needed. Recordings remain in the browser.

The sharp 4:3 player has video-style overlay controls on desktop and phone. Tap or
click the image to show/hide them. They hide after 2.5 seconds of playback inactivity;
held gestures, keyboard control focus and open Settings keep them visible. Showing
controls never resizes the image. The **Settings gear** opens hitboxes, recorded
inputs, detailed state and restart/previous/next controls. Closing restores focus.

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
- **Recorded inputs:** compact P1-left/P2-right rows beneath each side. A held-frame
  count precedes plain direction/button symbols; neutral rows retain their count.
  Up to six overlay runs come from the existing 128-update cursor window. `≥`
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
and the bound public browser access module are reused byte-for-byte. Browser
delivery supplies the information needed for decryption; public resources are not
secret. Plaintext media, original key files and private recordings are excluded.

Browser engine by **Mu-Tsun Tsai**. Existing `NOTICE.md` and
`public/upstream-license.txt` are retained. This repository does not relicense
third-party code or game resources. The app uses a typographic EFZ Replay Lab
wordmark and existing source artwork; no image generation was used.

## Reviewed deployment

This release publishes source commit
[`77aa85d8d522b1b3c2f516eff4eae2e67316bd3b`](https://github.com/Aquat1c/efz-replay-lab/commit/77aa85d8d522b1b3c2f516eff4eae2e67316bd3b).
Only five deployed paths differ from the previous public release: page HTML/CSS,
the page controller, and the new navigation/control-visibility modules. The engine,
replay/seek/training implementations, encrypted media and access bytes are unchanged.

The final site has **485 files / 207,619,892 bytes**. The unchanged nine base ZIP
parts and sound/art overlay are reused. `game-faithful-overlay.zip` contains the
exact **21-file delta from the sound/art base**, is **390,023 bytes**, and has SHA-256:

```
04cd2b95edce75a35a0c2aaf91c9f73fa22ab8cab625bfa286837317560dec10
```

The final `site-sha256.txt` SHA-256 is:

```
144dca1c2601d473a2ddd95eecef8c70b89b606df618174fae28bf5a88720616
```

The pinned Actions workflow verifies the exact ordered parts, all archive
commitments, safe ZIP member sets, base/delta relationships and complete final
file hashes. Extra files, symlinks, traversal, changed bases and unexpected
overwrites are refused. Only that verified tree is uploaded to Pages.

## Evidence and remaining qualification

Prepublication source regression passed **1,193/1,193 tests**, with zero failures,
skips or cancellations; Python tooling passed **22/22**. The exact candidate passed
**19 actual Chromium interaction groups**, responsive/fullscreen/large-text/reduced-
motion checks, actual UI transition recordings and **35 local served runtime hash
checks**. Independent code/visual review found and retested layout, route, fullscreen,
held-drag and input-display defects. Detailed evidence and limits are recorded in
the [source qualification report](https://github.com/Aquat1c/efz-replay-lab/blob/77aa85d8d522b1b3c2f516eff4eae2e67316bd3b/docs/qualification/DESIGN_RESET_EXECUTION_2026-10-28.md).

This UI release was explicitly requested for publication. Its fresh browser evidence
uses labeled synthetic recordings. The original `.rep` qualification input and the
175 original `nl###.dat` illustrations were not supplied for this iteration. Loading
continues to use the verified replay-art fallback; original NL loading is not claimed.
Prior engine/native-related receipts retain their original scope and are not a new
qualification campaign for this UI. Native Windows parity, physical-device behavior,
audibility and every matchup's correctness are not established by these checks.

**T04 and portable local checkpoints remain unqualified/refused.** Exact restart
seeking does not qualify continuous startup/selection/loading/battle/results/rematch
restoration. No results or rematch lifecycle is fabricated.
