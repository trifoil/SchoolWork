Before enabling remote management with telnet, you should [[Change default VLAN|change the default vlan]] of the switch.
### Assign ip and subnet mask
```
Switch(config)# interface vlan 99
Switch(config-if)# ip address 192.168.1.2 255.255.255.0
Switch(config-if)# ipv6 address fe80::2 link-local
Switch(config-if)# ipv6 address 2001:db8:acad:1::2/64
```
### Configure the default gateway
If no default gateway is set, the switch cannot be managed from a remote network that is more than one router away
```
Switch(config)# ip default-gateway 192.168.1.1
```
> The auto-completion doesn't work for this command, idk why.
### Configure vty line
See [[Password policy#Securise vty lines]].
___
## Remote access
You should now be able to remotely access the switch using telnet.
```powershell
C:\> telnet 192.168.1.2
```