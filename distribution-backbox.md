---
layout: distribution
uid: backbox
title: 'BackBox Linux'
Category: Distribution
type : Linux
permalink: /distribution/backbox
logo: backbox.png
preview: backbox-preview.jpg
home_page: https://backbox.org/
desktops: [xfce]
base : [ubuntu]
description : Discover BackBox Linux, a lightweight, Ubuntu-based OS built for penetration testing and ethical hacking. Explore its curated security tools and key features.
tagline: Penetration testing distribution

releases:
  BackBox Linux 10: /backbox-linux-10-release/
  BackBox Linux 7: "/backbox-7-release/"
  BackBox Linux 6: "/1-backbox-6.0-released-screenshots/"
  BackBox Linux 5.3: "https://blog.backbox.org/2019/02/18/backbox-linux-5-3-released/"

screenshots:
  BackBox Linux 7: "/backbox-7-release/"
  BackBox Linux 6: "/1-backbox-6.0-released-screenshots/"
---

**BackBox Linux** is an open-source, Ubuntu-based Linux distribution built specifically for penetration testing, ethical hacking, and security assessments. First introduced in 2010, it pairs a lean, fast **Xfce** desktop environment with a curated set of offensive and defensive security tools—prioritizing practical workflow organization, system speed, and Ubuntu compatibility over bloat.

## Why Security Professionals Use BackBox Linux

* **Lightweight Performance & Stability:** Built on Ubuntu LTS foundations (with **BackBox Linux 10** arriving in November 2026 on an Ubuntu 26.04 LTS base with Linux 7.0 and Xfce 4.20), it keeps memory and CPU overhead low enough to run smoothly on modest hardware or virtual machines.
* **Curated, Non-Redundant Tooling:** Rather than dumping every tool imaginable into the menu, BackBox organizes essential utilities cleanly by task—covering reconnaissance, vulnerability analysis, web application testing, exploitation, binary inspection, and network forensics (including staples like Nmap, Metasploit Framework, Wireshark, sqlmap, hashcat, and ZAP, alongside newer additions such as ffuf, gobuster, and AFL++).
* **Familiar Ubuntu Ecosystem:** Because it follows standard Ubuntu/Debian packaging and repository conventions, analysts can easily install standard software, manage packages, or add custom tools without fighting an unfamiliar base OS.
* **Practical Security & Deployment Options:** The installer supports normal or minimal setups, full-disk encryption (LVM on LUKS) and ZFS, UEFI/Secure Boot hybrid ISOs, and live/VM workflows tailored for security testing.

## Common Use Cases

Security researchers, red/blue teamers, and IT administrators use BackBox Linux for authorized **network and infrastructure audits**, **web app and API security testing**, **vulnerability assessment**, **digital forensics**, and **hands-on cybersecurity training**.