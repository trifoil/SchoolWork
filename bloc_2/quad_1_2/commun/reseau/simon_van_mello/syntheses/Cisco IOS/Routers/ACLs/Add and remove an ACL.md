ACLs are cool, even more if we know how to apply them :p
## Add an ACL
Before applying an ACL to an interface, you should [[Display ACLs#Show access-list|review the content of the access list]].
### ACL on interface
Once you are sure that your rules are correct, you can apply the ACL to an interface like so:
```
Router(config)# interface <interface>
Router(config-if)# ip access-group <acl-number/name> <direction>
```
> **direction** is either out or in
### ACL on vty line
```
Router(config)# line vty 0 15
Router(config-line)# access-class <acl-name> <direction>
```
## Remove an ACL
To remove an ACL from an interface, you first need to [[Display ACLs#Running-config|check which ACL you want to remove]]. Then you can remove it like this:
```
Router(config)# interface <interface>
Router(config-if)# no ip access-group <acl-number> <direction>
```