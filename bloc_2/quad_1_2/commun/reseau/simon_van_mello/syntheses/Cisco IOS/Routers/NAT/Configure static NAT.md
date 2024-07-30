Here is explained how to create a static NAT translation to map a local host address to its outside address.
```
Router(config)# ip nat inside source static <local-ip> <public-ip>
```
## Configure an interface as inside/outside
```
Router(config)# interface <interface>
Router(config)# ip nat <inside/outside>
```
> The LAN interface should be inside and the WAN interface outside, obviously