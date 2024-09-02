A router could need to get an IP address from a DHCP server. For example, a router could need to get an IP from his ISP DHCP server.
```
Router(config)# interface <interface>
Router(config-if)# ip address dhcp
Router(config-if)# no shutdown
```