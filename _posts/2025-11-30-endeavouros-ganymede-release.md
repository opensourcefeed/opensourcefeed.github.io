---
layout: post
title: "EndeavourOS Ganymede Release: Latest ISO Updates"
categories: ["endeavour", "EndeavourOS", "News"]
tags: ["EndeavourOS", "Ganymede", "Arch Linux", "Linux Release"]
description: "EndeavourOS releases its new Ganymede ISO with improved Nvidia support, installer updates, and desktop-specific refinements."
image: /assets/images/post-images/endeavouros/Ganymede.jpg
---

**The** EndeavourOS team has released a refreshed ISO called **Ganymede**. 

The release comes after a long gap, which led to questions about the project’s status. The team confirmed that development continues, and regular package updates have kept existing systems running without issues.  Only the live environment and offline installer had fallen behind, and Ganymede addresses this.

![Endeavour OS featured image](/assets/images/post-images/endeavouros/Ganymede.jpg)

This release affects **new installations only**.  

Existing EndeavourOS users who update often do not need to upgrade to this ISO.

You can read the original announcement here: <https://endeavouros.com/news/the-long-wait-is-over-ganymede-has-arrived/>

## What’s New in the Ganymede Release

### Key package versions on the ISO
> - Calamares 25.11.1.9-1  
- Firefox 145.0.1-1  
- Linux kernel 6.17.8.arch1-1  
- Mesa 1:25.2.7-1  
- Xorg-server 21.1.20-1  
- Nvidia-utils 580.105.08-4  

### Nvidia driver changes
Nvidia support has been rebuilt.  
The ISO now detects the GPU during boot and installs the correct driver—**nvidia** or **nvidia-open**—without user input.  
The live session loads the right modules, and the installer carries this over to the final system.  
This makes Nvidia handling automatic and reliable across all supported GPUs.

### Broadcom Wi-Fi handling
The **broadcom-wl** driver is no longer enabled by default.  
It caused issues with other network devices.  
If the live system detects hardware that needs this driver, it shows a prompt.  
When enabled, the installer adds the driver to the installed system.

### EOS Qogir icon updates
Icon naming changes from upstream have been added to prevent broken theming in GTK-based desktops and window managers.

### Desktop environment improvements

#### Plasma
- Maliit has been replaced by the Qt6 virtual keyboard for SDDM.  
- Libappindicator-gtk3 has been replaced by Libappindicator.

#### GNOME
- `gnome-screenshot` has been removed from the default package list.

#### LXDE
- GTK3 postfixes have been removed from package names.  
- `obconf` has been replaced by `lxappearance-obconf-gtk3`.  
- `pcmanfm-gtk3` has been renamed to `pcmanfm`.

#### i3
- `xbacklight` has been replaced by `brightnessctl`.

