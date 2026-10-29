# EFZ Replay Lab

[Open EFZ Replay Lab](https://qtc123123.github.io/efz-replay-pages/)

Watch Eternal Fighter Zero native and Revival replays in your browser, with game audio,
recorded inputs and optional hitboxes. No game installation is needed.

## Watch a replay

1. Choose **Add files or archives**, **Add folder**, or **Open replay**. Select `.rep`, ZIP, RAR or 7z files. Your recordings stay in your browser.
2. Wait for the game and audio to load. The player pauses on the first game image.
3. Press **Play**.

If the match used a different win target, select it in **Replay settings** before
opening the file. Recordings do not store this setting; the initial default is two wins.
Changing it reloads the replay.

## Local playlist

Folders and nested archives appear above replay cards. Each card shows original
character-selection artwork, duration when available, then a Vanilla/Revival badge.
Native duration is `-` until the recording is opened; bulk import never simulates
all native matches. Empty `.rep` entries are omitted. Archive contents stay as metadata until selected;
selected recordings share a bounded 64 MiB cache. Original archives remain local.
Recognizable filenames supply player names and recorded dates. Card backgrounds
use softly blurred original stage artwork.

Use previous/next recording controls or enable **Auto-advance** (off by default).
Cards can be reordered or removed. Imports can be cancelled without losing the
entries already admitted. Search and pagination keep large packs navigable.
The library is session-only: choose the files again after reloading.

Limits: 128 MiB per archive, 64 MiB per replay, four nested archives below the
outer archive, 20,000 visited entries, 20,000 playlist entries, 4 GiB expanded-work budget and 64 MiB selected-replay
cache and a 120-second import timeout. Password-protected,
multipart and self-extracting archives are not supported. Partial errors are
shown without discarding other accepted recordings.

Archive decoding uses pinned libarchive.js/libarchive WASM with local hardening.
[Decoder notices and provenance](https://qtc123123.github.io/efz-replay-pages/vendor/libarchive/PROVENANCE.md).

Solid archives may need to decode earlier data when a replay is selected. Use
**Cancel extraction** to stop waiting. Recordings can end without a KO; the player
reports **Recording ended**. Recorded F4/F5/Escape commands are supported in local
Revival playback; unqualified command bits still produce an explicit error.

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

The player supports native EFZ recordings and current/older Revival paired-input
recordings, all 25 characters,
23 stages, six palettes and win targets of one to three rounds. Files are limited
to 64 MiB and 1,000,000 game frames. Unsupported or incomplete files show an error.
Native recordings are scanned before playback. Recordings that run out of data
before a complete finish are rejected without inventing inputs. Native tapes do
not provide the separate recorded-input history available in paired recordings.
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
