SSH should replace Telnet for management connections. Telnet uses insecure plain text communications. SSH provides security for remote connections by providing strong encryption of all transmitted data between devices.
## Commands
___
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
> The auto-completion doesn't always work for this command, idk why.
### Configure domain name
```
Switch(config)# ip domain-name domain.lan
```
### Generate rsa keys
```
Switch(config)# crypto key generate rsa
```
> You will then be asked to choose the key length, the bigger is better but remember that larger key sizes also take longer to calculate.
> Then just press enter to enable ssh.
### Change ssh version
The default ssh version is 1, we will use the version 2.
```
Switch(config)# ip ssh version 2
```
### Configure vty lines
See [[Password policy#Securise vty lines]].
### Add a new user
```
Switch(config)# username yourUsername password yourPassword
```
___
## Remote access
You should now be able to remotely access the switch using ssh.
```powershell
C:\> ssh -l yourUsername switchIP
```