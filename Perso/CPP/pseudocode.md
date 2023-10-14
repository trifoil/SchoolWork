# Tonk pseudocode 

1) Menu
* Main menu
    * User management
    * User settings
        * Interface settings
        * Commands settings
    * Quit 
2) Interface
* Camera view 
* 
3) Network
* Local network
* Internet peer to peer
* VPN
4) Storage



## Tasklists

1) Startup sequence for the software :

- [x] Initialize the SDL2 librairy
- [ ] Launch the GUI and display "extracting user data"
- [ ] Check if there is a config file in the same edirectory
    * If it doesn't exist, create it
    * If it exists, decrypt the config file withe the key provided in the version of the software
- [ ] Display "config file ready"
- [ ] In both cases, check if a userId exists in the config file
- [ ] In any case,  prompt the user :
    * "Create a user"
    * "Proceed without user (limited use only)" that will only work in local mode
    * "Choose a user" only available if a config file already exists AND contains a userId 