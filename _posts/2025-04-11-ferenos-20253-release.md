---
title: "Feren OS 2025.03 Released: A Major Rebase and Refined Experience"
layout: post
categories: [ferenos, Linux, News]
tags: [Feren OS 2025.03, Ubuntu 22.04 LTS, KDE Plasma, Pipewire, DesktopSwop, Flatpak, GNOME Web]
description: "Feren OS 2025.03 is now available! Based on Ubuntu 22.04 LTS, this refined release brings better performance, KDE Plasma 5.27, Pipewire, DesktopSwop, and more — here’s everything new."
image: /assets/images/post-images/ferenos/ferenos-20253.jpg
---

Feren OS 2025.03 is here — and it’s a big one. Officially codenamed **"Osmium"**, this release marks a major rebase for the popular Linux distribution, now built on **Ubuntu 22.04 LTS**, and comes packed with system refinements, feature updates, and exciting under-the-hood changes.

![Feren OS 2025.3 featured image](/assets/images/post-images/ferenos/ferenos-20253.jpg)

Although finalized on **March 31st**, the update was rolled out to existing users at **4 AM on April 1st**. A brief delay was caused by a rare race condition during testing, making this technically a late-March release. The ISO itself needed further polishing and was released shortly after.

## What's New in Feren OS 2025.03?

### 🔁 Based on Ubuntu 22.04 LTS

Feren OS has now moved on from Ubuntu 20.04 LTS to **Ubuntu 22.04 LTS**, offering improved security, newer software, and support through April 2027. This foundational shift has enabled deeper refinements and long-overdue changes.

### 🔧 Rebuilt, Refined, and Reclaimed

This version revisits Feren OS’s system structure from the ground up:

- Removed unnecessary upstream metapackages and software recommendations.
- Eliminated unneeded dependencies, resulting in a **lighter, faster** system.
- Protected system-critical components from accidental removal.
- Pre-installed apps remain removable, except essential system parts.

These changes aim to **improve stability and future-proofing** while delivering the polished Feren OS experience users expect.

### 💻 KDE Plasma 5.27 — Final Release of Plasma 5

Feren OS 2025.03 ships with **KDE Plasma 5.27**, marking the end of the Plasma 5 era. Key tweaks include:

- Adaptive panel transparency (old behavior restored).
- Notification drain bar and extended accent color options.
- Reduced custom patching for faster Plasma updates and more authentic layouts.
- **Latte Dock removed** — replaced by pre-configured panels for "Human" and "Mac and Cheese" layouts.

### 🔊 Pipewire Takes Over

Replacing PulseAudio, **Pipewire** is now the default sound server. This change, in development since 2022, enhances sound quality and screen recording capabilities.

### 🧑‍💻 Rewritten OEM Config

OEM Config has been redesigned to resemble Vanilla OS's approach:

- Logs into a restricted Plasma session after boot.
- Lets users connect to Wi-Fi, monitor battery, and adjust brightness **before finishing setup**.
- Prepares the system for a **future Wayland transition**.

### 🖥️ Introducing: DesktopSwop

Feren OS introduces **DesktopSwop**, a feature that segregates GTK configurations per desktop environment:

- Separate themes for GTK apps on KDE, GNOME, etc.
- No more cross-DE theme conflicts.
- Ideal for advanced users running multiple desktop environments.

### 📦 Firefox & GNOME Web Now from Flathub

Two big package changes:

- **Firefox** now comes from **Flathub**, not Snap.
- **GNOME Web** (Epiphany) is also now pulled from **Flathub**, based on community votes.

These changes provide **faster updates**, **cross-platform profile consistency**, and better integration with Feren OS.

## Removals

- **PPAs and custom repositories** are disabled by default due to security and compatibility risks.
- Users needing advanced repository controls can manually install `software-properties-qt`.

## Known Issues

- **DNS Resolver Bug**: Occasionally, DNS resolution may fail due to a known `systemd` issue ([tracked here](https://github.com/systemd/systemd/issues/21123)). A quick reconnect to your network usually fixes it.


For [further information on FerenOS 2025.3](https://medium.com/feren-os/feren-os-2025-03-minor-rebase-update-for-feren-os-f82ce0a47a52) - read the official release announcement.