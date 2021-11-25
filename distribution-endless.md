---
layout: distribution
uid: endless
title: 'Endless OS'
Category: Distribution
permalink: /distribution/endless
logo: endless.png
preview: endless.jpg
home_page: https://endlessos.com/
tagline: For Endless computing experience
desktops: [gnome]
base : [debian]
technologies: flatpak, ostree

description : Endless OS is a solid GNU/Linux distribution created from Debian base. It is powered by technologies like OSTree and Flatpak.

screenshots:
  Endless OS 3.6.0: "/1-endless-os-3.6-screenshots/"

releases :
  Endless OS 4.0.0: "/endlessos-4.0.0-release/"
  Endless OS 3.6.0: "https://community.endlessos.com/t/release-endless-os-3-6-0/9638"


---

**Endless OS** is a solid GNU/Linux distribution created from Debian base. It is powered by technologies like OSTree and Flatpak.

As different from other distributions, Endless OS does not use apt, pacman, yum or any other packaging system. It provides read-only root file system managed by OSTree with application installed using Flatpak. This will help the Endless OS to ensure each application runs in *isolation* and can't affect the functioninig of other applications. Also, the Endless OS system is write protected and can be modified by Endless OS updater only.

Endless also enforces restribtion on Flatpak sources. The flatpak packages to be installed, should be coming from either the Endless project or from GNOME project.
