---
layout: post
title: "Solus 4.9 Serenity Released: Linux 6.18, LUKS2, and Wayland Transition"
categories: [solus, linux, release]
tags: [solus, solus-4, budgie, gnome, plasma, xfce, wayland, release]
description: "Solus 4.9 Serenity is out with Linux 6.18, LUKS2 encryption by default, GRUB 2.14, Calamares 3.4.2, and updated Budgie, GNOME, Plasma, and Xfce editions."
image: /assets/images/post-images/solus/solus-4-9-serenity-release.webp
---

**The** Solus team has released **Solus 4.9 Serenity**, the first Solus release of 2026. It arrives around five months after [Solus 4.8 Opportunity](/solus-4-8-opportunity-release/) and focuses on system management, installation reliability, and updated desktop editions.

Solus 4.9 Serenity brings notable changes across the kernel, installer, encryption stack, and desktop environments, while also continuing the project’s gradual move toward a Wayland-first future.

![Solus 4.9 Serenity desktop environments Budgie GNOME Plasma Xfce screenshot](/assets/images/post-images/solus/solus-4-9-serenity-release.webp)

## Key highlights

- Linux kernel 6.18.21
- LUKS2 encryption by default for new installations
- GRUB 2.14 with Argon2 support on legacy non-EFI systems
- Calamares 3.4.2 installer improvements
- Updated Budgie, GNOME, Plasma, and Xfce editions
- Continued transition toward Wayland in future releases

## What's new in Solus 4.9 Serenity

### System service management

Solus now uses **systemd preset files** to control which services start by default. Previously, the project relied on symlinks inside `target.wants` directories, which could cause systemd to report service status incorrectly and made maintenance more difficult. Preset files simplify service management and improve accuracy.

The default privileged group has also changed from `sudo` to `wheel`. Since many upstream projects already assume `wheel` as the standard administrative group, this reduces the number of Solus-specific patches needed during package updates.

### Installation and encryption improvements

On legacy non-EFI systems, GRUB has been updated to **version 2.14**. This release adds **Argon2 encryption support**, allowing **LUKS2** to become the default disk encryption format for new Solus installations.

LUKS2 offers a more modern encryption format than LUKS1 and also supports storing encryption keys in the system TPM for automatic partition unlocking during boot on supported hardware.

Solus also ships **Calamares 3.4.2**, which brings installer improvements. The project now uses a hybrid bootloader setup on legacy systems, creating partitions for both systemd-boot and GRUB2, with one chainloading the other. This replaces a custom patch Solus had previously maintained.

Another practical change is the increase of the default EFI partition size to **2 GB**, helping accommodate growing firmware, kernel module, and NVIDIA-related package requirements.

### Desktops and core packages

All Solus 4.9 editions ship with **Firefox 149.0.2**, **LibreOffice 25.8.6.2**, and **Thunderbird 149.0.2** as core applications. Across all editions, Solus uses **Linux kernel 6.18.21** together with **Mesa 26.0.4**.

The kernel configuration is now shared with the [AerynOS project](/distribution/aerynos), which broadens hardware support in Solus.

#### Budgie

The Budgie edition ships with **Budgie 10.9.4**. One visible change is the switch from GNOME Terminal to [ptyxis](https://gitlab.gnome.org/chergert/ptyxis) as the default terminal application.

#### GNOME

The GNOME edition includes **GNOME 49.5**, a maintenance update in the GNOME 49 series.

#### Plasma

The Plasma edition ships with **KDE Frameworks 6.24.0**, **KDE Plasma 6.6.4**, and **KDE Gear 25.12.3**. Plasma 6.6 brings several user-facing improvements, including a better on-screen keyboard, text extraction in Spectacle screenshots, QR-code-based Wi-Fi setup, and expanded accessibility options.

#### Xfce

The Xfce edition includes the latest **Xfce 4.20** series packages, continuing Solus’ usual focus on stability and lightweight desktop performance.

## Move toward Wayland

Solus 4.9 also reflects the broader Linux desktop shift toward **Wayland**. While this release itself is not fully Wayland-only, upstream roadmap changes already point in that direction.

Budgie 10.10 is expected to drop X11 support entirely, while future GNOME and KDE Plasma releases are also moving toward a Wayland-only model. That makes Solus 4.9 an important step in the project’s transition toward a more modern Linux desktop stack.

For a broader overview of [Solus as a distribution](/distribution/solus), or to compare this release with the earlier [Solus 4.7 Endurance release](/solus-47-release/), those pages provide useful background.

## Download Solus 4.9 Serenity

Solus 4.9 Serenity is available in **Budgie, GNOME, Plasma, and Xfce** editions from the [official Solus download page](https://getsol.us/download/).

For more technical details, see the [official Solus 4.9 release announcement](https://getsol.us/2026/04/solus-4-9-released/).

## FAQ

### What is new in Solus 4.9 Serenity?

Solus 4.9 Serenity introduces Linux kernel 6.18.21, LUKS2 encryption by default for new installs, GRUB 2.14 improvements, Calamares 3.4.2 installer updates, and refreshed Budgie, GNOME, Plasma, and Xfce editions.

### Does Solus 4.9 support Wayland?

Solus 4.9 is part of the project’s gradual move toward Wayland. While this release is not fully Wayland-only, future Budgie, GNOME, and Plasma updates are expected to continue that transition.