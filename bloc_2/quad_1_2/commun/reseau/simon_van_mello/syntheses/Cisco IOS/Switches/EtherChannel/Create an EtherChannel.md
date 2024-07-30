When configuring EtherChannels, it is recommended to shut down the physical ports being grouped on both devices before configuring them into channel groups. Otherwise, EtherChannel Misconfig Guard may place these ports into err-disabled state. The ports and port channels can be re-enabled after EtherChannel is configured.

EtherChannels can be realised using two similar protocols: PAgP and LACP. PAgP is a proprietary Cisco protocol and LACP is an open protocol. For compatibility purposes, LACP should be preferred.
## PAgP
To create an EtherChannel using PAgP, we can put our ports in `desirable` mode to make the switch actively negotiate to form a PAgP link.
```
Switch(config)# interface range <interfaces>
Switch(config-if-range)# shutdown
Switch(config-if-range)# channel-group <number> mode desirable
Switch(config-if-range)# no shutdown
```
> Don't forget to do this on both switches even tho it might works by doing it on a single switch if the other one is in auto mode

### Configure logical interface as trunk
In most case, you are gonna want you EtherChannels to be in trunk mode. This can be done in two steps. First we need to [[Assign ports to a VLAN#Switches to switches (trunk)|put our interfaces in trunk mode]], then we can configure the logical interface as a trunk port like so:
```
Switch(config)# interface port-channel <number>
Switch(config-if)# switchport mode trunk
```
> Again, don't forget to do it on both switches
## LACP
The process to create an EtherChannel using LACP is nearly the same as it is for PAgP. We just need to replace the `desirable` mode with the `active` mode.
```
Switch(config)# interface range <interfaces>
Switch(config-if-range)# shutdown
Switch(config-if-range)# channel-group <number> mode active
Switch(config-if-range)# no shutdown
```
Configuring the newly created logical interface as trunk is exactly the same [[Create an EtherChannel#Configure logical interface as trunk|as it is for the PAgP EtherChannels.]]