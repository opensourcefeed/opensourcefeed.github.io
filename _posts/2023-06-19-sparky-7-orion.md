---
title: "Sparky 7.0 <em>Orion Belt</em> released"
layout: post
categories: sparky release
tags:
  - debian based sparky linux
  - sparky linux updated with debian bookworm
image: /assets/images/post-images/sparky/sparky-7.0.jpg
description: Discover Sparky 7.0 "Orion Belt," the powerful and compatible operating system built on Debian 12. Upgrade or download ISO images now!
---

**The** Sparky team has announced the release of Sparky 7.0 "Orion Belt" According to the announcement, Sparky 7.0 is based on and fully compatible with Debian 12 "Bookworm." The release aims to provide users with an enhanced experience through significant updates, improved packages, and exciting features. This article will provide an overview of the key highlights of Sparky 7.0 "Orion Belt" and offer instructions for upgrading existing Sparky installations.

![Sparky 7.0 featured image](/assets/images/post-images/sparky/sparky-7.0.jpg)

## Highlights of Sparky 7.0 "Orion Belt":

The new version of Sparky, named "Orion Belt," incorporates several noteworthy features and enhancements. These include:
> 1. Based on Debian stable 12 "Bookworm":
Sparky 7.0 "Orion Belt" serves as an extension of the stable Debian 12 "Bookworm" platform. The integration ensures that users can expect a reliable and stable operating system.
2. Updated packages:
As of June 15, 2023, all packages from the Debian "Bookworm" and Sparky "Orion Belt" repositories have been updated. This encompasses security patches and software updates, ensuring users have access to the latest features and improvements.
3. Linux kernel 6.1.27 LTS as default:
The default Linux kernel for Sparky 7.0 is version 6.1.27 LTS. Furthermore, Sparky's unstable repositories offer more cutting-edge options, such as Linux kernel versions 6.3.8 and 5.15.117 LTS.
4. Enhanced software versions:
With Sparky 7.0 "Orion Belt," users will benefit from updated software applications, including:
   - Firefox 102.12.0ESR (114.0.1 in Sparky repositories)
   - Thunderbird 102.12.0
   - VLC 3.0.18
   - LibreOffice 7.4.5
5. Desktop environment choices:
To cater to diverse user preferences, Sparky 7.0 "Orion Belt" offers a range of desktop environments, including:
   - KDE Plasma 5.27
   - LXQt 1.2.0
   - MATE 1.26
   - Xfce 4.18
   - Openbox 3.6.1
6. Improved booting on UEFI motherboards:
Significant effort has been invested in enhancing the booting process for AMD64 ISO images on UEFI motherboards with Secure Boot enabled. This development allows for seamless compatibility and improved usability.
7. Sparky APTus AppCenter:
Sparky APTus AppCenter has been updated to version 20230530, making it easier for users to explore and install applications tailored to their specific needs.
8. Transition from ntp to systemd-timesyncd:
In order to streamline time synchronization, the replacement of ntp with systemd-timesyncd has been implemented, resulting in a more efficient mechanism.

## Upgrading Sparky:
For those interested in upgrading their Sparky installations, the process varies depending on the current version:

### For Sparky 6 users:
Users currently running Sparky 6 (oldstable) can choose to keep it up to date, as security updates will be provided until 2026. However, if upgrading to Sparky 7 is desired, the Wiki page provides a comprehensive upgrade guide [link]. Alternatively, an upgrade script is available by executing the following commands:

```
wget https://sparkylinux.org/files/sparky-dist-upgrade67
chmod +x sparky-dist-upgrade67
sudo ./

sparky-dist-upgrade67
```

### For Sparky 7 users:
Users who already have Sparky rolling (7) installed, which is based on Debian testing, do not need to reinstall their operating system. By keeping the system up to date, it automatically transitions to the stable release. Stay tuned for further updates on Sparky rolling, as new Debian and Sparky testing repositories will be announced separately.

## Conclusion
Sparky 7.0 "Orion Belt" delivers an array of updates, improved compatibility, and enhanced features to users. Building upon Debian 12 "Bookworm," with updated software packages and various desktop environment options, Sparky Linux continues to provide a versatile and user-friendly experience. To obtain the latest ISO images of Sparky 7.0 "Orion Belt," please visit [the official download page](https://sparkylinux.org/download/stable/). Additionally, the development of ARM images is currently underway, and updates will be shared once they are available.