We can check our ACLs using the following commands:
## IP interfaces
This is the less effective way to view ACLs since its all messy but hey it works
```
Router# show ip interface
```
## Running-config
This will show you the actual rules of your ACLs + where they apply even tho its still kinda messy.
```
Router# show running-config
```
We can also apply a search pattern to reduce the amount of useless information.
```
Router# show run | include interface|access
```
## Show access-list
This will show you the actual ACLs but it won't tell you where they apply.
```
Router# show access-list
```
We can also check a specific ACL using either its number or its name with this command.
```
Router# show access-list <1-199>
Router# show access-list NAME
```
> This command will also show you the number of matches of the ACLs