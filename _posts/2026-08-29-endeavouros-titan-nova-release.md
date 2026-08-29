---
layout: post
title: "EndeavourOS Titan Nova Released: Hardware Updates and Bug Fixes"
categories: [endeavour, arch, release]
tags: [endeavouros, arch-linux, rolling-release, linux, titan-nova]
description: "EndeavourOS Titan Nova is out with Linux 7.1.8, Mesa 26.1.7, Nvidia 610, keyboard fixes, and improved Nouveau support, bridging to the upcoming Triton release."
image: /assets/images/post-images/endeavouros/titan-nova-release.webp
---

**EndeavourOS** has released Titan Nova, a mid-cycle update to the Titan series. The release serves as a bridge while the team works toward the next major release, Triton. Titan Nova does not introduce major new features — the focus is on hardware support updates, component upgrades, and a handful of targeted bug fixes.

As with all EndeavourOS ISO releases, existing users do not need to reinstall. If you keep your system updated regularly, your packages are already current. Titan Nova's changes apply to the Calamares installer, the offline installer, and the live environment only. You can read about the previous release in our [EndeavourOS Titan release coverage](https://www.opensourcefeed.org/endeavouros-titan-release/).

![Endeavour OS Titan Nova release banner](/assets/images/post-images/endeavouros/titan-nova-release.webp)

## What Ships With Titan Nova

The live environment and offline installer include the following updated components:

- **Calamares** 26.03.2.3-1
- **Firefox** 153.0.4-1
- **Linux kernel** 7.1.8.arch1-3
- **Mesa** 1:26.1.7-1
- **Xorg-server** 21.1.24-1
- **Nvidia-utils** 610.57.04-1
- **Nvidia-open** 610.54.01-6

## Bug Fixes and Changes

**Keyboard setup fix:** A recent upstream change in keyboard configuration caused setup errors during installation. A temporary patch is in place and the team plans a permanent fix in the Triton release.

**Improved Nouveau support:** The experience on the live ISO when using Nouveau drivers for NVIDIA GPUs has been improved.

**Budgie desktop removed:** Budgie has been temporarily pulled from the installer options. The upstream project is in transition to Wayland, and the current state does not meet the team's standards for a default experience. It is expected to return in a future release.

## The Road to Triton

The team had originally hoped to ship Triton by now, but the move to Wayland for the live environment — driven by upcoming changes in the Plasma desktop — has proven more complex than expected. Titan Nova gives the team more time to complete that work without leaving the current ISO stale.

For reference, EndeavourOS follows a rolling release model. The ISO is refreshed periodically to keep the installer and live environment current. This [overview of EndeavourOS](https://www.opensourcefeed.org/distribution/endeavour) covers how the project works for those new to the distribution. If you're curious how Titan Nova compares to earlier refreshes, take a look at our [EndeavourOS Ganymede release notes](https://www.opensourcefeed.org/endeavouros-ganymede-release/) for context on how the project has evolved.

You can download Titan Nova or grab the torrent and magnet files from the [official EndeavourOS website](https://endeavouros.com/news/titan-nova-is-available/).
