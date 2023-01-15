---
title: How to install helloSystem on Kubuntu or Ubuntu
image: /assets/images/post-images/hello/building-on-linux.png
description: A tutorial explaining how to install helloSystem - a mac inspired desktop environment for BSD in a famous GNU/Linux distribution like Ubuntu or Kubuntu.
layout: post
categories: helloSystem tutorial
tags: 
  - Installing helloSystem on Linux
  - Mac inspired desktop environment for linux
video: https://www.youtube.com/embed/vzX7yHB1i1U
---

**helloSystem** is a project that combines a desktop environment and operating system to create a user-friendly and visually pleasing desktop experience. The design of helloSystem is inspired by the early design principles of Mac OS. This tutorial will guide you on how to install helloSystem on either Kubuntu or Ubuntu.

![helloSystem about dialog in Kubuntu](/assets/images/post-images/hello/building-on-linux.png)

Although helloSystem is designed to be used with the helloSystem operating system, which is based on FreeBSD, the developers are working to make the project reasonably platform-independent. It is possible to build helloSystem on GNU/Linux, and there is an official tutorial on building helloSystem on Alpine Linux in the documentation.

This tutorial will focus on installing helloSystem on Kubuntu as Alpine Linux is not a popular option. If you choose to use Ubuntu, be sure to install the Plasma Desktop before proceeding with the instructions.

Please note that these instructions should not be used on a production system. Instead, use VirtualBox or a USB live boot. You can also refer to the accompanying video tutorial for more guidance.

```bash
# Switch to root mode
sudo su

# Configure source repositories in the open window
# Use software-properties-gtk if using Ubuntu
software-properties-qt

# Install build dependencies for dolphin to reduce number of dependencies need to be installed while making the helloSystem components
apt build-dep  dolphin

git clone https://github.com/helloSystem/launch
mkdir -p launch/build
cd launch/build
cmake ..
make -j $(nproc) install
cd ../..

git clone https://github.com/helloSystem/Menu
mkdir -p Menu/build
cd Menu/build
apt install libqt5x11extras5-dev qttools5-dev xcb libxcb-util-dev libxcb-damage0-dev libxcomposite-dev libxdamage-dev libxrender-dev libxcb-ewmh-dev libdbusmenu-qt5-dev qtdeclarative5-dev libprocps-dev
cmake ..
make -j $(nproc) install
cd ../..

git clone https://github.com/helloSystem/Filer
mkdir -p Filer/build
cd Filer/build
apt install qtmultimedia5-dev pkg-config libfm-dev libmenu-cache-dev
cmake ..
make -j $(nproc) install
cd ../../

# Start the helloSystem components
launch Menu &
sleep 1
launch Filer &
killall plasmashell

```

*The content is partially phrased by OpenAI's GPT-3*