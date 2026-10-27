# EFZ replay player

Experimental browser playback for the supported Eternal Fighter Zero Revival recordings.

## Use

Open this repository's GitHub Pages website. Select a supported local `.rep` file, enter the separately supplied resource key, and press **Open replay**, then **Play**. The recording stays in your browser. The player also provides Pause, Step and stage-music volume controls.

The supported profile is Nayuki A versus Akiko (characters 17/16), stage 17, palettes 0/0, normal two-win battles and zero auxiliary-command high bytes. Unsupported recordings are rejected. Battle intros run; menus are skipped. Effect and voice audio is absent.

## Deployment contents

This repository contains the prepared static player, required source notices and encrypted resources in `replay-site.zip`. Its 28 files total 21,922,257 bytes before ZIP compression. The workflow verifies the ZIP digest and every extracted file before publishing the extracted site.

The matching resource key is supplied separately. It is not a repository secret or a workflow input. Keep it out of Git, URLs and logs. Encryption protects stored and transferred resource bytes; a viewer with the key can recover the resources they load.

This is an experimental replay player. T04 service resume remains unimplemented and unqualified. The supplied separate battle recordings do not qualify a continuous startup, selection, loading, results and rematch session. Artifact checks and a successful web deployment do not establish Windows-native parity or complete session correctness.

The packaged `NOTICE.md` and `public/upstream-license.txt` retain the applicable source notices. This repository does not relicense third-party code or game resources.

## Publishing

In repository Settings, select **Pages → Source → GitHub Actions**. The workflow runs on pushes to `main` and can also be started manually. It needs no custom token or resource key.

When replacing the package, review its exact contents and update both digest files. Only the extracted static artifact is published.
