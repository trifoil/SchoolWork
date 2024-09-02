The default configuration on the switch is to have the management of the switch controlled through vlan 1. However, a best practice for basic switch configuration is to change the management VLAN to a vlan other than vlan 1. \
For management purposes, use vlan 99. The selection of vlan 99 is arbitrary and in no way implies that you should always use vlan 99.
## Commands
___
### Create the new vlan and give it a name
We can start by [[Create a new VLAN|creating a new VLAN]] with the vlan number `99` and the name `management`.
### Assign all user ports to the vlan
```
Switch(config)# interface range gigabitEthernet 1/0/1-24
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 99
Switch(config-if-range)# exit

Switch(config)# interface range gigabitEthernet 1/1/1-4
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 99
Switch(config-if-range)# exit

Switch(config)# exit
Switch# show vlan brief
```
> The vlan 1 should now have no port in it.
