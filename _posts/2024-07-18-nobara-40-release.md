---
title: "Nobara 40 Released with Fedora 40 foundation"
layout: post
categories:
- nobara
- release
image: "/assets/images/post-images/nobara-40.jpg"
description:  "Discover Nobara 40: a major update featuring revamped system updates, enhanced Flatpak support, new theming options, gaming enhancements, and much more!"
---

**The** Nobara project has announced the release of Nobara 40, following several delays due to various bugs and issues, including those related to KDE 6.1.1, Mesa, GNOME 46, Nvidia 555 drivers, and the complete remake of their updater. Despite the bumpy transition from 38 to 39, the team focused on ensuring a smooth and stable transition for Nobara 40.

![Nobara 40 featured image](/assets/images/post-images/nobara-40.jpg)

## Key Updates and Enhancements in Nobara 40

### System Updates, Flatpaks, and Snaps

- Revamped Update System App: The update system has been remade into a Python GUI application, replacing the previous monolithic bash script.
Integration with Nobara Package Manager: The new update app is better integrated with the Nobara Package Manager (yumex-ng), providing a system tray app for receiving update notifications.
- Improved Flatpak Management: The Nobara Package Manager can now fully search, install, and remove Flatpaks in a user-friendly GUI, removing the need for KDE Discover or GNOME Software for system packages.
- Enhanced Snap Support: Issues preventing certain apps from operating have been fixed, and Snap support has been improved.

### Theming

- Reworked KDE Theme: The Nobara KDE theme has been reworked to avoid conflicts with other themes and no longer forces settings if not used.
- Icon Fixes: Issues with Papirus-Dark icons have been resolved, and standard Papirus packages are now used along with papirus-folders for folder color management.
- New Wallpapers: Nobara 40 includes a new set of standard and additional AI-generated “weebara” wallpapers.

### Desktop Environments

- KDE Update: Updated to version 6.1.1, following Fedora’s packaging.
- GNOME Update: Updated to version 46, following Fedora’s packaging.
- XWaylandVideoBridge Removal: Removed from default GNOME ISOs due to a bug causing a white border on the screen.

### Graphics

- Mesa and Nvidia Drivers: The current Mesa version is 24.1.3, with regular updates, and Nvidia drivers are proprietary 555.58.02.

### Gamescope and Gaming Enhancements

- Gamescope and Gaming Tools: Gamescope is built regularly from git, with various updates and fixes. Other gaming tools like Lutris, umu-launcher, mangohud, goverlay, and protonup-qt have also been updated or replaced.


### Content Creation

- OBS Studio Updates: Updated to version 30.2.0 with additional plugins for media playlist, background removal, and HDR capture support.
- Davinci Resolve Runtime: Still provided and works as of Resolve 18.6.

### Hardware Support

- Updated Kernel: The shipped kernel is 6.8.12, with patches for various devices including Surface, Lenovo Legion, and T2 MacBooks. Testing of kernel 6.10 is ongoing.

### Miscellaneous Changes

- Default Browser and Office Suite: Returned to using Firefox as the default browser and LibreOffice instead of OnlyOffice.
- KDE CLI Tools: Patched to allow certain applications to work correctly when external links are used.

### Community and Development

- Open Source Contributions: All package modifications and custom package sources are now available on GitHub, making it easier to access and contribute to the project.

For further information and download options, read the [Nobara 40 official release announcement in the projects website](https://nobaraproject.org/2024/07/17/july-17-2024/).
