---
layout: post
title: "SteamOS 3.8.10 Released: KDE Plasma 6.4.3 and Wayland Default"
categories: [steamos, linux, release]
tags: [steamos, steam-deck, kde-plasma, wayland, linux-gaming, release]
description: "SteamOS 3.8.10 brings KDE Plasma 6.4.3, Wayland by default, Linux kernel 6.16, HDMI VRR support, and early Steam Machine hardware support."
image: /assets/images/post-images/steamos/steamos-3-8-10-release.webp
---

**Valve** has released SteamOS 3.8.10. The key change in SteamOS 3.18.10 change is a desktop overhaul: KDE Plasma jumps from 6.2.5 to 6.4.3, and Wayland replaces X11 as the default session. Underneath that, there is new hardware groundwork that points toward Valve's next device.

![SteamOS 3.8 makes the Wayland as default and brings initial support for upcoming Steam Hardware](/assets/images/post-images/steamos/steamos-3-8-10-release.webp)

## Desktop Mode moves to KDE Plasma 6.4.3 and Wayland

The biggest change in this release is in Desktop Mode. KDE Plasma jumps from version 6.2.5 to 6.4.3, and Wayland is now the default session instead of X11. Developers who still need X11 can switch back through Steam's developer settings or the `steamosctl` command-line tool.

This newer [Plasma desktop](/desktop/plasma) brings several practical improvements: better performance in Desktop Mode that now matches Game Mode more closely, support for external HDR and VRR displays, per-display scale factors, and improved handling of rotated screens. TV users should also notice better default scaling out of the box. Valve points to the official KDE Plasma 6.3 and 6.4 announcements for the full list of upstream changes. Readers who want a deeper look at what changed inside Plasma itself can check our coverage of the [KDE Plasma 6.5 release](/kde-plasma-6-5-release/) for context on where the desktop is headed next.

Other Desktop Mode fixes include keyboard layout and language settings that now follow Game Mode, better window behavior for games running under Proton, and a fix for open applications not being remembered when returning to Gaming Mode. Night Color settings also no longer linger incorrectly after switching back to Game Mode.

## Steam Machine hardware support begins

SteamOS 3.8.10 includes initial support for Valve's upcoming Steam Machine hardware, the clearest signal yet that new SteamOS-powered devices are on the way. The update also adds support for waking the system from sleep using a connected Steam Controller, and the underlying Arch Linux base has been refreshed along with the Linux kernel, now at version 6.16.

Other general fixes in this release include faster OS updates over high-speed connections, improved screen casting in Game Mode for tools like OBS and Discord, and fixes for dropdown menus that failed to appear in some games. Valve also fixed session crashes tied to specific game recording settings and to closing certain titles, including STAR WARS Jedi: Survivor and Starfield.

## Display, performance, and audio improvements

The graphics driver has been updated for both performance and stability. SteamOS 3.8.10 adds preliminary support for HDMI Variable Refresh Rate (VRR) on devices with native HDMI output, along with improved VRR frame pacing overall. Valve also fixed the FSR badge in the performance overlay, which previously stayed off even when FSR was active, and added graphics features required by upcoming titles such as Crimson Desert.

On the audio side, SteamOS can now detect HDMI channel count and expose surround sound configuration when available. A new setting allows Bluetooth headset microphones to be used in Game Mode, though Valve notes that playback quality drops while the microphone is active. Audio underruns after sleep and resume have also been fixed, along with a bug that could cause OLED Steam Deck speakers to lose output after a reboot.

## Steam Deck firmware and hardware fixes

This release ships Steam Deck LCD BIOS v133 and Steam Deck OLED BIOS v114. The LCD update adds a new "Memory Power Down" setup option and preliminary hibernation support, while the OLED update changes the charging LED to shift color as soon as the charge limit is reached, rather than only at 100%.

Steam Deck owners also get fixes for excessive trackpad sensitivity on early LCD models, a controller firmware update process that now shows progress on the splash screen, and a fix for a firmware update bug that could leave the left controller unresponsive for the rest of a session on certain Deck revisions.

## Expanded support for third-party handhelds

Valve continues to widen SteamOS support beyond the Steam Deck itself. This release adds controller, TDP control, and speaker audio support for the ASUS ROG Xbox Ally series, plus controller support for the OneXPlayer X1 series and Lenovo Legion Go 2, including firmware updates and RGB lighting controls for the Legion Go 2.

Handheld input also gets a major latency improvement: controller input latency drops from a range of 5 to 8 milliseconds down to just 100 to 500 microseconds. Other third-party hardware fixes include SD card reliability improvements for the ROG Xbox Ally and several Legion Go and MSI Claw models, controller support for the MSI Claw A1M and AI+ series, and fixes for washed-out OLED colors on Zotac and OneXPlayer devices. Valve also added preliminary firmware for upcoming Intel-based handhelds and fixed a Bluetooth issue affecting some existing Intel handheld models.

## Developer-facing changes

For developers, Desktop Mode now defaults to Wayland, with X11 still available through developer settings. The Linux kernel has been updated to version 6.16, and Steam now uses `steamos-manager` to query available desktop sessions and switch between them. SteamOS also gains initial support for running as a virtual machine guest through virtio guest drivers, and a new `custom-update` verb in `atomupd-manager` makes it easier to test specific builds. Anyone running other distributions who wants to compare kernel and base system choices can see how [FreeBSD 15.1](/freebsd-15-1-released/) approached similar updates around the same time.

## Getting the update

SteamOS 3.8.10 is rolling out automatically to all users on the stable channel. Steam Deck owners can check for it under Settings > System > System Update. Full technical details are available in [Valve's official SteamOS 3.8 release notes](https://store.steampowered.com/news/app/1675200/view/697641379212298072) on Steam.