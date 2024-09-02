## Create an ACL
We first need to create an ACL that we are gonna associate with our interface. Example:
```
Router(config)# access-list 2 permit 172.16.0.0 0.0.255.255
```
## Associate ACL to interface
```
Router(config)# ip nat inside source list <acl-number> interface <interface> overload
```
## Configure an interface as inside/outside
```
Router(config)# interface <interface>
Router(config)# ip nat <inside/outside>
```
> The LAN interface should be inside and the WAN interface outside, obviously