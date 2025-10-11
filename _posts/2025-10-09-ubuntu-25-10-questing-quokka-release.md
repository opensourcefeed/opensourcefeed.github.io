---
layout: post
title: "Ubuntu 25.10 'Questing Quokka' Released with Updated Flavors"
categories: [Linux, Ubuntu, Release]
tags: [ubuntu, questing-quokka, linux, release, flavors, kubuntu, xubuntu, lubuntu, budgie, studio, cinnamon, edubuntu]
description: "Ubuntu 25.10 'Questing Quokka' released with Linux 6.17, GNOME 49, and major updates across Kubuntu, Lubuntu, Xubuntu, and other flavors."
image: /assets/images/post-images/ubuntu/25.10.webp
---

**Canonical** has released Ubuntu 25.10, codenamed *Questing Quokka*. It is an interim release with support until **July 2026**. This version focuses on cleaner code, simpler tools, and a stronger system foundation. All official Ubuntu flavors have also received updates.

![Ubuntu 25.10 Questing Quokka featured image](/assets/images/post-images/ubuntu/25.10.webp)

## What’s New in Ubuntu 25.10

Ubuntu 25.10 updates core software and replaces several long-used components with newer tools.

### Main Changes

> - **Linux Kernel 6.17** improves hardware support and system performance.  
- **Rust-based system tools** replace some GNU utilities, improving safety and reliability.  
- **Dracut** replaces `initramfs-tools` for building the boot process.  
- **GNOME 49** is now the desktop environment, running only on **Wayland**.  
- **Loupe** is the new image viewer, replacing Eye of GNOME.  
- **Ptyxis** is the new terminal, designed for modern workflows.  
- **Chrony** replaces `systemd-timesyncd` for time synchronization, with Network Time Security support.  
- **Ubuntu Insights** adds a simple way to share anonymous system data.  
- **Mesa 25.2** updates graphics drivers for Intel, AMD, and NVIDIA GPUs.  
- **RISC-V** support now targets the newer RVA23 profile.

These updates make Ubuntu 25.10 faster, more secure, and easier to maintain.

## Updates in Ubuntu Flavors

Each Ubuntu flavor benefits from the same base upgrades. They also include updates to their desktop environments and applications.

| **Flavor** | **Changes in 25.10** |
|-------------|----------------------|
| **Kubuntu** | Uses **KDE Plasma 6.4.5** with KDE Frameworks 6.17 and KDE Gear 25.08.1. Wayland is the default. Improves performance and display handling. |
| **Xubuntu** | Updates the Xfce desktop. Gains better hardware support and lower resource usage. Ideal for older systems. |
| **Lubuntu** | Keeps the LXQt desktop simple and light. Includes kernel and software updates. |
| **Ubuntu Studio** | Ships with newer versions of **Audacity**, **Kdenlive**, **GIMP**, **Krita**, and other creative tools. Adds a new optional dock layout. Runs on **KDE Plasma 6.4.5**. |
| **Ubuntu Budgie** | Includes visual fixes and updated applications. Built on the same core improvements as the main release. |
| **Ubuntu Cinnamon** | Refines the Cinnamon desktop with smoother performance and updated artwork. |
| **Edubuntu** | Updates educational tools and improves classroom usability. |

> **Note:** Ubuntu MATE did not meet the release schedule and may not have an official 25.10 release.

All flavors share the same support period until **July 2026**.


## Upgrade and Installation Notes

- **Upgrade path:** Users on Ubuntu 25.04 can upgrade directly.  
- **Clean install recommended:** A fresh install applies new defaults like Dracut more effectively.  
- **Support window:** Ubuntu 25.10 will receive updates for nine months.  
- **X11 users:** GNOME now runs only on Wayland. Use Kubuntu or Xubuntu if X11 is required.  
- **Testing:** Try 25.10 in a virtual machine before deploying it widely.


## Summary

Ubuntu 25.10 is a stable and modern update. It continues Ubuntu’s move toward safer, memory-protected software and streamlined system tools.  

It’s a good choice for users who want new features and don’t mind short-term support. Those seeking long-term stability should stay on Ubuntu 24.04 LTS or wait for Ubuntu 26.04 LTS.

*Sources:*  [Ubuntu Wiki](https://wiki.ubuntu.com/Releases) • [9to5Linux](https://9to5linux.com/ubuntu-25-10-questing-quokka-is-now-available-for-download-this-is-whats-new) • [OMG! Ubuntu](https://www.omgubuntu.co.uk/2025/10/ubuntu-25-10-new-features) • [Phoronix](https://www.phoronix.com/news/Ubuntu-25.10-Lands-Linux-6.17)
