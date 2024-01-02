# Scaled Up Web Infrastructure

![Image of a scaled up web infrastructure](3-scale_up.jpg)

## Description

This web infrastructure represents an upscaled version of the previously described setup. In this iteration, all Single Points of Failure (SPOFs) have been eliminated. Each major component (web server, application server, and database servers) has been relocated to individual GNU/Linux servers. SSL protection isn't terminated solely at the load balancer, and every server's network is fortified by a firewall, with each server being actively monitored.

## Specifics About This Infrastructure

+ Implementation of a firewall between each server:
  - This measure safeguards each server against unwanted and unauthorized access, enhancing the overall security posture by fortifying individual servers rather than a singular one.

## Challenges With This Infrastructure

+ Increased maintenance expenses:
  - The segregation of major components onto distinct servers implies the acquisition of more hardware. This expansion leads to higher electricity consumption, thereby escalating the company's utility costs. Additional expenditure would be required for server purchases and sustaining the electricity consumption to uphold the operation of both new and existing servers.