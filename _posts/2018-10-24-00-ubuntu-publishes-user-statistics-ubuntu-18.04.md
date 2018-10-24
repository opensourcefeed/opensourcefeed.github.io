---
title: " Ubuntu publishes the user statistics for Ubuntu 18.04 <em>Artful Aardvark</em>"
layout: post
categories: ubuntu news
tags: ubuntu release
image: "/assets/images/post-images/ubuntu-statistics/user-locations.png"
---

**In** past years, Ubuntu has faced a lot of criticism for collecting user information and sharing it with 3rd parties for the commercial purpose. This forced the Ubuntu team to place an OPT-IN for users to allow data sharing with 3rd parties. Later, Ubuntu introduced a feature for collecting the installation preferences of users. This is also an OPT-IN feature but is enabled by default. Now, Ubuntu has published a user statistics report which showcases the user preferences while installing Ubuntu 18.04 <em>Artful Aardvark</em>

Let's try to get a quick summary of Ubuntu 18.04 user statistics.

### User Info

#### How many users opted-in for data collection?

![Users opted-in for data collection](/assets/images/post-images/ubuntu-statistics/opted-in-users.png)

Ubuntu 18.04 with the OPT-IN option enabled by default and it can be disabled by users at the beginning of the installation. As per statistics, 66% of users decided to proceed with data collection enabled, while the remaining section decided to not. Majority of these users were installing Ubuntu on physical machines.

In privacy policies, it is clearly mentioned that the data collected will be used only for development purpose and to improve the user experience.

#### Fresh installation or upgrading?

![Fresh installation or upgrade](/assets/images/post-images/ubuntu-statistics/install-or-upgrade.png)

While 80% of users decided to do a fresh installation and 20% decided to upgrade their existing installation. It should be noted that users who install on Virtual Machines will mostly prefer to do the fresh installation unless they are doing the regression on the upgrade process.

#### Where are Ubuntu users located?

![Ubuntu user locations](/assets/images/post-images/ubuntu-statistics/user-locations.png)

Ubuntu collects the user location information based on the location and the time zone selected during installation. The IP address is not used for identifying users location.

Based on this, Ubuntu users are present everywhere. They are densely located in regions like Russia, South America, Australia and some parts of Africa.

#### Primary language used on computers

![Primary language of Ubuntu users](/assets/images/post-images/ubuntu-statistics/language-used.png)

Around 59% of Ubuntu users stick with English as the default language. Spanish, French, Portuguese and Chinese languages hold the next positions.

### Desktop specifications
The user information was collected based on the options selected during installation. Desktop specifications are directly taken from the system.

#### OS architecture

![Ubuntu OS architecture](/assets/images/post-images/ubuntu-statistics/os-architecture.png)

Ubuntu provides both 64-bit and 32-bit installation images. With the advent of technology, 98% of users chose the 64-bit operating system and the remaining 2% chose 32-bit systems. The 32-bit systems were mostly chosen because of hardware limitations.

#### Display server technology

![Display server](/assets/images/post-images/ubuntu-statistics/display-server.png)

The display server is something that regulates the input and output of its clients from the hardware and the operating system. When 99% of users stuck with X11, 1% users opted for Wayland. Wayland is a new generation display technology.

#### Firmware

![Firmware used](/assets/images/post-images/ubuntu-statistics/firmware.png)

Firmware is a hardware-software that loads the operating system and initialize the hardware on start.

On physical machines, more than 40% of users had UEFI enabled, while on virtual machines, more than 80% had BIOS (the legacy bootloader).

#### Graphics & Display

![Graphics & Display](/assets/images/post-images/ubuntu-statistics/display-graphics.png)

Based on the information collected during installation, 93% of users are having single screen setup. This can't be accurate as most of the users connect secondary displays after the installation. Also, 94% of users were operating systems with single GPU (Graphical Processing Unit). GPU is a component that performs the display related operations.

### Customized Ubuntu installation

During the installation, Ubuntu provides various ways for customizing the system. This includes downloading updates during installation, enabling auto-login ..etc

![Installation with default settings](/assets/images/post-images/ubuntu-statistics/default-settings.png)

On physical machines, 33% of users installed with default configurations. While on virtual machines 61% users adopted the default configurations.

![Auto-login](/assets/images/post-images/ubuntu-statistics/auto-login.png)

29% of users decided to enable auto-login on startup. Auto-login allows the users to load desktop without entering the password. 

![Minimal installation](/assets/images/post-images/ubuntu-statistics/minimal-install.png)

Ubuntu minimal installation provides a basic system with a few applications. 12% and 13% of users selected this option for installation, on physical systems and virtual machines respectively.

![Update packages while installing](/assets/images/post-images/ubuntu-statistics/update-while-installing.png)

Ubuntu installer provides the option to download updates before starting the installation. 93% of users decided to select this option. The percentage is the same on physical machines and on virtual machines.

You can find the [complete Ubuntu statistics](https://www.ubuntu.com/desktop/statistics) along with the graphical illustration on Ubuntu blog.
