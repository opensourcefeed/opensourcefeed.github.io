---
layout: distribution
uid: cutefishos
title: 'CutefishOS'
Category: Distribution
type: Linux
permalink: /distribution/cutefish
logo: cutefishos.png
preview: cutefishos.jpg
home_page: https://cutefish.org/
desktops: [cutefish]
base : [debian]
tagline: A macOS-style Linux distribution, relaunched in 2026
image: /assets/images/preview/cutefishos.jpg

description : Cutefish (formerly CutefishOS) is a macOS-inspired Linux distribution built on Debian 13, relaunched in late 2026 with a new desktop, compositor and nightly ISOs for amd64 and arm64.

seo:
  type: OperatingSystem

releases:
  Cutefish 1.0 Nightly: https://cutefish.org/
  CutefishOS 0.8 Beta: /cutefishos-08-beta/
  CutefishOS 0.7 Beta: /cutefishos-07-beta-introduces-more-features-improvements/
  CutefishOS 0.6 Beta: /cutefish-os-0.6-release/
  CutefishOS 0.5 Beta: /cutefishos-0.5-release/

screenshots:
  CutefishOS 0.7: /cutefishos-07-beta-introduces-more-features-improvements/
  CutefishOS 0.6: /cutefish-os-0.6-release/

faq:
  Is CutefishOS still alive?: "Yes. After several years of inactivity, the project resumed development in 2026 and relaunched in November under the shorter name Cutefish, with a new website at cutefish.org and nightly ISO builds. No stable release has been announced yet."
  What is Cutefish based on?: "Early CutefishOS releases were based on Ubuntu and later Debian 11. The relaunched Cutefish nightly images are built on Debian 13 (Trixie), according to independent testing. The project's website does not state its base distribution."
  Is the new Cutefish the same project as the original CutefishOS?: "The relaunch is published from the same cutefishos GitHub organization, and the original maintainer has said that cutefish.org and that organization are the only official sources. Some community members questioned this in October 2026, so check the official channels before downloading."
  Does Cutefish still use Qt?: "No. The relaunched desktop uses its own compositor and a native C++ toolkit drawn with Skia, instead of the Qt-based stack used by earlier CutefishOS releases."
  Which architectures does Cutefish support?: "The official site lists amd64 and arm64 builds, with a nightly channel alongside the 1.0 listing."
  Can Cutefish run macOS apps?: "The project is writing its own versions of the frameworks Mac apps rely on. Apps such as Ghostty, CotEditor, NetNewsWire and Itsycal are reported to run on development builds. This is experimental, and it is not a general macOS compatibility layer."
---

**Cutefish**, formerly **CutefishOS**, is a Linux distribution for people who like the macOS way of working. It started in 2021 as a Debian-based system built around the [Cutefish desktop](/desktop/cutefish), went quiet, and returned in 2026 with a rebuilt desktop, a new website at [cutefish.org](https://cutefish.org/) and nightly ISO images.

## What happened to CutefishOS?

The original CutefishOS shipped several beta releases between 2021 and early 2022, from [0.5](/cutefishos-0.5-release/) to [0.8](/cutefishos-08-beta/). Development then stalled, and old repositories saw little activity for years. Third-party sites and community rebuilds, such as one based on Ubuntu 22.04, filled the gap, and the original project was widely considered abandoned.

In 2026 that changed:

- **August 2026**: commits resumed in the cutefishos GitHub organization.
- **October 2026**: the original maintainer, reionwong, stated in a GitHub issue that [cutefish.org](https://cutefish.org/) is the official website and that the cutefishos GitHub organization holds the only official source code. They added that no new ISO was planned at that time, and that cutefishos.com is not affiliated with the project.
- **November 2026**: the project relaunched as Cutefish, with a 1.0 entry and nightly builds for amd64 and arm64, and a release post covering 17 languages, a Preview app and software updates.

Reports from independent outlets note that the community debated who controls the relaunch, since the maintainer's October statement and the later nightly ISOs sit awkwardly together. Treat cutefish.org and the official GitHub organization as the reference points, and be cautious with downloads from anywhere else.

<!-- VERIFY: exact relaunch date and 1.0 release status. cutefish.org lists "1.0" plus a Nightly build, but independent testing in Nov 2026 found no stable release. -->

## What is new in Cutefish?

The relaunched project is a rewrite more than an update:

- **Own desktop stack**: the desktop shell, compositor and bundled apps are developed by the project. The toolkit is native C++ drawn with Skia, rather than Qt as in earlier versions.
- **Performance targets**: the site claims under 1 GB of memory in use after login and roughly 0.1 seconds from click to window for bundled apps. Independent testing of a November 2026 nightly measured about 817 MB of RAM at idle.
- **Mac app compatibility work**: the project is implementing its own versions of frameworks that Mac apps use. Ghostty, CotEditor, NetNewsWire and Itsycal are reported to run on development builds. This is experimental.
- **AI agent control**: a bundled MCP server lets agents such as Claude Code or Codex see the screen and control input through the compositor. Users must consent first, a Stop button stays in the status bar, and agents pause when the user touches the mouse or keyboard.
- **Traceable builds**: the desktop and ISO are built by a public GitHub Actions workflow, and packages are signed by that workflow.

## Installing Cutefish

- **Nightly ISO**: download from [download.cutefish.org](https://download.cutefish.org). Independent testing found the amd64 image to be about 1.6 GB, installable on UEFI systems with Secure Boot enabled. The installer uses the whole disk, so back up your data first.
- **APT repository**: on an existing Debian 13 system, the nightly repository can provide the desktop package. See the official instructions before adding it.
- **From source**: build instructions are in the [getting-started repository](https://github.com/cutefishos/getting-started).

Since only nightly builds are available, expect rough edges. Test in a virtual machine before committing a main computer. At least 4 GB of RAM is a sensible minimum for real use.

<!-- VERIFY: license of the relaunched code is not stated on cutefish.org. -->

## Who is Cutefish for?

- Users coming from macOS who want a similar layout, dock and global menu on Linux.
- Enthusiasts who want to follow a young desktop project and are comfortable with nightly software.
- Developers curious about running Mac-style apps, or about agent-controlled desktops, on Linux.

If you need a stable daily driver today, a mature distribution with a similar look may be safer, such as [Debian](/distribution/debian)-based systems running a macOS-style theme, or see the [Cutefish desktop](/desktop/cutefish) page for other ways to try the desktop.

Cutefish is an independent project and is not affiliated with or endorsed by Apple.

## Screenshots

Images from the project's official site, showing the 2026 desktop with its dock, bundled apps and the consent prompt for AI agent control.

{% include image-gallery.html folder="/screenshots/Cutefish 2026" %}
