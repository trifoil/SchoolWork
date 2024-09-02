## Exclude static IPs
Addresses that have been statically assigned to devices in the networks that will use DHCP must be excluded from the DHCP pools. This avoids errors associated with duplicate IP addresses.
```
Router(config)#ip dhcp excluded-address <start-ip> <end-ip>
```
## Create a DHCP pool
```
Router(config)# ip dhcp pool <pool-name>
```
Then we can configure information such as network address, default gateway and the IP of the DNS server.
```
Router(dhcp-config)# network <network-ip> <netmask>
Router(dhcp-config)# default-router <gateway-ip>
Router(dhcp-config)# dns-server <dns-ip>
```