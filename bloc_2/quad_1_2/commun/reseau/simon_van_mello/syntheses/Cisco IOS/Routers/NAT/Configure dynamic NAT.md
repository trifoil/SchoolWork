## Create a NAT pool
```
Router(config)# ip nat pool <pool-name> <start-ip> <end-ip> netmask <netmask>
```
## Associate an [[Create and delete an ACL|ACL]] with a NAT pool
```
Router(config)# ip nat inside source list <acl-number/name> pool <pool-name>
```
## Configure an interface as inside/outside
```
Router(config)# interface <interface>
Router(config)# ip nat <inside/outside>
```
> The LAN interface should be inside and the WAN interface outside, obviously