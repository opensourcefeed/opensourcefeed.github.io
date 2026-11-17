---
layout: desktop
uid: cutefish
title: 'Cutefish Desktop'
Category: Desktop
permalink: /desktop/cutefish
logo: cutefishos.svg
preview: cutefish-desktop.jpg
home_page: https://cutefish.org/
description: The Cutefish desktop is a macOS-inspired Linux desktop, rebuilt in 2026 with its own Wayland compositor, a native C++ toolkit drawn with Skia, and bundled apps.
tagline: Desktop like macOS
image: /assets/images/preview/cutefish-desktop.jpg
---

**The** Cutefish desktop is a macOS-inspired desktop environment for Linux. It is the flagship of the [CutefishOS](/distribution/cutefish) project, which relaunched in 2026 as simply Cutefish.

## A rebuilt desktop

The 2021 version of the desktop was built on Qt and KDE technologies. The 2026 relaunch replaces that foundation. According to the project, the desktop shell, compositor and apps are all its own, with a native C++ toolkit drawn with Skia. The site states under 1 GB of memory in use after login.

## Features

- **macOS-style layout**: a top status bar, a dock and a launcher, aimed at people coming from macOS.
- **Bundled apps**: a set of first-party apps, including a Preview app and software updates, with the interface available in 17 languages.
- **Mac app compatibility (experimental)**: the project is writing its own versions of frameworks that Mac apps use. Ghostty, CotEditor, NetNewsWire and Itsycal are reported to run on development builds.
- **AI agent control**: agents that speak MCP, such as Claude Code or Codex, can view the screen and control input through the compositor, with user consent, a Stop button and automatic pause on user input.
- **Verifiable builds**: desktop packages and ISOs are built and signed by a public GitHub Actions workflow.

## How to get it

- Use the Cutefish nightly ISO from [download.cutefish.org](https://download.cutefish.org), built on Debian 13 and available for amd64 and arm64.
- Build from source with the [getting-started repository](https://github.com/cutefishos/getting-started).
- Older CutefishOS releases also made the desktop available on Ubuntu and Arch/Manjaro, such as [Manjaro Cutefish](/manjaro-cutefish/). Those packages date from the previous Qt-based desktop and may not reflect the 2026 rewrite.

<!-- VERIFY: whether the rewritten desktop is packaged for distributions other than Debian 13. -->

Only nightly builds are available at the moment, so expect changes. Cutefish is independent and not affiliated with Apple.

## Screenshots

Images from the project's official site, showing the 2026 desktop with its dock, bundled apps and the consent prompt for AI agent control.

{% include image-gallery.html folder="/screenshots/Cutefish 2026" %}
