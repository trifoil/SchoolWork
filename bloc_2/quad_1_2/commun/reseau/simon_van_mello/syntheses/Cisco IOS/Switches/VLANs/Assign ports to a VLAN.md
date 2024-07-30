## Swiches to end devices
### Regular VLAN
```
Switch(config)# interface <interface>
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan <vlan-number>
```
> The access mode means that the interface will only carry traffic for a single VLAN. It is generally used to connect end devices to a switch.
### Voice VLAN
A switch interface can be configured to support user traffic and voice traffic at the same time. This interface must enable Qos and trust the Class of Service (CoS).
```
Switch(config)# interface <interface>
Switch(config-if)# mls qos trust cos
Switch(config-if)# switchport voice vlan <vlan-number>
```
## Switches to switches (trunk)
If we want our switches to be able to transit VLANS traffic, we need to define the ports between theses switches as trunk. Trunks allow the traffic from multiples VLANs to travel over a single link while keeping the VLAN identification and segmentation.
### Example
To explain how to configure trunking ports, we are gonna use this topology with VLAN 99 as the native VLAN.
![[Pasted image 20230525164719.png]]
### Configure ports for trunking manually
Firstly, we are gonna set the S1 ports as trunking ports.
```
S1(config)# interface range g0/1-2
S1(config-if)# switchport mode trunk
S1(config-if)# switchport trunk native vlan 99
S1(config-if)# switchport nonegociate
```
> The `switchport nonegociate` disable DTP

Then, on S2 and S3, we need to set the ports connected to S1 as trunking port even tho the Dynamic Trunking Protocol (DTP) should have set these port on auto mode. \
We can verify that the DTP have set the ports on `auto` mode with this command:
```
S2# show interfaces trunk
```
The process to set a port as trunk is the same on all the switches but im gonna show it again. On S2:
```
S2(config)# interface g0/1
S2(config-if)# switchport mode trunk
S2(config-if)# switchport trunk native vlan 99
```
Now if we re-check the trunk state:
```
S2# show interfaces trunk
```
We should see that the port is on `on` mode instead of `auto` and that the native VLAN went from 1 to 99.
### Configure ports for trunking using DTP
Since the default DTP mode of a Cisco switch is `dynamic auto`, we can simply set one of the port between two switches in `dynamic desirable` mode to negotiate a trunk link. \
In the example, we could set the g0/1 of S1 on `dynamic desirable` to negotiate the trunk link.
```
S1(config)# interface g0/1
S1(config-if) switchport mode dynamic desirable
```
If we issue the `show interfaces trunk` command on S2, we could see that the trunk is on auto mode.
> This method is easy to setup but is to be avoided since it only works with Cisco devices
### Configure allowed VLANs
To improve security, we are gonna restrict the allowed VLANs. This is not really relevant in our example since we don't have implemented inter-VLAN routing.
```
S1(config)# interface g0/1
S1(config-if)# switchport trunk allowed vlan 10,20,30,99
```
#### More relevant example
In the following example, we are going to allow every VLAN to go from S1 to the router so that the router can perform inter-VLAN routing and we allow VLANs 3 and 13 to go from S1 to S2 because VLANs 3 and 13 are the only one in this direction.
![[Drawing 2023-05-26 13.31.24.excalidraw|center]]
> **Blue numbers** represents allowed VLANs and **green numbers** represents devices VLANs.