172.20.1.0/24

SRA: 58 hotes -> 64
SRB: 110 hotes -> 126
SRC: 20 hotes -> 32
SRD: 8 hotes -> 16
SRE: 2 hotes -> 4
SRF: 2 hotes -> 4

1. SRB 128 /25
2. SRA 64 /26
3. SRC 32 /27
4. SRD 16 /28
5. SRE 4 /30
6. SRF 4 /30

x = 172.20.1

1. net_addr => x.0/25, broadcast_addr => x.127/25, first: x.1/25, last: x.126/25
2. net_addr => x.128/26, broadcast_addr => x.191/26, first x.129/26, last: x.190/26
3. net_addr => x.192/27, broadcast_addr => x.223, first x.193/27, last: x.222/27
4. net_addr => x.224/28, broadcast_addr => x.239, first x.225/28, last: x.238/28
5. net_addr => x.240/30, broadcast_addr => x.243, first x.241/30, last: x.242/30
6. net_addr => x.244/30, broadcast_addr => x.247, first x.245/30, last: x.246/30