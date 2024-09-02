A multilayer switch is capable of both layer 2 switching and layer 3 routing. They can route from one VLAN to another using multiple virtual interfaces (SVIs), as well as the ability to convert a layer 2 switchport to a layer 3 interface.
## Set a port as a routed port
By default, all ports are configured to act as a switch port. We can make them act as a router ports with the following commands:
```
MLS(config)# interface <interface>
MLS(config-if)# no switchport
MLS(config-if)# ip address <network-ip> <netmask>
```
Here the `no switchport` is what's making the port go from switching to routing.
> **MLS** stands for Multilayer Switch 
