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

The page uses the supplied original animated city behind a blurred translucent
layer, with the original sunset softened beneath the header. Open replay is one
compact action in each view. Decorative motion pauses for reduced-motion
preference, hidden tabs and fullscreen; it cannot advance a replay.

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

Site, Netplay support and Engine modification by **Aquatic**.
Original web engine by **Mu-Tsun Tsai**. Game created by **Twilight Frontier**,
all rights reserved. This site is not affiliated with Team Shanghai Alice or
Twilight Frontier. Existing `NOTICE.md` and
`public/upstream-license.txt` are retained. This repository does not relicense
third-party code or game resources. The app uses a typographic EFZ Replay Lab
wordmark and existing source artwork; no image generation was used.

## Reviewed deployment

This release publishes source commit
[`7b29dd02b30e767fcb387459352f25382c0aec51`](https://github.com/Aquat1c/efz-replay-lab/commit/7b29dd02b30e767fcb387459352f25382c0aec51).
The release includes the city backdrop, sunset header, compact action and credits.
The public NOTICE.md contains concise credits and rights information. This latest
update changes only that notice in the deployed site.
The engine, battle media,175 NL illustrations and browser access bytes are unchanged.
The uploaded executable and decompilation are private static references and are
not included in the site or executed by it.

The final site has **665 files / 214,437,296 bytes**. The unchanged
nine base ZIP parts and sound/art overlay are reused. `game-faithful-overlay.zip`
contains the exact **203-file delta from the sound/art base**, is
**7,226,591 bytes**, and has SHA-256:

```
880e69d4314f3434dc895151437885b120d2c0095f528804e80029dfe14f2f1a
```

The final `site-sha256.txt` SHA-256 is:

```
c725b360507a38df937a2550f87eb8e666c835977337805ca5d73a3b56cab7c8
```

The pinned Actions workflow verifies the exact ordered parts, all archive
commitments, safe ZIP member sets, base/delta relationships and complete final
file hashes. Extra files, symlinks, traversal, changed bases and unexpected
overwrites are refused. Only that verified tree is uploaded to Pages.

## Evidence and remaining qualification

Prepublication source regression passed **1,211/1,211 tests**, with zero failures,
skips or cancellations;58 affected page/build tests passed after the final header
markup change. The exact candidate passed **19 shell interaction groups** and
**six city-background groups** in actual Chromium, including desktop/phone layouts,
reduced motion, fullscreen, replay independence, resource failure and the requested
credits. Independent code review found no critical or important issue. Evidence,
input identities and native spatial-rendering references are in the
[source qualification report](https://github.com/Aquat1c/efz-replay-lab/blob/7b29dd02b30e767fcb387459352f25382c0aec51/docs/qualification/CITY_BACKGROUND_2026-10-28.md).
Browser animation cadence is a presentation adaptation, not native timing parity.
The notice-only update was compared byte-for-byte: every other deployed file,
including the upstream license, is identical to that verified candidate.

This UI release was explicitly requested for publication. Its fresh browser evidence
uses labeled synthetic recordings. All 175 original NL illustrations were supplied
through the user's Drive folder and hash-verified. No original `.rep` was supplied
for this correction. Prior engine/native receipts retain their original scope;
native Windows parity, physical-device behavior, audibility and every matchup's
correctness are not established by these checks.

**T04 and portable local checkpoints remain unqualified/refused.** Exact restart
seeking does not qualify continuous startup/selection/loading/battle/results/rematch
restoration. No results or rematch lifecycle is fabricated.
