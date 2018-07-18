---
title: "Managing multi-cloud services using Juju"
layout: post
categories: cloud juju
image: "/assets/images/post-images/mojo-brand-gray.png"
---

**Deploying** an application to a single cloud platform is not a very difficult task. But, it can be very challenging when we are dealing with multiple public clouds. It becomes quite difficult to handle the scalability and to troubleshoot deployment issues.

There should be some kind of robust automation for managing applications on multi-cloud platforms. This automation mechanism should be highly flexible. It should permit to do a one-time configuration and allow to deploy applications on any platform. Let it be a bare metal or a cloud container.

![Ubuntu Mirror service management using Juju](/assets/images/post-images/mojo-brand-gray.png)
*Ubuntu Mirror service management using Juju*


The *Ubuntu blog* has shared an article on managing multi-cloud platform using *Juju*.  Juju is a cloud deployment automation tool. It is responsible for talking to the cloud APIs, installation and configuration of each application, provisioning cloud services, such as security, networking, storage, and user access control. It enables scalable and efficient deployment of applications on different cloud platforms.

The article published on Ubuntu blog explains the scenario on which *Juju* was used for multi-cloud deployment. It is used to deploy Ubuntu Archive Mirror services to serve a large number of requests.

<blockquote>
All our Archive Mirror deployments are centrally managed. We have a deployment host from which all SREs connect to environments we manage. An internally developed tool allows SREs to search for the environment they need to connect to (such as “Azure Archive Mirror for Japan East region”), and then configures for them everything they need to connect to that environment in a consistent way.

The Ubuntu Archive Mirror service itself is modeled as a Mojo specification. Mojo is a system of configuration and tools for verifying the success of Juju environment deployments. It allows us to define what an Archive Mirror is in a revision-controlled configuration repository, and a means of validating whether what we deployed is as we intended.
</blockquote>
Read the complete article on [multi-cloud management using Juju](https://blog.ubuntu.com/2018/07/17/how-to-manage-multi-cloud-services-with-juju) on Ubuntu blog.