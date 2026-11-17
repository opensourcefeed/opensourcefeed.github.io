---
layout: distribution
uid: bazzite
title: 'Bazzite'
tagline: 'An immutable, SteamOS-like gaming OS for any PC or handheld'
Category: Distribution
type: Linux
permalink: /distribution/bazzite
logo: bazzite-logo.svg
preview: bazzite-preview.jpg
home_page: https://bazzite.gg/
desktops: [plasma, gnome]
base: [fedora]

description: 'Bazzite is an immutable, Fedora Atomic-based gaming distribution built by Universal Blue. It brings a SteamOS-like Steam Deck experience to handhelds, desktops and HTPCs.'

seo:
  type: OperatingSystem

faq:
  "Is Bazzite the same as SteamOS?": "No. Bazzite is a separate, community-built distribution that copies SteamOS's Steam Deck-style Gaming Mode and KDE theming on top of Fedora Atomic. SteamOS is Valve's own OS, officially supported only on Steam Deck and a short list of handhelds; Bazzite runs on far more hardware, including desktops, laptops and HTPCs."
  "Do I need to reinstall Bazzite to switch desktops?": "Yes, in most cases. KDE Plasma (built on Fedora Kinoite) and GNOME (built on Fedora Silverblue) are separate base images, so moving between them means downloading the other image and rebasing or reinstalling, not flipping a setting."
  "Can I install regular Linux apps on Bazzite?": "Yes. The base system is read-only, but Flatpak apps install normally through Flathub or the bundled Bazaar store, and Distrobox lets you run a full traditional Linux environment (Ubuntu, Fedora, Arch, etc.) in a container for anything that needs deeper system access."
  "Does Bazzite support Nvidia GPUs?": "Yes, Nvidia drivers are included in the Bazzite images. Support in Steam Gaming Mode and on HTPC images is marked beta by the project, so AMD and Intel GPUs currently have the more mature path."
---

**Bazzite** is a free, open-source Linux distribution built for gaming, from handhelds and HTPCs to full desktops and laptops. It is produced by [Universal Blue](https://universal-blue.org/), a project that builds ready-to-use, customized images on top of Fedora's immutable "Atomic" desktops, and it borrows the Steam Deck's console-like interface and KDE theming to bring a SteamOS-style experience to hardware Valve doesn't officially support.

## Built on Fedora Atomic, not from scratch

Bazzite doesn't maintain its own package base. Each edition rebases a stock Fedora Atomic image and layers gaming tools, drivers and configuration on top:

- The **KDE Plasma edition** is built on [Fedora Kinoite](/distribution/fedora).
- The **GNOME edition** is built on Fedora Silverblue.

Both inherit Fedora's `rpm-ostree` image-based update model: the whole filesystem updates and reboots as one atomic unit, the previous working image stays available to boot into if an update causes problems, and updates are kept for about 90 days before they're pruned. This is the same resilience model SteamOS itself uses, rather than a traditional package-by-package upgrade that can leave a system partially broken.

## A SteamOS-style gaming experience, almost anywhere

Bazzite's main pitch is bringing the Steam Deck's Gaming Mode to hardware Valve never shipped it on:

- **Steam Gaming Mode** boots straight into a console-like, controller-navigable interface, with Valve's own SteamOS themes pre-installed on the KDE edition.
- **Custom kernel and CPU scheduler tuning** aim to reduce input latency and improve frame pacing compared to a stock Fedora install.
- **Decky Loader** plugin support lets Steam Deck plugins and themes run in Gaming Mode on other hardware too.
- **HDR and VRR (variable refresh rate)** support is enabled where the display and GPU allow it.

## Beyond Steam

Steam and Lutris come pre-installed, and other storefronts are supported through separate launchers:

- **Heroic**, **itch**, and similar tools add Epic Games Store, GOG and itch.io libraries.
- **Waydroid** runs Android apps alongside the rest of the desktop, useful for mobile games or companion apps that have no native Linux client.
- **Bazaar**, Bazzite's Flatpak front-end, and Distrobox (for anything that needs a full traditional Linux environment in a container) cover everything outside the gaming stack.

## Who it's for

- **Steam Deck owners who also have a gaming PC or HTPC** and want the same Gaming Mode workflow everywhere.
- **Handheld PC owners** (ROG Ally, Legion Go and similar x86 devices) looking for a SteamOS alternative with broader hardware support than Valve offers. ARM-based handhelds aren't covered — the project points those users to [Armada](https://armada.aliceroux.dev/) instead.
- **Anyone who wants an immutable desktop** with gaming defaults already configured, rather than building the same stack manually on plain Fedora or Arch.
- **Users who want Secure Boot and full-disk encryption** out of the box: Bazzite ships SELinux, signed container images, Secure Boot support and LUKS encryption with optional TPM-backed unlocking.

Download the image that matches your device, GPU vendor and desktop choice from the [Bazzite website](https://bazzite.gg/), or rebase an existing Fedora Atomic install onto it with `rpm-ostree`.
