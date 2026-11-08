---
layout: post
title: "GIMP 3.2.8 Released: Faster Preferences, Better RTL Text"
categories: [gimp, image-editing, release]
tags: [gimp, gimp-3-2, release, image-editor, linux, flatpak]
description: "GIMP 3.2.8 opens Preferences faster, improves right-to-left text editing and adds semi-transparent borders to Add Border. See what changed and where to get it."
image: /assets/images/post-images/gimp/gimp-3-2-8-released.webp
---

**The** GIMP team released GIMP 3.2.8 on November 2, 2026. It is the fourth maintenance update to the 3.2 series, which launched in March 2026. The release brings back Offset as a non-destructive filter, opens the Preferences dialog faster and improves how the text tool handles right-to-left languages.

![GIMP 3.2.8 image editor window with the text tool open on a Linux desktop](/assets/images/post-images/gimp/gimp-3-2-8-released.webp)

This is a fix-and-polish update, not a feature release. If you build composites with non-destructive filters, or you write in Arabic, Hebrew or another right-to-left language, it is worth installing. The same goes for macOS 27 users and for anyone who prints from GIMP on Windows 11. If your current version runs without problems, you can take your time. You can read more about the editor, its features and how it compares with paid tools on our [GIMP software page](/software/gimp/).

## What's new in GIMP 3.2.8?

### Editing and tools

- **Levels Color Picker fixed.** Picking input levels on a layer with non-destructive filters now gives correct values.
- **Add Border can make semi-transparent borders.** The filter now uses the transparency of the color you pick.
- **Levels shows correct values with the Color Picker.** Picking input levels on a layer that has non-destructive filters used to report the wrong numbers.
- **Copying non-rectangular selections from layer groups works again.** This fixes a regression that arrived in 3.2.6.
- **Color pickers show smaller color changes.** Small shifts are easier to see while you edit.

### Text tool and right-to-left support

- **New direction buttons.** The on-canvas text box now has icons to switch between left-to-right and right-to-left.
- **Automatic direction detection.** GIMP picks the base direction using the Unicode Bidirectional Algorithm until you choose one yourself.
- **Better cursor movement.** Arrow keys behave correctly in right-to-left text and in lines that mix both directions. The team also reduced problems with negative kerning.

### Speed and everyday fixes

- **Faster Preferences.** The dialog opens more quickly.
- **Faster large gradients.** Gradients larger than 6000 × 6000 pixels use better caching, and the "marching ants" selection outline needs less processing.
- **Quicker shutdown.** Font loading can stop early when you quit GIMP.
- **Larger HEIF images.** The HEIF loader can open bigger files.
- **Multi-monitor and Dot for Dot.** Dialogs open on the correct screen, and Dot for Dot reports the right pixel density again. It had been wrong since GIMP 3.0.
- **Windows.** The interface no longer appears to freeze after you open several images at once. Print Preview works with the Windows 11 print dialog.
- **macOS.** Title bars and menu icons show a background color again on macOS 27. Intel Macs no longer trigger Gatekeeper warnings, and the blank interface at startup on some Macs should be fixed.

### For plug-in developers

- Plug-ins can add submenus inside named menu sections, such as `<Image>/File/[Paste as]/Custom`. The old `gimp_plug_in_add_menu_branch()` function is now deprecated.

Since GIMP 3.2.6, the project closed 82 reports and merged 46 merge requests. 27 people contributed code, translations or packaging.

## Security fixes: how much should you worry?

The GIMP team says it keeps receiving a large number of security reports, helped by newer automated scanning tools, and it patched several in this release. Most reports target older image plug-ins and legacy filters. They trust the image size stored in a file. A crafted file can change that value and crash the plug-in, but not GIMP itself.

The announcement names no CVE identifiers. Treat this as a normal update, not an emergency. As a habit, open image files from sources you trust.

## Download GIMP 3.2.8

Get the stable build from the [official GIMP downloads page](https://www.gimp.org/downloads/). It offers:

- Linux AppImage, Flatpak and Snap packages for 64-bit x86 and ARM
- A Windows installer for x86 and ARM, also available in the Microsoft Store
- macOS DMG packages for Intel and Apple silicon

Most Linux distributions will take a while to ship 3.2.8 in their own repositories. Until then, Flatpak, Snap or the AppImage is the fastest route. The AppImage can now install Python packages from pip, like the Flatpak and Snap builds do. GIMP 3.2 still expects a fairly recent distribution, newer than Debian 13 "Trixie". The project publishes SHA256 and SHA512 checksums for the source release, so you can verify your download.

## References

- [GIMP 3.2.8 Released – official announcement](https://www.gimp.org/news/2026/11/02/gimp-3-2-8-released/)
- [GIMP downloads page](https://www.gimp.org/downloads/)
- [GIMP 3.2.8 Speeds Up Preferences, Improves Text Tool – Linuxiac](https://linuxiac.com/?p=222286)
- [GIMP 3.2.8 Released With Many Refinements – Phoronix](https://phoronix.com/news/GIMP-3.2.8-Released)
- [GIMP 3.2.8 brings bug fixes – OMG! Ubuntu](https://www.omgubuntu.co.uk/2026/11/gimp-3-2-8-brings-bug-fixes-fixes-fixes)
