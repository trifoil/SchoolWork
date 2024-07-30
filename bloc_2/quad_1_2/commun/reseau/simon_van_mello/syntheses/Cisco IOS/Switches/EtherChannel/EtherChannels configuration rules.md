EtherChannel has some specific guidelines that must be followed in order to avoid configuration problems.
1. All Ethernet interfaces support EtherChannel up to a maximum of eight interfaces with no requirement that the interfaces be on the same interface module.
2. All interfaces within an EtherChannel must operate at the same speed and duplex.
3. EtherChannel links can function as either single VLAN access ports or as trunk links between switches.
4. All interfaces in a Layer 2 EtherChannel must be members of the same VLAN or be configured as trunks.
5. If configured as trunk links, Layer 2 EtherChannel must have the same native VLAN and have the same VLANs allowed on both switches connected to the trunk.
6. When configuring EtherChannel links, all interfaces should be shutdown prior to beginning the EtherChannel configuration.  When configuration is complete, the links can be re-enabled.
7. After configuring the EtherChannel, verify that all interfaces are in the up/up state.
8. It is possible to configure an EtherChannel as static, or for it to use either PAgP or LACP to negotiate the EtherChannel connection.  The determination of how an EtherChannel is setup is the value of the **channel-group** _number_ **mode** command.  Valid values are:
```
active -> LACP is enabled unconditionally
passive -> LACP is enabled only if another LACP-capable device is connected.
desirable -> PAgP is enabled unconditionally
auto -> PAgP is enabled only if another PAgP-capable device is connected.
on -> EtherChannel is enabled, but without either LACP or PAgP.
```
9. LAN ports can form an EtherChannel using PAgP if the modes are compatible.  Compatible PAgP modes are:
```
desirable -> desirable
desirable -> auto
```
> If both interfaces are in auto mode, an EtherChannel cannot form

10. LAN ports can form an EtherChannel using LACP if the modes are compatible.  Compatible LACP modes are:
```
active -> active
active -> passive
```
> If both interfaces are in passive mode, an EtherChannel cannot form using LACP

11. Channel-group numbers are local to the individual switch. Channel-group 1 (interface po1) on one switch can form an EtherChannel with Channel-group 5 (interface po5) on another switch.