---
title: "Exploring Manjaro Cutefish; screenshots and video tour"
layout: post
categories: manjaro cutefish
tags: 
  - Manjaro Cutefish
  - macOS like linux desktop
  - Userfriendly Linux
  - How to install Manjaro Cutefish
  - Manjaro Cutefish screenshots
  - Cutefish screenshots
image: /screenshots/Manjaro Cutefish Intro/09 Appearance Settings.jpg
video: https://www.youtube.com/embed/bjhMvuetl6M 
---

**The** Cutefish Desktop is an emerging desktop environment for the GNU/Linux ecosystem. It aims to offer a more intuitive and familiar experience for the majority of users.

![Manjaro Cutefish featured image](/screenshots/Manjaro Cutefish Intro/09 Appearance Settings.jpg)

Cutefish Desktop is actively developed by the CutefishOS team and, it is expected to be the flagship desktop of CutefishOS. The CutefishOS project is still in the development phase. So, for the early birds, There are two unofficial respins of CutefishOS with Ubuntu and Manjaro foundations.

- [Download Manjaro with Cutefish Desktop](https://github.com/manjaro-cutefish/download/releases)
- [Download Ubuntu with Cutefish Desktop](https://cutefish-ubuntu.github.io/download/)

Cutefish Desktop takes its inspiration from the macOS/iOS designs. It offers a global menu, dock, launchpad application menu, and a system menu. Just like the recent desktop environments, it also provides the option to choose between a dark and light theme with a color accent.

## How to download ISO for the Manjaro Cutefish?
Manjaro Cutefish images are hosted in a Github repository. The images are split into multiple parts because the Github recommendation is to keep the file size below 2GB.

For preparing the working ISO, you may follow the steps below.

1. Visit the [Manjaro Cutefish release](https://github.com/manjaro-cutefish/download/releases) page in Github.
2. Download both the .iso.zip and .iso.z01 into the same directory.
3. Open that directory in the terminal.
4. Run the below command in terminal.
```sh
zip -s- manjaro-cutefish-21.08-development-unstable-minimal-210819-linux513.iso.zip -O combined.zip
```
5. Extract the combined.zip archive to get the .iso

## Manjaro Cutefish screenshots
{% include image-gallery.html folder="/screenshots/Manjaro Cutefish Intro" %}
