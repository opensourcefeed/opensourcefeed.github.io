---
layout: post
title: "Fedora Linux 43 Released: A New Chapter for the Fedora Project"
categories: [fedora, Linux, Releases]
tags: [Fedora 43, GNOME 49, Wayland, RPM 6.0, Linux Distribution]
description: "Fedora Linux 43 introduces GNOME 49, Wayland-only GNOME sessions, RPM 6.0, and improved CoreOS image building. Learn what’s new in this release."
image: /assets/images/post-images/fedora/fedora-43.webp
---

Fedora Linux 43 has arrived, marking another important milestone for the Fedora community. This release is the first under the new Fedora Project Leader, Jef Spaleta, who expressed gratitude to contributors and excitement for the project’s future direction.

![Fedora 43 featured image](/assets/images/post-images/fedora/fedora-43.webp)

## Upgrading to Fedora 43

Upgrading from an existing Fedora installation is simple. The process is similar to a regular system update and can be done through the terminal using **dnf system-upgrade** or through **GNOME Software**. As always, it’s recommended to back up your data before upgrading.

## Fresh Installation Options

New users or those wanting a clean start can download installation media for Fedora’s main Editions—**Workstation, KDE Plasma Desktop, Cloud, Server, CoreOS, and IoT**. Atomic Desktops like **Silverblue, Kinoite, Cosmic, Budgie, and Sway** are also available, alongside community Spins such as **Cinnamon, Xfce, and LXQt**.

## Key Changes in Fedora 43

Fedora 43 continues the project’s focus on innovation and modernization. While the release notes cover a long list of updates, here are the most notable highlights:

### 1. New Installer Experience

Fedora Spins now use the **Anaconda WebUI** as their default installer. Previously introduced in Fedora Workstation 42, this web-based interface brings a cleaner and more consistent installation experience across Editions.

### 2. GNOME Goes Wayland-Only

The **GNOME desktop** in Fedora 43 now runs exclusively on **Wayland**. X11 support has been deprecated and disabled in GNOME 49. This change paves the way for better performance, smoother visuals with triple buffering, and improved support for modern graphics hardware.

### 3. RPM 6.0 Arrives

Under the hood, Fedora 43 introduces **RPM 6.0**, a major upgrade to the package manager. It includes multiple key signing support, strengthening package security and preparing Fedora for future cryptographic standards, including post-quantum OpenPGP keys.

### 4. CoreOS Image Building Improvements

**Fedora CoreOS** can now be built from a base bootc image using a standard **Containerfile**, allowing anyone with **podman** to build images manually or through CI/CD pipelines. Updates for Fedora CoreOS are now delivered exclusively as **OCI images**, completing the transition from OSTree repositories.

## Fedora Workstation 43 Highlights

The **Workstation Edition** ships with **GNOME 49**, bringing refined UI polish, improved multi-display handling, new screenshot and screen recording tools, and a new **Focus Mode**. The update also introduces smarter background resource management for better performance and battery life.

A new default video player, **Showtime**, replaces Totem. Built with **GTK 4** and **Libadwaita**, Showtime provides a modern and responsive video experience.

For developers, **Peas 2.0** updates the GNOME plugin framework, while the **Noto Color Emoji** font now uses the **COLRv1** format, delivering scalable color emoji rendering.

For [further information on Fedora 43](https://fedoramagazine.org/announcing-fedora-linux-43/) - read the official release announcement on projects blog.