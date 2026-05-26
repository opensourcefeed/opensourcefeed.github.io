---
layout: post
title: "MX Linux 25.2 Released: Text-Mode Installer, Debian 13.5, and Linux 7.0 AHS"
categories: [mx, debian, release]
tags: [mxlinux, mx-linux-25, debian-trixie, release, linux]
description: "MX Linux 25.2 'Infinity' is out with a new text-mode installer, Debian 13.5 base, Linux 6.12 LTS, and a Liquorix 7.0 kernel on AHS builds."
image: /assets/images/post-images/mx/mx-25-2-release.webp
---

**The** MX Linux team has released MX Linux 25.2, the second ISO refresh in the MX 25 "Infinity" series. Coming four months after MX Linux 25.1, this update brings a Debian 13.5 base, kernel updates, and a notable new text-mode installer — all without requiring a reinstall for existing users.

![MX Linux 25.2 'Infinity' released with a text-mode installer, Debian 13.5 base, Linux 6.12 LTS, and a Liquorix 7.0 kernel on AHS builds.](/assets/images/post-images/mx/mx-25-2-release.webp)

MX 25.2 builds on the foundation of [MX Linux 25 "Infinity"](https://www.opensourcefeed.org/mx-linux-25-infinity-released/), which moved the series to Debian 13 Trixie and adopted systemd as the default init system.

## What's New in MX Linux 25.2

**Kernel updates**

All standard ISOs ship with the updated Debian 6.12.90 kernel. The Xfce AHS (Advanced Hardware Support) edition uses a Liquorix-flavored Linux 7.0.9 kernel for users who need support for the latest hardware. AHS-enabled builds also include Mesa 26.0.1, providing a more current graphics stack out of the box.

**New text-mode installer**

The standout addition in MX Linux 25.2 is a text-based installer mode. Running `minstall-launcher` in a text console now opens a full TUI (terminal user interface) with all the features of the graphical installer — useful when graphics hardware, display drivers, or resource constraints make a GUI impractical. You can also invoke it directly from a terminal emulator with `sudo minstall --tui`.

**Microcode-enabled live systems**

MX Snapshot and live-kernel-updater now generate microcode-enabled live systems when the optional `uc-tool-mx` package is installed. The package is available in the standard repository.

**Improved rescue and live tooling**

The chroot-rescue-scan script now handles Btrfs and encrypted partitions better. There are also new init service files for the live system and improved support for pre-Sandy Bridge Intel graphics in live sessions.

**MX Tools and cosmetics**

This release includes a range of mx-tool updates, updates to mx-ease-themes, and a couple of new wallpapers.

**Raspberry Pi Respin returns**

The Raspberry Pi Respin is back with MX 25.2 after an absence in the previous refresh.

## Upgrade and Download

Existing MX Linux 25 users do not need to reinstall. All updates come through the regular update channel. The new ISOs are mainly useful for fresh installs and live USB use.

MX 25.2 is available in Xfce, KDE Plasma, and Fluxbox editions — including AHS and SysVinit variants. For download links and full changelog, see the [official release announcement](https://mxlinux.org/blog/mx-25-2-infinity-isos-now-available/).

If you're coming from an older branch, the [MX Linux 23.2 Libretto release notes](https://www.opensourcefeed.org/mx-232-release/) offer useful context on how the series has evolved over recent cycles.