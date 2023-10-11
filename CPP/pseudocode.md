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



3) Storage
* A "userconfig.csv" file has to be created if it doesn't exist and contains data
    * 



4) Startup sequence for the software :

    1) Initialize the SDL2 librairy
    2) Check if there is a config file in the same edirectory
        * If it doesn't exist, create it
        * If it exists, decrypt the config file withe the key provided in the version of the software
    4) In both cases, check if a userId exists in the config file
    5) In any case,  prompt the user :
        * "Create a user"
        * "Proceed without user (limited use only)" that will only work in local mode
        * "Choose a user" only available if a config file already exists AND contains a userId