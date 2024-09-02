We need to assign our VLANs to subinterfaces in order to use inter-VLAN routing. To do so, we first need to **create these subinterfaces**.
```
Router(config)# interface <interface>.<subinterface>
```
Then we can **set the encapsulation type** and assign a VLAN to the subinterface.
```
Router(config-subif)# encapsulation dot1Q <vlan-number>
```
Next we can **set an ip address** on this subinterface.
```
Router(config-subif)# ip address <device-ip> <netmask>
```
> We can add the `native` keyword at the end of the command if it is the native vlan (idk why :x)

Finally we can **activate the interface** and check if the subinterfaces are also active.
```
Router(config-subif)# interface <interface>
Router(config-if)# no shutdown
Router(config-if)# end
Router# show ip interface brief
```