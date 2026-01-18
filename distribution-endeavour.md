---
layout: distribution
uid: endeavour
title: 'EndeavourOS'
Category: Distribution
type : Linux
permalink: /distribution/endeavour
logo: endeavouros-logo.png
preview: endeavouros-preview.jpg
image: /assets/images/preview/endeavouros-preview.jpg
home_page: "https://endeavouros.com"
desktops: [xfce,mate,cinnamon,gnome,budgie,plasma,lxqt,lxde,i3,bspwm,sway,openbox]
base : [arch]
tagline: A Simple Way to Use Arch Linux

description : "EndeavourOS is an Arch-based Linux distribution by former Antergos community members. It offers a simple installer, multiple desktop environments, and the flexibility of Arch Linux for both new and experienced users."

releases:
  EndeavourOS Ganymede Neo: /endeavouros-ganymede-neo-released/
  EndeavourOS Ganymede: /endeavouros-ganymede-release/
  EndeavourOS Mercury: /endeavouros-mercury-release/
  EndeavourOS Neo Galileo: /endeavoros-20240125-release/
  EndeavourOS Atlantis Neo: "https://endeavouros.com/news/happy-holidays-atlantis-neo-has-arrived/" 
  EndeavourOS Atlantis Orbit: "https://endeavouros.com/news/the-atlantis-release-is-in-orbit/"

telegram : 
  Group: "https://t.me/EndeavourOS"

seo:
  type: OperatingSystem
---

## What is EndeavourOS?

**EndeavourOS** is a Linux distribution based on [Arch Linux](/distribution/arch). It provides a clean system with sensible defaults while staying close to upstream Arch. The project focuses on simplicity and transparency rather than heavy customization.

The installer helps users set up the system without hiding core choices. After installation, the system behaves like Arch Linux. Users manage packages with `pacman` and may use the Arch User Repository if they choose.

## Project Background

The EndeavourOS project started in 2019. It was created by former members of the [Antergos](/distribution/antergos) community after that project ended.

Unlike Antergos, EndeavourOS avoids replacing Arch core packages with custom versions. This design reduces conflicts and keeps the system predictable. The project follows a rolling release model and tracks Arch Linux closely.

## Installation and Setup

EndeavourOS uses the **Calamares installer**. It supports both offline and online installation modes.

* **Offline installation** installs the Xfce desktop with a stable base system.
* **Online installation** allows users to select other desktop environments or window managers.

The installer handles disk partitioning, user creation, locale setup, and bootloader configuration. After installation, users update the system using standard Arch tools.

## Desktop Environments and Window Managers

EndeavourOS supports a wide range of desktop environments and window managers.

Available desktop environments include:

* Xfce
* GNOME
* KDE Plasma
* Cinnamon
* MATE
* Budgie
* LXQt

It also supports window managers such as:

* i3
* bspwm
* sway
* Openbox

This flexibility makes EndeavourOS suitable for both traditional desktop use and minimal keyboard-driven workflows.

## System Design and Philosophy

EndeavourOS keeps the base system minimal. It installs only essential packages and avoids heavy theming or custom system layers.

The project documents changes clearly and avoids hidden automation. Users can inspect, modify, and maintain their system without relying on distribution-specific tools. This approach follows Arch Linux principles while lowering the entry barrier.

## Who Should Use EndeavourOS?

EndeavourOS is designed for users who want Arch Linux without a manual installation process.

It is suitable for:

* Users moving from other Linux distributions
* Developers who prefer a rolling release system
* Arch users who want a guided installer
* Desktop users who want flexibility without excess tooling

It may not suit users who prefer fixed releases or long-term support models.

## Release Model and Updates

EndeavourOS follows a **rolling release model**. New releases mainly refresh the installer and installation images.

Installed systems receive continuous updates from Arch repositories. There are no major version upgrades. Users keep the same system while receiving new kernels, drivers, and software over time.

## Summary

EndeavourOS offers a practical entry point to Arch Linux. It combines a simple installer with a clean and predictable system design.

For users who want Arch Linux without manual setup, EndeavourOS remains a stable and community-driven option.