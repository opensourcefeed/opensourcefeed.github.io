---
layout: post
title: "Kali Linux 2026.1 Released: New Theme, BackTrack Mode, and 8 New Tools"
categories: [kali, linux, release]
tags: [kali-linux, penetration-testing, ethical-hacking, backtrack, nethunter, security]
description: "Kali Linux 2026.1 is out with a 2026 theme refresh, BackTrack mode for kali-undercover, 8 new security tools, and NetHunter improvements."
image: /assets/images/post-images/kali/kali-linux-2026-1-release.jpg
seo:
  type: DesktopEnvironment
---

The Kali Linux team has released Kali Linux 2026.1, the first update of the year. This release brings a fresh visual theme, a nostalgic nod to BackTrack Linux, eight new tools, and several NetHunter improvements.

![Kali Linux 2026.1 desktop with the new 2026 theme refresh](/assets/images/post-images/kali/kali-linux-2026-1-release.jpg)

Building on [Kali Linux 2025.4](https://www.opensourcefeed.org/kali-linux-2025-4-released/), this release continues the tradition of a yearly theme overhaul alongside practical improvements for security professionals.

## 2026 Theme Refresh

Every `.1` release gets a full visual refresh, and 2026.1 is no exception. The new theme covers the boot animation, GRUB boot menu, graphical installer, login screen, and desktop wallpapers. The boot animation also received a fix — it no longer gets stuck on live images and now loops correctly if the boot process takes longer than expected.

## BackTrack Mode for Kali-Undercover

2026 marks the 20th anniversary of BackTrack Linux, the predecessor to Kali. To mark the occasion, the team has added a "BackTrack mode" to the `kali-undercover` tool. Running `kali-undercover --backtrack` transforms the desktop to look and feel like BackTrack 5, complete with the original wallpaper, colors, and window themes. Running it again returns you to the standard Kali desktop.

This is a fun tribute for longtime users of the platform. If you're new to Kali's history, the [Kali Linux history page](https://www.kali.org/docs/introduction/kali-linux-history/) gives a good overview of how BackTrack evolved into what Kali is today.

## New Tools in Kali 2026.1

Eight new tools have been added to the Kali network repositories:

- **AdaptixC2** — Extensible post-exploitation and adversarial emulation framework
- **Atomic-Operator** — Execute Atomic Red Team tests across multiple OS environments
- **Fluxion** — Security auditing and social-engineering research tool
- **GEF** — Modern GDB extension with advanced debugging capabilities
- **MetasploitMCP** — MCP server for Metasploit
- **SSTImap** — Automatic SSTI detection tool with interactive interface
- **WPProbe** — Fast WordPress plugin enumeration tool
- **XSStrike** — Advanced XSS scanner

In total, this release includes 25 new packages, 9 removals, and 183 updates. The kernel has been bumped to version 6.18.

## Kali NetHunter Updates

The [Kali NetHunter](https://nethunter.kali.org/) app received several bug fixes, including a WPS scan bug, HID permission check issue, and a back button problem. The Redmi Note 8 (Ginkgo) now has a new kernel for Android 16. The Samsung S10 series also gained improved internal wireless support, bringing working monitor mode and injection to tools like reaver, bully, and kismet.

On the wireless side, the first working packet injection patch for QCACLD-3.0 has landed, which could unlock injection support for a wide range of Qualcomm-based Android devices.

## Known Issues

Users of the `kali-tools-sdr` metapackage (Software Defined Radio) should be aware that the GNU Radio ecosystem is broken in this release. Tools like `gr-air-modes` and `gqrx-sdr` are affected. A fix is expected in the next release.

## Updating or Installing

Existing users can update with:

```bash
echo "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
sudo apt update && sudo apt -y full-upgrade
cp -vrbi /etc/skel/. ~/
[ -f /var/run/reboot-required ] && sudo reboot -f
```

Fresh images are available on the [Kali Linux download page](https://www.kali.org/get-kali/). Weekly builds are also available if you want the latest packages before the next stable release.

For the full changelog, see the [official Kali Linux 2026.1 release announcement](https://www.kali.org/blog/kali-linux-2026-1-release/).