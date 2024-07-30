## Undo a command
It is possible to undo every command issued on Cisco IOS using the `no` keyword.
### Example
If i have to unset an IP on a switch, after i typed the following command:
```
Switch(config-if)# ip address 192.168.1.2 255.255.255.0
```
I can simply undo it by typing the same command preceded by the `no` keyword.
```
Switch(config-if)# no ip address 192.168.1.2 255.255.255.0
```
## Erase startup-config
```
Device# erase startup-config
```
## Delete a file
We can easily delete a file by using the `delete` keyword followed by the file name.
> [[Switches files locations]]
> [[Routers files locations]]
### Example
To delete the VLAN file on a switch, we can type the following command:
```
Switch# delete vlan.dat
```