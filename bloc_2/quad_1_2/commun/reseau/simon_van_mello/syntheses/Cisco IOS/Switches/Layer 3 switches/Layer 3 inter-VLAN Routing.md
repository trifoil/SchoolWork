## Create VLANs
The process to create VLANs on a MLS is exactly the same [[Create a new VLAN|as it is for a layer 2 switch]].
## Configure trunking
Trunk configuration differs slightly on a MLS. Here the trunking interface needs to be encapsulated with the dot1Q protocol, however it is not necessary to specify VLAN numbers as it is when working with a router and [[Subinterfaces configuration|subinterfaces]].
```
MLS(config)# interface <interface>
MLS(config-if)# switchport mode trunk
MLS(config-if)# switchport trunk native vlan <vlan-number>
MLS(config-if)# switchport trunk encapsulation dot1Q
```
## SVIs configuration
In order to route traffic between our VLANs, we are gonna use switched virtual interfaces (SVIs).
```
MLS(config)# interface vlan <vlan-number>
MLS(config-if)# ip address <device-ip> <netmask>
MLS(config-if)# ipv6 address <device-ipv6>/<netmask>
```
Then we can check if any mistake was made.
```
MLS# show ip interface brief
```
## Enable routing
Routing is disabled by default. This can be confirmed by issuing the following command.
```
MLS# show ip route
MLS# show ipv6 route
```
This should show an empty routing table. \
We can enable routing to allow traffic to go from a VLAN to another with the `ip routing` command.
```
MLS(config)# ip routing
MLS(config)# ipv6 unicast-routing
```
Finally, we can confirm it worked by issuing the `show ip(v6) route` command again. This should show the routes between the VLANs.