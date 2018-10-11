---
title: "Kali Linux is now officially available for Vagrant"
layout: post
categories: kali release
image: "/assets/images/post-images/kali-on-vagrant.jpg"
---

**Inspired** by the efforts of the community to run Kali in Vagrant, the Kali Linux team has introduced officially maintained images for Vagrant Cloud. This will enable users to install and configure Kali Linux on multiple Virtual Machines with a single configuration script.

![Kali on Vagrant Cloud banner](/assets/images/post-images/kali-on-vagrant.jpg)

### What is Vagrant?
Vagrant is basically a tool that helps to create and manage virtual machine environments easily. It can be considered as a configuration file that can be used to configure multiple virtual machines in an identical way. The Vagrant tasks can include the downloading of the base platform, installation, configuring the virtual machine, and running scripts on first boot.

### How to use Kali with Vagrant?
VirtualBox and Vagrant are prerequisites for running Kali Linux on Vagrant. After installing both these tools, a base configuration file can be created by running the following command.

```
$ vagrant init offensive-security/kali-linux
A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.
```

This will create a configuration file named *Vagrantfile* in the current directory. It includes the basic image specification only. Other options are available as comments and can be configured as per the requirement.

The Kali Linux team has shared a blog post on Kali for Vagrant. This gives a brief idea on different configuration options available. Later, the project will publish detailed documentation for the same.
> This will create a file named Vagrantfile, which contains all the configuration options for the virtual machine. Every ‘vagrant’ command must be run from the directory containing that file. By default, it contains only the box name as well as many commented common options. We’ll review some of those later, but here is an excerpt. <br/>
Vagrant will first download the box file if it’s not in its cache, then create the Kali VM and power it on. You will see the VirtualBox UI pop up so you can use Kali normally with the root/toor credentials.<br/>
Vagrant veterans might notice that the VM is not headless, unlike most other Vagrant boxes. We have decided to show the GUI by default because many Kali tools require it. If you do not need the GUI, you can disable it in the Vagrantfile (see below for an example config) and run the following command to SSH to the machine as the vagrant user.

For further details on [Kali Linux for Vagrant](https://www.kali.org/news/announcing-kali-for-vagrant/), see the original blog post on Kali Linux website.