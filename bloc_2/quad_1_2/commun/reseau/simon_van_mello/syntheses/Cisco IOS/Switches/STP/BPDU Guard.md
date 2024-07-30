**Bridge Protocol Data Unit** (BPDU) is a spanning tree protocol (STP) message unit which describes the switch port attributes such as MAC address, priority, and cost to achieve which allow switches to participate in the Spanning Tree Protocol to collect information from each other. **BPDU Guard** is a feature that defends the Layer 2 Spanning Tree Protocol (STP) topology against BPDU-related threats and is designed to protect the switching network. The BPDU guard feature must be activated on ports that should not receive BPDUs from connected devices.
## Enable BPDU Guard
```
Switch(config)# interface <interface>
Switch(config-if)# spanning-tree bpduguard enable
```