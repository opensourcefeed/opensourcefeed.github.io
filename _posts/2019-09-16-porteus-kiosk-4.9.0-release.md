---
title: "Porteus Kiosk 4.9.0 released with Chrome 76.x, Firefox 68.x and other updates"
layout: post
categories: porteus release
tags: porteus release
image: "/assets/images/post-images/porteus-kiosk-4.9.0.png"
---

**Mr** *Tomasz Jokiel* has announced the release of Porteus Kiosk 4.9.0, the latest stable release of popular embedded device operating system. This release includes updated versions of Google Chrome, Firefox, Linux Kernel, and other core packages.

![Porteus Kiosk 4.9.0 banner](/assets/images/post-images/porteus-kiosk-4.9.0.png)

In Porteus Kiosk 4.9.0, all packages are synced with *portage snapshot* tagged on 8th September 2019.

One of the key highlights of Porteus 4.9.0 is Firefox 68 ESR release. This means the plugins that make use of NPAPI (Netscape Plugin API) would not be supported anymore. The java module is also removed from additional components, while the Citrix Receiver will still continue to work as an associated application.

Other changes in Porteus 4.9.0 are listed below.

> - Support for setting default zoom level in both Firefox and Chrome browsers.
- Session idle function is now able to lock the session instead of restarting it.
- Users can now select a large mouse cursor theme.
- Screen locking button can also function in the 'shutdown menu' if it is enabled in the kiosk config.
- Remote config name is displayed in the Administration Panel of Porteus Kiosk Server. 
- This makes it easy to identify which config is used by Kiosk.
- Users can now enable bookmarks toolbar in Firefox, even when the rest of the toolbox is hidden.
- The boot loader is updated to boot some CoffeLake and GeminiLake systems which support EFI firmware only.
- Forced screen resolution on the framebuffer level allows the kiosk to work in 'FullHD' mode in Hyper-V virtual machines.
- Other bug fixes and improvements.

For a completed list of changes, read the [Porteus Kiosk 4.9.0 detailed changelog](https://porteus-kiosk.org/changelog-releases.html#4.9.0).