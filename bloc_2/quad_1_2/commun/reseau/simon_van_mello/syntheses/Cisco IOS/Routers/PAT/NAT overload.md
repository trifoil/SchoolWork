NAT overload allows multiple devices on a local network to use the same inside global IP to communicate with outside networks by using different ports.

## Create an ACL
We first need to create an ACL that we are gonna associate with our NAT pool. Example:
```
Router(config)# access-list 1 permit 172.16.0.0 0.0.255.255
```
## Configure a pool of address
Then we can create an address pool like for regular dynamic NAT.
```
Router(config)# ip nat pool <pool-name> <start-ip> <end-ip> netmask <netmask>
```
## Associate ACL to the NAT pool and overload
NAT overloading allows addresses to be used by multiple devices using different ports.
```
Router(config)# ip nat inside source list <acl-number/name> pool <pool-name> overload
```
## Configure an interface as inside/outside
```
Router(config)# interface <interface>
Router(config)# ip nat <inside/outside>
```
> The LAN interface should be inside and the WAN interface outside, obviously
## Check if working
To check if the NAT overload, you can try to send to requests from multiple LAN devices and type the following commands to see if they use the same address:
```
Router# show ip nat translations
```