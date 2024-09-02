When using cisco ios commands, you can choose to display only specifics patterns of research, just like grep on linux. \
To do so, you just need to add a **|** after your command and type the keyword with a search pattern.
## Keywords
### Include
The include keyword will return each line containing the given pattern.
Example:
```
Switch# show running-config | include hostname
```
This return:
```
hostname Switch
```
### Exclude
The exclude keyword will return each line that does **not** contains the pattern.
Example:
```
Switch# show running-config | exclude hostname
```
This will return every line of the ```show running config``` command except the one containing the hostname.
### Begin
This return the all the lines after the first line containing the pattern.
Example:
```
Switch# show running-config | begin interface
```
This return:
```
interface GigabitEthernet0/0/0
description Connection to SW1
ip address 172.16.20.1 255.255.255.128
duplex auto
speed auto
!
interface GigabitEthernet0/0/1
description Connection to SW2
ip address 172.16.20.129 255.255.255.128
duplex auto
speed auto
...
```