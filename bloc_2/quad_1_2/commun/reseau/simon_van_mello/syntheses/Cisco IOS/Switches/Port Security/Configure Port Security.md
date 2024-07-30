Port security allows you to restrict a port's ingress traffic by limiting the MAC addresses that are allowed to send traffic through that port.
## Enable Port Security
```
Switch(config)# interface <interface>
Switch(config-if)# switchport port-security
```
## Configure maximum device(s)
```
Switch(config-if)# switchport port-security maximum <1-132>
```
## Dynamically learn MAC address
```
Switch(config-if)# switchport port-security mac-address sticky
```
> You can verify that it worked by sending packets and then issuing the `show running-config` command. You should now see the mac address in the interface section
## Violation rules
You can configure Port Security to drop packets from MAC addresses that exceed the maximum, generate a Syslog entry but not disable ports.
```
Switch(config-if)# switchport port-security violation restrict
```