---
layout: post
title: 'Debian 9 Stretch installer rc1 released '
categories: debian release
---

**The** Debian Installer team has announced availability of first release candidate for 
Debian 9 Stretch Installer rc1. This release is coming after several alpha releases and 
can expect improved stability and robustness.

This release of Debian installer reverts the switch to merge /usr as the default configuration 
of debootstrap as it raises a number of serious issues which might not be fixed in time 
for stretch. In next release cycle, this configuration will come back.

![Debian 9 Banner](/assets/images/Debian 9.png)

In previous Alpha release (Alpha 6) Debian Pure Blends appeared in Software selection 
screen. There were some different opinions regarding this. How ever, it was n't addressed 
during the freeze as freeze is not the phase where critical screens are expected to revamp.

Following are some improvements made in this development release: 
<blockquote>
<ul style="text-align: left;">
<li>apt-setup
<br>&nbsp; - Tweak which images will offer to scan more discs.</li>
<li>brltty:<br>&nbsp; - Switch to espeak-ng.<br>&nbsp; - Add support for LXQt.<br>&nbsp; - Improve detection of USB devices.</li>
<li>cdebconf-terminal:<br>&nbsp; - Switch from ttf-dejavu-mono-udeb to fonts-dejavu-mono-udeb.</li>
<li>debian-installer:<br>&nbsp; - Add HTTPS support through new ca-certificates and wget udebs<br>&nbsp; - Switch from ttf-dejavu-udeb to fonts-dejavu-udeb.<br>&nbsp; - Switch from fonts-lklug-sinhala to fonts-noto-hinted-udeb for Sinhala<br>&nbsp; - Bump Linux kernel version from 4.7.0-1 to 4.8.0-2.<br>&nbsp; - Update theme to softWaves by Juliette Belin.</li>
<li>debian-installer-utils:<br>&nbsp; - Add checksum verification to fetch-url.</li>
<li>espeakup-udeb:<br>&nbsp; - Avoid issues with sound board names containing spaces.<br>&nbsp; - Fix race conditions when starting espeakup.<br>&nbsp; - Switch to espeak-ng (#833658).
</li>
</ul>
</blockquote>
For more details, see [original announcement](https://lists.debian.org/debian-devel-announce/2017/01/msg00004.html) published in *Debian Development* mailing list. 