HSRP stands for Hot Standby Router Protocol. It is a Cisco proprietary protocol used to provide redundancy in a network. The purpose of HSRP is to ensure that if one router fails, another router can take over its duties seamlessly without disrupting network connectivity. It is a FHRP.
## Configure HSRP on a LAN interface
### Specify the HSRP version
The most recent version is version 2.
```
Router(config)# interface <interface>
Router(config-if)# standby version 2
```
> The interface should be the one inside the LAN
### Configure virtual gateway IP
This will be the IP used by the hosts as their default gateway.
```
Router(config-if)# standby <group-number> ip <virtual-gateway-ip>
```
### Designate the active router
The default HSRP priority is 100. A higher value will determine which router is the active router.
```
Router(config-if)# standby <group-number> priority <priority>
```
> If the priorities of the routers in the HSRP group are the same, then the router with the highest configured IP address will become the active router.
### Allow the designated router to resume his role (optionnal)
If it is desirable that the active router resume that role when it becomes available again, configure it to preempt the service of the standby router. The active router will take over the gateway role when it becomes operable again.
```
Router(config-if)# standby <group-number> preempt
```