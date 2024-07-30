## Define a minimum password length
This will apply to all user and enable passwords.
```
Switch(config)# security passwords min-length <0-16>
```
## Encrypt passwords
```
Switch(config)# service password-encryption
```
## Enable secret
This is the password you will use to elevate privileges with the ```enable``` command. It's the same as ```enable password``` except that it is encrypted.
```
Switch(config)# enable secret yourPassword
```
## Securise console port access
### Setup a password
```
Switch(config)# line console 0
Switch(config-line)# password yourPassword
Switch(config-line)# login
Switch(config-line)# logging synchronous
```
> To prevent console messages from interrupting commands, use the **logging synchronous** option.
### Disconnect users on inactivity
```
Switch(config)# line console 0
Switch(config-line)# exec-timeout min sec
```
## Securise vty lines
### Accept ssh/telnet connections only
```
Switch(config)# line vty 0 15
Switch(config-line)# transport input ssh/telnet
Switch(config-line)# login local
```
> Use login local for ssh and login for telnet
### Setup a password
```
Switch(config)# line vty 0 15
Switch(config-line)# password yourPassword
Switch(config-line)# login local
```
> We use login local instead of just login because we want to ask for a password **and** a username (login only ask for password).
### Disconnect users on inactivity
```
Switch(config)# line vty 0 15
Switch(config-line)# exec-timeout min sec
```