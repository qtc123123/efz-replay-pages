# EFZ Replay Lab

[Open EFZ Replay Lab](https://qtc123123.github.io/efz-replay-pages/)

Watch Eternal Fighter Zero Revival replays in your browser, with game audio,
recorded inputs and optional hitboxes. No game installation is needed.

## Watch a replay

1. Choose **Open replay** and select a `.rep` file. Your recording stays in your browser.
2. Wait for the game and audio to load. The player pauses on the first game image.
3. Press **Play**.

If the match used a different win target, select it in **Replay settings** before
opening the file. Recordings do not store this setting; the initial default is two wins.
Changing it reloads the replay.

## Controls

Tap or click the game image to show or hide the controls. During playback they
hide after **1 second** of inactivity. Open menus and held controls keep them visible.

- Drag the timeline to seek. Longer seeks may take a few seconds and can be cancelled.
- Restart returns to the first gameplay frame and pauses there.
- Open **Sound** to mute audio or adjust music and effects separately.
- Enable **Voice mod** in Sound for the optional replacement voices. Original
  game sounds are used by default; both sets load before playback.
- Choose **EN / 日本語** for the interface and in-game artwork. Changing language
  keeps your replay position.
- Open **Settings** for hitboxes, recorded inputs, match details and frame stepping.
- Enable **Keep playing in background** in Settings to continue when switching
  tabs or windows. It is off by default.
- Recorded inputs appear on each player's side, with the number of frames held
  before each direction or button. Empty rows count frames with no input.

| Key | Action |
| --- | --- |
| Space | Play / pause |
| Right Arrow | Step forward while paused |
| Left Arrow | Step back while paused |
| Home | Restart while paused |
| F | Toggle fullscreen |
| Escape | Close a menu, cancel a seek or leave fullscreen |

Seeking and stepping are silent. Audio resumes with playback. Leaving the player
pauses it; returning keeps your place without starting playback automatically.
Music keeps its position through pauses and seeks; restarting the replay restarts
the track.

Your player settings are remembered in this browser, including volumes, mute,
overlays, the win target, background playback, language and Voice mod.

## Supported recordings

The player supports EFZ Revival paired-input recordings, all 25 characters,
23 stages, six palettes and win targets of one to three rounds. Files are limited
to 64 MiB and 1,000,000 game frames. Unsupported or incomplete files show an error.
Compatibility with every recording or gameplay modification is not guaranteed.

**Live spectating is not available yet.** The Watch page will need a connected
spectator service before it can show sessions.

## Credits

- Site, Netplay support and Engine modification by **Aquatic**.
- Original web engine by **Mu-Tsun Tsai**.
- English translation by **SaltyBucket & fishshapedfish**.
- Original voiceover source: **Key/Tactics**.
- Game created by **Twilight Frontier**, all rights reserved.
- Original visual novels: **Key** (Kanon / AIR), **NEXTONE** (MOON. / ONE).

This site is not affiliated with Twilight Frontier, Key or NEXTONE.
See the [credits and notices](https://qtc123123.github.io/efz-replay-pages/NOTICE.md)
and [original engine license](https://qtc123123.github.io/efz-replay-pages/public/upstream-license.txt).
