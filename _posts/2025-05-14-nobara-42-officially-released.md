---
title: "Nobara 42 Officially Released!"
layout: post
categories: [linux, nobara, release]
tags: [nobara, linux, rolling release, brave, flatpost, drivers]
description: "Explore the new features and enhancements in Nobara 42, including Brave as the default browser, the introduction of Flatpost, and improved driver management."
image: /assets/images/post-images/nobara/nobara-42.jpg
---

**Nobara Linux** 42 has officially landed, introducing a host of significant updates aimed at enhancing user experience, particularly for gamers and content creators. This release marks Nobara's full transition into a rolling release model, ensuring users receive continuous updates without the need for major version upgrades.

![Nobara 42 featured image](/assets/images/post-images/nobara/nobara-42.jpg)

## 🦁 Brave Becomes the Default Browser

After extensive testing, Brave has been adopted as the default web browser in Nobara 42. This decision follows issues encountered with other browsers:

- **Firefox and its derivatives** (like Floorp and LibreWolf) experienced GPU crashes when scrolling through live videos with Variable Refresh Rate (VRR) enabled.
- **Chromium and Vivaldi** faced compatibility problems with Google Meet when hardware acceleration was active.

Brave stood out by operating reliably without requiring additional packages for video codecs. To streamline the browsing experience and prioritize user privacy, Nobara ships Brave with a custom policy that disables features such as Brave Rewards, Brave Wallet, Brave VPN, and Tor integration. These settings can be adjusted by users if desired.

## 📦 Introducing Flatpost: A Universal Flatpak Manager

Nobara 42 replaces traditional package managers like plasma-discover and gnome-software with **Flatpost**, a new in-house developed application designed to manage Flatpak software seamlessly across various desktop environments. Built with Python and GTK, Flatpost allows users to install, remove, upgrade, and manage permissions for Flatpak applications, offering a user-friendly interface akin to Flatseal. This change aims to provide a consistent software management experience, especially for users who opt for desktop environments beyond GNOME and KDE.

## 🔄 Transition to Rolling Release

With version 42, Nobara completes its shift to a rolling release model. This approach ensures that users receive the latest updates and features continuously, eliminating the need for periodic major version upgrades. Users who were on Nobara 41 would have already received the updates leading to version 42 through the system updater.


## 🎮 Enhanced Driver Management

The updated **Nobara Driver Manager** offers users greater flexibility in managing their graphics drivers:

- Easily switch between `mesa-vulkan-drivers` and `mesa-vulkan-drivers-git`.
- Choose between open or closed versions of NVIDIA drivers across different branches, including Production, Beta, and New Feature.

These enhancements aim to simplify driver management, catering to both novice and advanced users.


## 🧱 Core Component Updates

Nobara 42 includes updates to several core components:

- **GNOME**: Version 48
- **KDE Plasma**: Version 6.3.4
- **Linux Kernel**: Version 6.14.6
- **Mesa**: Version 25.1.0, featuring patches for Wine Wayland and DOOM: The Dark Ages
- **NVIDIA Driver**: Production version 570.144

## 🚀 Getting Started with Nobara 42

For those interested in exploring Nobara 42, the distribution is available for download on the [official Nobara Project website](https://nobaraproject.org/). Whether you're a gamer, content creator, or a Linux enthusiast seeking a user-friendly experience, Nobara 42 offers a robust and continuously updated platform tailored to your needs.

*Note: For detailed information on the changes and features introduced in Nobara 42, refer to the [official changelog](https://nobaraproject.org/category/changelog/).*
