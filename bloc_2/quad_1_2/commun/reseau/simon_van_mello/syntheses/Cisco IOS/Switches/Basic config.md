This a generic config that should be done in most of the cases.
## Commands
___
### Disable ip domain-lookup
By default, any single word entered on a command line that is not recognized as a valid command is considered as a hostname by the router, and the router will by default try to telnet to that hostname. This is annoying because we have to wait.
```
Switch# configure terminal
Switch(config)# no ip domain-lookup
```
### Change hostname
```
Switch(config)# hostname S1
```
### Change motd
The motd (message of the day) is the message that will be shown when a user try to connect to our device.
```
Switch(config)# banner motd #
Unauthorized access is strictly prohibited. #
```
> Note that the "#" marks the end of the message.
### Configure passwords
See [[Password policy|the password policy section]].
### Set the clock
```
Switch# clock set hh:mm:ss <1-31> MONTH <1993-2035>
```
___
## Save your config
```
Switch# copy running-config startup-config
```