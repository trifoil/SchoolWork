# Tank Kommander ↯

## Intro

Aimed at RC hobby vehicles, this software equipment is meant to provide a complete remote solution to control your toy.
The concept is actually the one of a ground station.
It will give you full control of any actuator on the vehicle, provide a strong user management, reliable data transmission for a smooth user experience, while being fairly easily customized.

## Tasklist

- [ ] Get joysticks inputs and print them on terminal
- [ ] Establish a communication bridge using sockets
- [ ] Send and receive data between sockets
- [ ] Share a video stream on local network
- [ ] Read and display video stream from local network
- [ ] Imagine config file standards
- [ ] Read config file
- [ ] Create config file
- [ ] Put read and create config file together
- [ ] Nice GUI :)
- [ ] Sound options (optional)

## Features

Features include :
* Network
* Controls
* Feedback
* Video
* UI and user management
* Sound 

### Network

First approach 

The network should always be a local network, for convenience and simplicity of code.

All networks available should always be checked, to be available if an intentional (or not) change occurs. 

If network is saturated, then the user should be warned and asked if wants to reduce the amount of video channels

### Controls

The app should send control data at a high rate to the vehicle.
As a convention, the server is in the vehicle, because you can reconnect from another device, so it makes more sense.

It should be verified that data hasn't been modified or altered.

### Feedback

All useful informations from the tank should ciculate the same way control data goes in the other direction.

### Video

Video streams from the vehicle should be streamed to the network and picked by the remote unit.

### UI and user management

Two kind of users should exist :
* Master 
* Slave

The master always has control over any slave user added to control the same vehicle.

The slave can become the master if the master password is provided and the master becomes the new slave.
Config files.

The UI should be manageable by the user.

### Sound

To be developed last

## User manual 

Start by crying (because you don't possess my genius)

### Main menu

### Commands

### Views

### Users management 

## Pseudocode



a
a
a
a
a
a
a

    a
    a
    a
    a
    a
    a
    a
    a
    a
    a

## Trash

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


# TK 🛆
Tank Kommander : Open source tank remote control sofware with video feedback

The final product should include :

* Hardware
  
  * Bundle rogue
   
    * Handheld
    * Backpack (optional)
   
  * Bundle hybrid
 
    * Gamepad
    * Laptop
    * Backpack (optional)
    
  * Bundle headquarters

    * Desktop computer
    * Custom built sim, including

      * Handwheel
      * Dashboard
      * Pedals
      * Joystick
      
* Software

The project initially started using python and the following modules :

  * Pygame
  * OpenCV
  * 


## Software part

Made with love

https://www.youtube.com/watch?v=TH7plF4UT_E&list=PLSPw4ASQYyynKPY0I-QFHK0iJTjnvNUys&index=17

### Client
Includes the GUI
### Server
Embedded board 
### Arduino
Connected to the board