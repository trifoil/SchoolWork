There is two ways to modify an ACL. The first one is deleting the entire ACL and recreating it. This is not very efficient. The second way is more efficient
## Deleting the entire ACL
```
Router(config)# no ip access-list standard <acl-name>
```
## Appending new ACEs
First we need to [[Display ACLs#Show access-list|check the numbers of the current ACEs]]. Then we just have to specify the numbers of the new rules. For example, let's say we have the following ACEs:
```
Router# show access-lists
Standard IP access list BRANCH-OFFICE-POLICY
    10 permit 192.168.30.3 (8 matches)
    20 permit 192.168.40.0 0.0.0.255 (5 matches)
```
We could add new rules like so:
```
Router(config)# ip access-list standard BRANCH-OFFICE-POLICY
Router(config-std-nacl)# 30 permit <network-ip> <wildcard-mask>
Router(config-std-nacl)# 40 deny any
```