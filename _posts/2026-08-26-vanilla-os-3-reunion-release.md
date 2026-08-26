---
layout: post
title: "Vanilla OS 3 Reunion Released with ARM64 Support and GNOME 50"
categories: [vanillaos, linux, release]
tags: [vanillaos, gnome, arm64, immutable-linux, debian, release]
description: "Vanilla OS 3 Reunion is out with ARM64 support, Linux 7.1.3, GNOME 50 Tokyo, reproducible builds, and the new Vanilla Continuity backup tool."
image: /assets/images/post-images/vanilla-os-3-reunion-release.webp
---

The Vanilla OS team has released Vanilla OS 3 "Reunion", a major update to the Debian-based immutable Linux distribution. The release arrives roughly two years after [Vanilla OS 2 Orchid](/vanillaos-2-orchid-beta/), and delivers ARM64 support, a refreshed desktop, and several under-the-hood improvements.

![Vanilla OS 3 Reunion release](/assets/images/post-images/vanilla-os-3-reunion-release.webp)

Vanilla OS is an immutable operating system that uses ABRoot to maintain two system states — one active, one for updates — ensuring atomic, safe upgrades. Visit the [Vanilla OS distribution page](/distribution/vanillaos) for background on the project.

## ARM64 Support

The headline addition in Reunion is official ARM64 support for UEFI-compatible devices. All images are now multi-architecture, and every package ships ARM64 builds alongside the existing AMD64 builds. The team says the experience on ARM64 is identical to AMD64, with no compromises in functionality — opening the door to single-board computers, ARM-based laptops, and workstations.

## GNOME 50 "Tokyo" and Refreshed Apps

Reunion ships with GNOME 50 "Tokyo" on top of Linux kernel 7.1.3, using a Wayland-only session with improved fractional scaling.

The default application set has also changed:

- **Ptyxis** replaces Black Box as the default terminal, providing quick access to the host shell, the VSO shell, or any Apx subsystem
- **Papers** replaces Evince as the document viewer
- **Resources** replaces GNOME System Monitor
- File Roller and Photos are no longer installed by default

A new update mode in First Setup handles the app transition automatically after upgrading from Orchid, letting users confirm which new apps to install and which old ones to remove.

A community-designed wallpaper, "Fairy Tale" by Enner Kou, comes as the new default, available in both light and dark variants.

## Reproducible Builds

Most Vanilla OS images (NVIDIA images excluded due to kernel modules) are now fully reproducible — meaning the build process produces bit-for-bit identical images from the same sources. This allows anyone to independently verify that an image has not been modified, rather than relying solely on trust in GitHub Actions.

## Apx, VSO, and Distrobox v3

Both Apx and VSO (Vanilla System Operator) have been rewritten on top of a new Vanilla OS SDK. Key command changes include:

- `vso config set -k <key> -v <value>` is now `vso config set <key> <value>`
- `vso sys-upgrade upgrade` is now `vso upgrade`
- `vso pico-init` is now `vso native init`

Debian and openSUSE Leap join the default Apx stacks. The Apx GUI is now available on Flathub, making it accessible to all Linux users. The VSO image moves from Debian sid to Debian testing for better stability.

Reunion also ships Distrobox v2.0.0-rc.4, which has been rewritten in Go by the Distrobox team and validated for compatibility with Apx v3.

## Vanilla Continuity — Backup and Restore

Reunion introduces Vanilla Continuity, a snapshot-based backup and restore tool. It saves home directories, installed Flatpak app lists, and ABRoot metadata. Backups can go to a local directory, an external drive encrypted with LUKS2, or a remote server over SFTP, FTP, or NFS.

Basic usage:

```bash
host-shell pkexec continuity backup [backup-label]
host-shell pkexec continuity list
host-shell pkexec continuity restore <snapshot-id>
```

Continuity 1.0.0 is a command-line-only release for now.

## Upgrading from Vanilla OS 2 Orchid

Users on Vanilla OS 2 Orchid v1.4.0 can upgrade without a clean install. The upgrade will arrive as a normal system update, or can be triggered manually with `abroot upgrade`. Note that ABRoot 2.4.0 or later is required, as earlier versions do not support multi-architecture images.

For users still relying on the legacy `apx-vso-pico` subsystem, the team recommends upgrading packages inside the container before upgrading the host system. A workaround for systemd v261 compatibility is documented in the [official release notes](https://vanillaos.org/blog/article/2026-08-24/vanilla-os-3-reunion---stable-release).

## Download

Vanilla OS 3 Reunion is available for download from the [official Vanilla OS website](https://vanillaos.org). The installation documentation has also been updated with revised steps.