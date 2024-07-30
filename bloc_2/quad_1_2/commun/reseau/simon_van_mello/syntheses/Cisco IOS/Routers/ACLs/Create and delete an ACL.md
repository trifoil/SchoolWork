## Create an ACL
---
The order of the rules is important since the ACL will try to match the source IP from the top to the bottom.
### Standards ACLs
Standards ACLs are used to permit/deny traffic from specific hosts/networks. These ACLs numbers are in the range [1, 99].
#### Numbered standard ACL
```
Router(config)# access-list <1-99> <permit/deny> <network-ip> <wildcard-mask>
```
By default an ACL denies all traffic that does not match any rules. To permit all other traffic, we can use the following statement.
```
Router(config)# access-list <1-99> permit any
```
#### Named standard ACL
This shows you how to create a named ACL that only allow a specific host.
```
Router(config)# ip access-list standard <acl-name>
Router(config-std-nacl)# permit host <device-ip>
Router(config-std-nacl)# deny any
```
### Extended ACLs
Extended ACLs are used to permit/deny traffic from specific hosts/networks and for specific protocols to specific destinations hosts/networks. Writing an extended ACL can be quite long, i recommend you to use the `?` to get help.
#### Numbered extended ACL
I won't specify the entire command here since it's pretty easy to write with the `?`. The point here is to show you that these ACLs are in the range [100, 199].
```
Router(config)# access-list <100-199> <permit/deny> <proto> <source> <destination> ...
```
#### Named extended ACL
Again, i won't specify the entire command because of its length but i just want to show the difference between an extended named ACL and a standard named ACL.
```
Router(config)# ip access-list extended <acl-name>
Router(config-ext-nacl)# <permit/deny> <proto> <source> <destination> ...
```
## Delete an ACL
---
This will show you how to delete an ACL from a router. Note that even if your delete an ACL, you still have to [[Add and remove an ACL#Remove an ACL | remove it from your interfaces]].
### Delete all ACLs
```
Router(config)# no access-list
```
> This may or may not work (Cisco says it works but it didn't when i tried)
### Delete a specific ACL
```
Router(config)# no access-list <acl-number>
```