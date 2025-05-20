---
title: "GIMP 3.0.4 Released: Stability and Performance Enhancements"
layout: post
categories: [GIMP, Software Updates]
tags: [GIMP, Open Source, Image Editing, Software Release]
description: "Explore the latest improvements in GIMP 3.0.4, focusing on bug fixes, performance enhancements, and UI refinements."
image: /assets/images/post-images/gimp-3.0.4.jpg
---

**The** GIMP team has announced the release of **GIMP 3.0.4**, the second micro-update following the major 3.0 launch in March 2025. This release emphasizes stability and performance improvements, addressing various bugs and regressions identified by the community.


![GIMP 3.0.4 Splash Screen](/assets/images/post-images/gimp-3.0.4.jpg)


## 🛠️ Key Fixes and Improvements

- **Clipboard Pasting Bug**: Resolved an issue where pasted selections were incorrectly padded to the original image size when transferred to other applications.

- **Monitor-Related Crashes**: Fixed crashes occurring when changing or turning off the main monitor, enhancing stability in multi-monitor setups.

- **Font System Enhancements**: Improved font loading speed at startup, benefiting users with extensive font libraries.

- **Non-Destructive Filters**: Enhanced undo history tracking for non-destructive filters, including displaying filter names and individual edits.

- **Additional Fixes**:
  - Corrected the Help button functionality in the About dialog.
  - Restored the Wilber icon on KDE Wayland systems.
  - Fixed the `ZDI-CAN-26752` bug affecting `.ICO` file imports.


## 🔄 Addressing Regressions

- **Window Hint Option**: Restored the functionality allowing floating windows to remain in front in multi-window mode.

- **Canvas Interaction**: The space bar now respects user-defined actions, allowing customization beyond default panning.

- **Difference Cloud Filter**: Reintroduced the GUI for the Difference Cloud filter, correcting a long-standing regression from GIMP 2.8.

- **Plug-in Browser**: Ensured all plug-ins are visible again in the browser.

- **Sample Points Display**: Fixed issues with the Sample Points display not updating with changes in image precision.

- **Screenshot Plug-in**: Reverted to using radio buttons for options, simplifying user interaction.

- **BMP Format Warnings**: Addressed missing warnings for BMP formats on Linux systems.


## 🎨 UI/UX Enhancements

- **MyPaint Brush Tool**: Updated the options UI to align with other painting tools, promoting consistency.

- **Pencil Tool Adjustment**: Removed the non-functional "Force" slider from the Pencil Tool options to reduce confusion.


## 📥 Download GIMP 3.0.4

GIMP 3.0.4 is available for various platforms:

- **Windows**: Universal installer supporting x86 (32 and 64-bit) and ARM (64-bit).

- **macOS**: DMG packages for both Intel and Apple Silicon hardware.

- **Linux**: AppImages and Flatpaks for x86 and ARM (64-bit).

Download the latest version from the official GIMP website: [gimp.org](https://www.gimp.org/downloads/)

For a detailed overview of all changes in GIMP 3.0.4, refer to the official release announcement: [GIMP 3.0.4 Released](https://www.gimp.org/news/2025/05/18/gimp-3-0-4-released/)
