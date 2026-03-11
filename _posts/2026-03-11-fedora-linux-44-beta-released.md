---
layout: post
title: "Fedora Linux 44 Beta Released: KDE Overhaul, Nix Support, and Reproducible Builds"
categories: [fedora, linux, release]
tags: [fedora, fedora-44, beta, linux, kde, gnome, release]
description: "Fedora Linux 44 Beta is now available with a unified KDE out-of-the-box setup, Budgie migrating to Wayland, Nix package manager support, and a push toward 99% reproducible builds."
image: /assets/images/post-images/fedora/fedora-44-beta.jpg
---

**The** Fedora Project announced the availability of Fedora Linux 44 Beta on March 10, 2026. This beta is an open invitation for users and contributors to test the release before it reaches its final form. Your feedback shapes the quality of the final release.

![Fedora Linux 44 Beta release banner with the Fedora logo on a dark background and the text Fedora Linux 44](/assets/images/post-images/fedora/fedora-44-beta.jpg)

## Download Fedora Linux 44 Beta

The beta is available across all major Fedora editions:

- [Fedora Workstation 44 Beta](https://fedoraproject.org/workstation/download/?beta)
- [Fedora KDE Plasma Desktop 44 Beta](https://fedoraproject.org/kde/download/?beta)
- [Fedora Server 44 Beta](https://fedoraproject.org/server/download/?beta)
- [Fedora IoT 44 Beta](https://fedoraproject.org/iot/download/?beta)
- [Fedora Cloud 44 Beta](https://fedoraproject.org/cloud/download/?beta)

Fedora CoreOS "next" stream will move to this beta one week later. The branched stream already carries F44 content. Existing Fedora systems can upgrade via [DNF system-upgrade](https://docs.fedoraproject.org/en-US/quick-docs/upgrading-fedora-offline/).

## What's New in Fedora Linux 44

### Installer and Desktop Changes

**Cleaner Anaconda Network Profiles**
Anaconda now only creates network profiles for devices you actually configure during installation. Previously, it created profiles for all detected devices, which caused headaches when reconfiguring them after install. This change cleans that up.

**Unified KDE First-Run Setup**
Fedora KDE variants now ship with the post-install Plasma Setup application. This gives users a consistent out-of-the-box experience. Anaconda's configuration for KDE has been adjusted to skip setup steps that would duplicate what the new application already handles.

**Plasma Login Manager Replaces SDDM**
Fedora KDE now uses the Plasma Login Manager (PLM) as its default display manager instead of SDDM.

**Games Lab Switches to KDE Plasma**
The Fedora Games Lab has been modernized. It now uses KDE Plasma instead of Xfce to take advantage of the improved Wayland stack for gaming.

**Budgie 10.10 Moves to Wayland**
Budgie Desktop 10.10 drops X11 in favor of Wayland. This secures a long-term path for Budgie users and sets the foundation for the next major Budgie release.


### Live Media Improvements

**ARM Laptop Support for aarch64 ISO**
The aarch64 Fedora Live ISO images will now automatically select the correct DTB at boot on Windows on ARM (WoA) laptops, enabling them to work without manual configuration.

**USB Persistent Overlays**
The live media experience has been updated with new livesys-scripts and improved dracut support. When you flash the ISO to a USB stick, it can now automatically enable persistent overlays to save your changes across reboots.


### System Enhancements

**GNU Toolchain Update**
Fedora 44 ships with updated versions of gcc, glibc, binutils, and gdb, keeping the distribution current with upstream security and feature updates.

**Reproducible Package Builds Target: 99%**
Over several releases, Fedora has been working toward fully reproducible package builds. Fedora 44 targets no fewer than 99% of all package builds being reproducible. Bugs will be filed against any package that fails this check.

**Nix Package Manager Added**
Fedora 44 introduces the Nix package manager as a developer tool. This makes it easier for developers who rely on Nix-based workflows to use Fedora as their primary system.

**Packit as Default CI for dist-git**
Fedora continues to modernize its CI pipeline by completing the integration of Packit as the default CI system for Fedora dist-git.

**Python Mock Cleanup**
`python-mock` was deprecated in Fedora 34. Fedora 44 pushes through the remaining cleanup of packages still using it, with the goal of retiring the package entirely.

**Hardlinking Identical Files**
All Fedora packages now automatically hardlink identical files under `/usr` after installation. This reduces disk usage and addresses reproducibility edge cases caused by race conditions in older hardlinking approaches.


### Package and Toolchain Updates

| Package | Update |
|---|---|
| Golang | 1.26 |
| MariaDB | 11.8 (new distribution default) |
| IBus | 1.5.34 (better Wayland and Emoji support) |
| Django | 6.x (with python3-django5 available for compatibility) |
| TagLib | 2 |
| Helm | 4 (Helm 3 remains available as `helm3`) |
| Ansible | 13 / Ansible Core 2.20 |
| TeXLive | 2025 (with modularized packaging) |

**Note on Ansible 13:** This update includes significant fixes to the templating engine. Some existing playbooks with incorrect behavior that was silently ignored may break. Review your playbooks before upgrading.


### Removals

- **QEMU 32-bit host builds** are dropped from i686, in line with upstream QEMU's deprecation of 32-bit host support.
- **FUSE 2** binaries and libraries are removed from all Atomic Desktops.
- **pkla polkit rules** support is removed from all Fedora Atomic Desktops.


## How to Help

Testing the beta is the most direct way to contribute to Fedora 44. Install it, use it, and report any issues you find. The full list of changes is on the [Fedora 44 ChangeSet](https://fedoraproject.org/wiki/Releases/44/ChangeSet) page.

For more information, see the [official announcement on Fedora Magazine](https://fedoramagazine.org/announcing-fedora-linux-44-beta/).