---
layout: post
title: "Ubuntu 26.10 Beta Released: Linux 7.3 and GNOME 51"
categories: [ubuntu, linux, release]
tags: [ubuntu, ubuntu-26-10, beta, stonking-stingray, gnome-51, rust, linux-kernel]
description: "The Ubuntu 26.10 beta is out with Linux 7.3 RC, GNOME 51, and Rust coreutils. See what is new and get beta images for all ten official flavors."
image: /assets/images/post-images/ubuntu/ubuntu-26-10-beta-released.webp
---

**Canonical** has released the Ubuntu 26.10 beta, the last public test build before the final release on October 15, 2026. Codenamed *Stonking Stingray*, the beta arrived on October 1 for Ubuntu Desktop, Server, WSL, and Cloud, along with ten official flavors.

![Ubuntu 26.10 Stonking Stingray featured image](/assets/images/post-images/ubuntu/ubuntu-26-10-beta-released.webp)

## Ubuntu 26.10 beta release date and schedule

The beta was due on September 24. The Ubuntu release team moved it to October 1 because of infrastructure problems. Canonical said the delay would not change the final release date, so testers have about two weeks before October 15.

Ubuntu 26.10 is an interim release. It gets nine months of support, until July 2027.

## What is new in the Ubuntu 26.10 beta

### Linux 7.3 and GNOME 51

The beta images use a Linux 7.3 release candidate kernel. Canonical plans to ship Linux 7.3 in the final release. The desktop moves to GNOME 51, and the graphics stack is based on Mesa 26.2.

### 100% Rust coreutils

The default core utilities now run on the Rust-based `uutils` project. The last GNU tools that Ubuntu kept, `cp`, `mv`, and `rm`, have now moved over as well. This makes 26.10 the first Ubuntu release with a fully Rust coreutils package.

### dbus-broker replaces dbus-daemon

Ubuntu 26.10 switches its default D-Bus implementation from `dbus-daemon` to `dbus-broker`.

### Sequoia PGP

Ubuntu has added Sequoia PGP, a memory-safe OpenPGP implementation written in Rust, to the main archive. The goal is to make its `sq` and `sqv` tools the counterparts of `gpg` and `gpgv`. Both `gpg` and `gpgv` remain in the main repository for now.

### OpenSSH split on Ubuntu Server

Ubuntu Server splits OpenSSH into two source packages, `openssh` and `openssh-gssapi`. The first builds without GSSAPI and Kerberos support, which reduces the attack surface. Fresh installs use the non-GSSAPI packages. The release upgrader picks the GSSAPI packages if it detects that you use Kerberos with OpenSSH.

### RISC-V support

Ubuntu 26.10 adds official support for RVA23 RISC-V hardware, including the SpacemiT K3 boards and the SiFive BigSky platform. Ubuntu Desktop and Xubuntu Minimal RISC-V images support the SpacemiT K3 and QEMU.

## Ubuntu 26.10 beta flavors

All ten official Ubuntu flavors have beta images. The release announcement describes them as follows:

| Flavor | Desktop or focus | Beta download |
|--------|------------------|---------------|
| Edubuntu | Education-focused system for children of all ages | [Edubuntu beta](https://cdimage.ubuntu.com/edubuntu/releases/26.10/beta/) |
| Kubuntu | KDE Plasma desktop with KDE tools | [Kubuntu beta](https://cdimage.ubuntu.com/kubuntu/releases/26.10/beta/) |
| Lubuntu | Lightweight LXQt desktop | [Lubuntu beta](https://cdimage.ubuntu.com/lubuntu/releases/26.10/beta/) |
| Ubuntu Budgie | Budgie desktop, community developed | [Ubuntu Budgie beta](https://cdimage.ubuntu.com/ubuntu-budgie/releases/26.10/beta/) |
| Ubuntu Cinnamon | Cinnamon desktop | [Ubuntu Cinnamon beta](https://cdimage.ubuntu.com/ubuntucinnamon/releases/26.10/beta/) |
| UbuntuKylin | Aimed at Chinese users | [UbuntuKylin beta](https://cdimage.ubuntu.com/ubuntukylin/releases/26.10/beta/) |
| Ubuntu MATE | MATE desktop | [Ubuntu MATE beta](https://cdimage.ubuntu.com/ubuntu-mate/releases/26.10/beta/) |
| Ubuntu Studio | Audio, graphics, video, photo, and publishing tools | [Ubuntu Studio beta](https://cdimage.ubuntu.com/ubuntustudio/releases/26.10/beta/) |
| Ubuntu Unity | Unity7 desktop | [Ubuntu Unity beta](https://cdimage.ubuntu.com/ubuntu-unity/releases/26.10/beta/) |
| Xubuntu | Xfce desktop, light and configurable | [Xubuntu beta](https://cdimage.ubuntu.com/xubuntu/releases/26.10/beta/) |

## How to download the Ubuntu 26.10 beta

- **Ubuntu Desktop, Server, and WSL (x86):** [releases.ubuntu.com/26.10](https://releases.ubuntu.com/26.10/)
- **Non-x86 images:** [cdimage.ubuntu.com/releases/26.10/beta](https://cdimage.ubuntu.com/releases/26.10/beta/)
- **Cloud images:** the [daily Cloud images](https://cloud-images.ubuntu.com/daily/server/stonking/current/). Use a build with serial 20261001 or higher.

If you run Ubuntu 26.04 LTS, Canonical has a [guide to upgrade Ubuntu Desktop](https://documentation.ubuntu.com/desktop/en/latest/how-to/upgrade-ubuntu-desktop/) to the beta.

## Should you install the beta?

The release team says the beta images are reasonably free of showstopper bugs in the image build and the installer. They are still test builds. Use a virtual machine, a spare drive, or a test machine, and keep your production systems on a stable release. Report any bugs you find through the [Ubuntu bug reporting guide](https://documentation.ubuntu.com/project/contributors/qa-and-testing/report-a-bug/).

Canonical will publish the final Ubuntu 26.10 on October 15, 2026. The release notes are still a work in progress, so details may change before then.

## Sources

- [Ubuntu 26.10 (Stonking Stingray) Beta released](https://lists.ubuntu.com/archives/ubuntu-announce/2026-October/000329.html), ubuntu-announce
- [Ubuntu 26.10 release notes](https://documentation.ubuntu.com/release-notes/26.10/), Canonical
- [Ubuntu 26.10 beta delay](https://www.omgubuntu.co.uk/2026/09/ubuntu-2610-beta-release-delay), OMG! Ubuntu
- [Ubuntu 26.10 Beta Lands With Linux Kernel 7.3-rc and GNOME 51](https://linuxiac.com/ubuntu-26-10-beta-lands-with-linux-kernel-7-3-rc-and-gnome-51/), Linuxiac
