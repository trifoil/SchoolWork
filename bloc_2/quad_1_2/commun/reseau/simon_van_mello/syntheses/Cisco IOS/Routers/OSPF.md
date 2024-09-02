OSPF is a dynamic routing protocol used for large networks.
## Assign ip addresses
Start by assigning an ip address on each used interface of the router.

## Define router id
The rid is a 32 bits number that can be represented as an [[IPv4]] address. This id will be used to determine who is the designated router (DR). If multiple routers have the same priority, the router with the highest rid will be the DR and the second highest will be the backup designated router (BDR).
```
Router(config)# router ospf <process-id>
Router(config-router)# router-id <rid>
```
> process-id is an arbitrary number between 1 and 65565

## Activate OSPF
### Define networks
We need to specify the connected networks of the router.
#### Using network address
```
Router(config-router)# network <network-address> <wildcard-mask> area <area-number>
```
#### Using interface address
```
Router(config-router)# network <interface-address> 0.0.0.0 are <area-number>
```
### Configure interfaces
TODO: explain why we have to configure interfaces like that
(we set a router id on these routers)
```
Router(config)# interface <interface>
Router(config-if)# ip ospf <process-id> area <area-number>
```
## Changing intervals
You need to use the same intervals on each router, otherwise it wont work. These changes apply to an interface.
```
Router(config)# interface <interface>
Router(config-if)# ip ospf hello-interval <new-interval>
Router(config-if)# ip ospf dead-interval <new-interval>
```
Note that the default hello-interval is 10 and the default dead-interval is 40.
## Configure ospf to propagate default route
```
Router(config)# router ospf <process-id>
Router(config-router)# default-information originate
```
## Configure passive interfaces
If we don't want routing updates to be sent into a network, we can define an interface as passive.
```
Router(config)# router ospf <process-id>
Router(config-router)# passive-interface <interface>
```
## Configure OSPF interface priority
If we want a router interface to be the designated router, we can manually set its OSPF priority. The default priority is 1 on all routers. A router with high priority will always win the DR/BDR election process.
```
Router(config)# interface <interface>
Router(config-if)# ip ospf priority <priority-number>
```
## Configure interfaces cost
### Changing the reference bandwidth
OSPF automatic cost calculation is an inverse function of bandwidth of an interface. As higher the bandwidth values of an interface, the lower the cost value.
The interface cost can be found with this formula: 
```
Interface Cost = Reference bandwidth / interface bandwidth
```
We also know that the default reference bandwidth is 100. Knowing that, we can change interfaces cost by changing the reference bandwidth.


Example: if we want the Gigabit Ethernet interfaces cost to be 10 and the Fast Ethernet cost to be 100, we will do:
```
Router(config)# router ospf <process-id>
Router(config-router)# auto-cost reference-bandwidth 1000
```
### Directly changing the cost
We can also change the cost of an interface by setting it manually
```
Router(config)# interface <interface>
Router(config-if)# ip ospf cost <cost-number>
```
## OSPF summarization
To help reduce the size of the OSPF routing table and reduce the amount of routing informations exchanged between OSPF routers, we can implement OSPF summarization. \
Instead of advertising multiple individuals subnets, we will advertise a single summary route for all the subnets within the specified range.
```
Router(config)# router ospf <process-id>
Router(config-router)# area <area-number> range <network-ip> <netmask>
Router(config-router)# end
```
> OSPF summarization is beyond the scope of the CCNA exam