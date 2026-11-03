---
layout: distribution
uid: opensuse
title: 'openSUSE'
Category: Distribution
type : Linux
permalink: /distribution/opensuse
logo: openSUSE.svg
preview: opensuse-laptop.jpg
home_page: https://www.opensuse.org/
desktops: [gnome, plasma, xfce]
base : Independent
tagline: Leap and Tumbleweed news and reviews

description : "openSUSE is a community-developed Linux distribution sponsored by SUSE. Read about Leap and Tumbleweed releases, reviews, screenshots and FAQs."

releases :
  # TODO: add openSUSE Leap 15.6 once the post is available, e.g. openSUSE Leap 15.6: /your-leap-156-post/
  openSUSE Leap 16.1: /opensuse-leap-16-1-release/
  openSUSE Leap 16: /opensuse-leap-16-release/
  openSUSE Leap 15.5: /opensuse-leap-155-release/
  openSUSE Leap 15.4: "/opensuse-leap-154-has-been-released/"
  openSUSE Leap 15.2: "/opensuse-leap-15.2/"
  openSUSE Leap 15: "https://open-source-feed.blogspot.com/2018/05/opensuse-leap-15-released-based-on-suse.html"
  openSUSE Leap 42.3: "https://open-source-feed.blogspot.com/2017/07/opensuse-leap-423-released-with-better.html"

reviews:
  openSUSE Tumbleweed Xfce, Pros & Cons: "/opensuse-tumbleweed-review/"
  openSUSE Leap 42.2: "https://open-source-feed.blogspot.com/2017/02/opensuse-leap-422-is-extremely-stable.html"
  openSUSE Leap 42.2 GNOME: "https://open-source-feed.blogspot.com/2017/02/opensuse-leap-422-gnome-flavor-is.html"

screenshots:
  openSUSE Leap 15.2 GNOME: "/opensuse-leap-15.2-gnome/"
  openSUSE Leap 15.2 Plasma: "/opensuse-leap-15.2-plasma/"
  openSUSE Tumbleweed Xfce: "/opensuse-tumbleweed-review/"
  openSUSE Leap 15.1 Plasma: "/1-opensuse-leap-15.1-plasma-screenshots/"

faq:
  "What is the difference between openSUSE Leap and Tumbleweed?": "Leap is the fixed-release edition. It shares its core with SUSE Linux Enterprise (SLE) and gets conservative, tested updates. Tumbleweed is a rolling release that delivers new upstream software as soon as it passes testing. Choose Leap for servers and stable desktops, and Tumbleweed if you want the latest software."
  "Is openSUSE Leap 15.6 still supported?": "No. Leap 15.6 was the last release of the Leap 15 series and reached end of life on 30 April 2026. Upgrade to <a href='/opensuse-leap-16-release/'>openSUSE Leap 16</a> or move to Tumbleweed."
  "What is new in openSUSE Leap 16?": "Leap 16.0 was released on 1 October 2025. It is built on SUSE Linux Enterprise 16, uses the new Agama installer, enables SELinux by default (AppArmor is still available), and requires a CPU with x86-64-v2 support, which generally means hardware from 2008 or later."
  "How to install Budgie Desktop in openSUSE": "You can download GeckoLinux Budgie Edition (an openSUSE derivative) or follow the steps on the <a href='https://en.opensuse.org/Budgie' rel='nofollow'>openSUSE wiki page for Budgie</a>."
---

<!-- VERIFY: Budgie FAQ. The original also mentioned enabling Solus repositories on OBS; this is removed until the method is confirmed. -->

**openSUSE** is a community-developed Linux distribution sponsored by SUSE. It is known for stable releases, strong packaging tools and a rolling edition for people who want current software. The project is independent, so it does not depend on another distribution.

Two tools set openSUSE apart. The *Open Build Service* (OBS) builds packages for openSUSE and for other distributions such as Fedora, Ubuntu and Debian. The *zypper* package manager handles installs and updates. Leap 15 users also know *YaST*, the system configuration and installation tool. <!-- VERIFY: YaST status on Leap 16 and Tumbleweed -->

## openSUSE Leap and Tumbleweed

openSUSE comes in two editions, and the choice depends on how much change you want.

- **Leap** is the stable, fixed-release edition. It shares core packages with SUSE Linux Enterprise (SLE) and gets security and maintenance updates from the community and SUSE. It suits servers, workstations and anyone who wants few surprises.
- **Tumbleweed** is the rolling edition. It ships new kernels, desktops and tools soon after upstream releases them. It suits developers and enthusiasts who want current software.

If you want a middle path, the project also offers Slowroll, a slower rolling release.

## What's new in openSUSE Leap 16

[openSUSE Leap 16](/opensuse-leap-16-release/) was released on 1 October 2025 and changes a lot compared with Leap 15:

- **New installer**: Agama replaces the YaST-based installer.
- **SELinux by default**: AppArmor remains available as an option after installation.
- **Longer lifecycle**: each release gets 24 months of support, and the series is planned to run until Leap 16.6 in 2031.
- **Desktops**: Leap 16.0 offers KDE Plasma 6.4, GNOME 48 and Xfce 4.20.
- **Hardware requirement**: x86-64-v2 or newer, which generally means CPUs from 2008 or later.

**Leap 16.1 is next.** It is in the release candidate phase, with general availability planned for November 2026. It adds an immutable mode for container and VM hosts and updates KDE Plasma to 6.6. We will add a link here after it is released.

**Leap 15 users:** Leap 15.6, the last Leap 15 release, reached end of life on 30 April 2026. If you still run it, plan your move to Leap 16 or Tumbleweed.

## Download openSUSE

You can download Leap and Tumbleweed images from the [official openSUSE download page](https://get.opensuse.org/). Leap images come as a large offline image or a small network installer.

## Desktop environments

openSUSE supports several desktops. See our pages for [GNOME](/desktop/gnome), [KDE Plasma](/desktop/plasma) and [Xfce](/desktop/xfce) to compare them.

## More from OpenSourceFeed

Looking for apps to run on openSUSE? Browse the [software directory](/software/) or see our [open source alternatives](/software/alternative-to/). To compare openSUSE with other systems, visit [all operating systems](/distribution/) or use the [Distro Finder](/distro-chooser/).