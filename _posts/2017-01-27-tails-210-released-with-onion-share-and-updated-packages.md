---
layout: post
title: 'Tails 2.10 released with OnionShare and other updated packages'
categories: tails release
image: "/assets/images/post-images/tails image.png"
---
**The** Tails developers has announced release of Tails 2.10, latest maintenance release of Debian based  *amnesic incognito live system* that offers provision for anonymous and secure browsing. This release fixes many issues reported in previous releases and comes with several updated packages.

A notable highlight of Tails 2.10 is inclusion of OnionShare an anonymous file sharing tool, and  tor circuit view is enabled in tor browser which will show the nodes through which connection is made to the internet.

![Tails banner](/assets/images/post-images/tails image.png)

Other notable updates/changes in this release includes:
<blockquote>
<ul style="text-align: left;">
<li>Upgrade Tor to 0.2.9.9.</li>
<li>Upgrade Tor Browser to 6.5.</li>
<li>Upgrade Linux to 4.8. This should improve the support for newer hardware (graphics, Wi-Fi, etc.)</li>
<li>Upgrade Icedove to 45.6.0.</li>
<li>Replace AdBlock Plus with uBlock Origin.</li>
<li>Configure the APT package manage to use Debian's Onion services.</li>
<li>Install the AMDGPU display driver. This should improve the support for newer AMD graphics adapters.</li>
<li>Renamed the Boot Loader Menu entries from "Live" to "Tails", and replaced the confusing "failsafe" wording with "Troubleshooting Mode".</li>
<li>Add support for exFAT.</li>
<li>Remove Nyx (previously called arm).</li>
<li>Rewrite Tor control port filter entirely. Now Tails can safely support OnionShare, the circuit view of Tor Browser, and similar. This also enabled Whonix to replace their own similar piece of software with this one.</li>
<li>Made OnionCircuits compatible with the Orca screen reader.</li>
</ul>
</blockquote>
You can also find out [release announcement](https://tails.boum.org/news/version_2.10/index.en.html) in tails website. 