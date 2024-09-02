SSH should replace Telnet for management connections. Telnet uses insecure plain text communications. SSH provides security for remote connections by providing strong encryption of all transmitted data between devices.
## Commands
___
### Configure domain name
```
Router(config)# ip domain-name domain.lan
```
### Generate rsa keys
```
Router(config)# crypto key generate rsa
```
> You will then be asked to choose the key length, the bigger is better but remember that larger key sizes also take longer to calculate.
> Then just press enter to enable ssh.
### Change ssh version
The default ssh version is 1, we will use the version 2.
```
Router(config)# ip ssh version 2
```
### Configure vty lines
See [[Password policy#Securise vty lines]].
### Add a new user
```
Router(config)# username yourUsername password yourPassword
```
___
## Remote access
You should now be able to remotely access the router using ssh.
```powershell
C:\> ssh -l yourUsername routerIP
```