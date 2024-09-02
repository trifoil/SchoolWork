For STP to converge it takes about 50 seconds i.e. to identify root bridge, root ports, blocking the port, and transition of designated to forwarding port, all these things take about 50 seconds. Now if you don’t wish to wait that long and you are absolutely sure that your topology is loop-free(and will be) you may use the feature of PortFast which is a Cisco proprietary extension to the 802.1d standard. By using PortFast the ports will transition from blocking to the forwarding state immediately.
## Enable PortFast
```
Switch(config)# interface <interface>
Switch(config-if)# spanning-tree portfast
```
## Enable PortFast by default
It is possible to enable PortFast by default on all non-trunking interfaces.
```
Switch(config)# spanning-tree portfast default
```