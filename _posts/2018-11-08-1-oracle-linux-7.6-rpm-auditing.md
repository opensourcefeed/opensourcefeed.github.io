---
title: "Oracle Linux 7 Update 6 enable auditing for RPM managed packages"
layout: post
categories: oraclelinux release
tags: oraclelinux release
image: "/assets/images/post-images/OracleLinux-banner.jpg"
---


**Mr.** *Avi Miller* has announced the availability of Oracle Linux Update 6. It is a minor update in Oracle Linux 7.x series and brings updated packages and other minor improvements. One of the remarkable highlight of Oracle Linux 7 Update 6, or in short Oracle Linux 7.6 is the ability to track the packages installed/removed using *yum*.

![Oracle Linux banner](/assets/images/post-images/OracleLinux-banner.jpg)

### Oracle Linux 7.6 retains the compatibility with RHEL 7.x and Oracle Linux 7.x packages
As an update in Oracle Linux 7.x series, this release is compatible with previous minor updates in same series and the base distribution, ie, RHEL 7.x. The existing applications can run on this release without any modification or update. These applications won't require a recertification if it is already certified for RHEL 7.x or Oracle Linux 7.x.

### What is special in Oracle Linux 7.6?
Oracle Linux 7.6 brings a few notable highlights comparing to previous releases. The main highlights are listed below.
> - **Pacemaker** is a cluster resource manager which ensures higher availability. In Oracle Linux 7.6, Pacemaker supports path, mount, and timer as systemd unit files. Although previous releases of Pacemaker supported service and socket systemd unit files, alternative units would fail. Pacemaker can now manage path, mount and timer systemd units.
> - Package installation and upgrade using *rpm* can be tracked using *audit* events. The RPM package manager has been updated to provide audit events so that software package installation and updates can be tracked using the Linux Audit system. Software installation and upgrades using yum are also tracked.
> - Clevis is an automation encryption framework that can automatically encrypt or decrypt data, or unlock LUKS volumes. In Oracle Linux 7.6, it has been updated to support the encryption of keys in a Trusted Platform Module 2.0 (TPM2) chip. This feature is only available for x86_64 systems.

In addition to these improvements, Oracle Linux 7.6 also introduces some experimental features. These features include,
> -   Block and object storage layouts for parallel NFS (pNFS)
> -   DAX (Direct Access) for direct persistent memory mapping from an application. This is under technical preview for the ext4 and XFS file systems
> -   Multi-queue I/O scheduling for SCSI (scsi-mq). Please note that this functionality is disabled by default

For [more information on Oracle Linux 7.6](https://blogs.oracle.com/linux/announcing-the-release-of-oracle-linux-7-update-6), read the release announcement published on projects official blog.