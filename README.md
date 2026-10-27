# EFZ replay player

Experimental browser playback for supported Eternal Fighter Zero Revival recordings.

## Use

[Open the replay player](https://qtc123123.github.io/efz-replay-pages/public/replay.html).
Select a supported local `.rep` file and press **Open replay**, then **Play**. No resource key or game installation is required. Your recording stays in your browser. Pause, Step and stage-music volume controls are available.

The supported profile is Nayuki A versus Akiko (characters 17/16), stage 17, palettes 0/0, normal two-win battles and zero auxiliary-command high bytes. Unsupported recordings are rejected. Battle intros run; menus are skipped. Effect and voice audio is absent.

## Deployment contents

This repository contains the prepared static player, source notices and encrypted resources in `replay-site.zip`. Its 29 files total 21,924,145 bytes before ZIP compression. The workflow verifies the archive digest and every extracted file before publishing the site.

Resources are decrypted automatically in the browser using a generated, obfuscated access module bound to the resource manifest. The original key file and plaintext resource files are not included. The obfuscation deters casual extraction; it is not a secrecy or copy-prevention guarantee.

This is an experimental replay player. T04 service resume remains unimplemented and unqualified. The separate battle recordings do not qualify a continuous startup, selection, loading, results and rematch session. Artifact checks and a successful deployment do not establish Windows-native parity or complete session correctness.

The packaged `NOTICE.md` and `public/upstream-license.txt` preserve the original source notices. Some NOTICE paths describe the earlier private development layout and are historical references, not public links. This repository does not relicense third-party code or game resources.

## Publishing

In repository Settings, select **Pages → Source → GitHub Actions**. The workflow runs on pushes to `main` and can also be started manually. It needs no custom token or resource-key secret.

When replacing the package, review its exact contents and update both digest files and the workflow's expected file count. Only the extracted static artifact is published.

