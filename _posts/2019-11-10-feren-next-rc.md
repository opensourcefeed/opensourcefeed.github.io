---
title: "First RC released for Feren OS Next"
layout: post
categories: ferenos release
tags: ferenos release
image: "/assets/images/post-images/ferenos/feren-next-rc1.png"
---

**The** Feren OS developer has announced a release candidate for Feren OS Next. This release candidate includes a set of features and improvements that we can expect from the upcoming Feren OS stable release.

![Improved Login Screen in Feren OS Next RC1](/assets/images/post-images/ferenos/feren-next-rc1.png)
*Improved Login Screen in Feren OS Next RC1*

As different from the real *definition* of the release candidate (RC), the currently announced release is not completely free from issues. There are some known hard corners, which, however, would not affect the overall stability of the system.

## What changed from the BETA release?
There are many improvements and bug fixes since the previous BETA release for Feren OS. These improvements and bug fixes contribute to overall stability and user experience. The main highlights are briefed below.
> - The Feren OS can now installed without any internet connection. It was very annoying for the users that, Feren OS could not be installed on UEFI enabled systems without an active internet connection.
- VM Configuration is now faster and it would not take a long period for booting on virtual machines.
- The default locale is now set to en_GB UTF-8. Previously, the system was falling back to locale *C* if you don't explicitly choose any locale.
- *xdg-user-dirs-gtk* implementation is corrected and KDE Dialogs’ Places sidebar now properly lists the default places in Feren OS
- The Calamares configuration has been updated to match with HDD space requirement for Feren OS
- Splash screen & login screen can now scale properly on HiDPI devices.
- The lock screen UI has been redesigned.
- Welcome Screen > Getting Started > Keyboard Shortcuts now displays actual shortcuts.
- Plasma 5.17.2
- Removed everything that refers to the BETA release.

For [more information on Feren OS Next RC](https://medium.com/feren-os/the-first-release-candidate-of-feren-os-next-is-here-1124e51f1c5d), read the official release announcement.