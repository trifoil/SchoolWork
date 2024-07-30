For DHCP clients to obtain an address from a server on a different LAN segment, the interface that the clients are attached to must include a helper address pointing to the DHCP server.
## Configure the helper address
```
Router(config)# interface <interface>
Router(config)# ip helper-address <ip>
```
> This interface is the one inside the LAN
