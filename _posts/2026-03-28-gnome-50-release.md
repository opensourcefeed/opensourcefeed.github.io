---
layout: post
title: "GNOME 50 'Tokyo' Released: Parental Controls, Remote Desktop, and More"
categories: [gnome, release, desktop]
tags: [gnome, gnome-50, release, linux-desktop, wayland]
description: "GNOME 50 'Tokyo' is out with screen time controls, Orca improvements, document annotations, hardware-accelerated remote desktop, and VRR/fractional scaling by default."
image: /assets/images/post-images/gnome/gnome-50.jpg
---

**The** GNOME Project has released **GNOME 50**, codenamed **"Tokyo"**, on March 18, 2026. The name honors the local organizers of GNOME.Asia Summit 2025. This is a milestone version — the fiftieth release — and it brings a wide range of improvements across accessibility, parental controls, remote desktop, display handling, and core apps.

![GNOME 50 'Tokyo' desktop environment release screenshot](/assets/images/post-images/gnome/gnome-50.jpg)

## Parental Controls Get a Major Overhaul

One of the headline additions in GNOME 50 is a completely rebuilt parental controls system. Parents and guardians can now set screen time limits and bedtime schedules for child accounts. When a limit or bedtime is reached, the screen locks automatically. Guardians can also grant extra time on the fly when needed.

The Parental Controls app has a fresh look, and Settings now links directly to it. Under the hood, GNOME has also laid the groundwork for web filtering — a backend service that can enforce content restrictions for child accounts, with the user interface coming in a future update. This work was funded by [Endless](https://endlessglobal.com/foundation-grants).

## Orca Screen Reader and Accessibility

GNOME 50 ships several meaningful updates for assistive technology users. The **Orca** screen reader gets a redesigned preferences window, global settings (no more per-app saving), automatic language switching for web content and app UI, extended browse mode for all document content, and improved Braille support. Mouse Review now works in Wayland sessions too.

A new **Reduced Motion** option has also been added to Accessibility settings. It tones down interface animations for users who find them distracting or uncomfortable.

## Document Viewer Annotations

The **Document Viewer** app now has a fully reworked annotation system. Users can add text annotations, draw lines, and highlight sections — all accessible from the main view with a single click. The tool supports color choices, line thickness control, and an eraser. It is a practical feature that was long overdue.

## Files App: Faster and More Refined

The **Files** app has seen broad improvements in GNOME 50. Thumbnail and icon loading is faster, memory usage is lower, and test coverage has expanded to help keep bugs in check. On the interface side, batch rename now shows visual highlights for replaced text, file properties open as free-floating windows, and the pathbar supports case-insensitive completions.

For those who missed it, [GNOME 40 introduced a redesigned Activities overview](https://www.opensourcefeed.org/gnome-40-release/) that set the tone for many of these incremental refinements.

## Calendar: Attendees, ICS Export, and Navigation

**Calendar** picks up an attendee list — you can now see who is invited to an event and whether their attendance is required or optional. There is also a new ICS export option, a redesigned Quick Add popover, smoother Month view scrolling, and support for hardware Back/Forward buttons. The app now respects the system's first-day-of-week setting, which is also honored by Settings and Evolution.

## Remote Desktop with Hardware Acceleration

GNOME 50 adds **Vulkan and VA-API** hardware acceleration to the built-in remote desktop feature, making remote sessions noticeably smoother with lower latency and less power draw. NVIDIA users get additional stability through explicit sync support. New **HiDPI support** lets clients scale automatically to the remote display's resolution, and **camera redirection** lets you use a local webcam inside a remote session. Kerberos Authentication support is also included for professional environments.

## Display: VRR, Fractional Scaling, and HDR

Variable Refresh Rate (VRR) and fractional scaling are now **enabled by default** in GNOME 50. VRR keeps the display refresh rate matched to the application's frame rate for tear-free motion; fractional scaling allows increments like 125% or 150% for better DPI matching. A new low-latency cursor mode keeps mouse movement fluid at up to 144Hz even when an app runs at a lower frame rate.

NVIDIA users also benefit from frame-timing fixes that reduce stuttering. On the color side, GNOME 50 adds support for Wayland color management protocol v2, and HDR screen sharing is now possible — screen recorders can capture HDR content as it appears on screen.

## New GNOME Circle Apps

Several new apps have joined [GNOME Circle](https://circle.gnome.org) with GNOME 50:

- **Gradia** — annotate and refine screenshots with gradients, shadows, and ten annotation modes.
- **Sudoku** — a clean number-puzzle app with conflict highlighting and keyboard navigation.
- **Constrict** — compress video to a target file size using codecs like AV1, HEVC, and H.264.
- **Sessions** — a simple Pomodoro timer for focused work sessions.

## Getting GNOME 50

GNOME 50 will arrive in most distributions over the coming weeks. You can try it now via the [GNOME OS image](https://os.gnome.org/) in a virtual machine using GNOME Boxes. Major distributions like Fedora and Ubuntu are expected to ship it in upcoming releases — [Fedora has been a reliable early adopter of new GNOME versions](https://www.opensourcefeed.org/fedora-linux-42-released/).

For the full list of changes, see the [official GNOME 50 release notes](https://release.gnome.org/50/).