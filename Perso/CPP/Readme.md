# HowtoCPP ⛢
C++ quick tutorial

## Table of contents <a name="0"></a>
0. [Table of contents](#0)
1. [Introduction](#1)
2. [The g++ compiler](#2)

The basics (CLI)

3. [Basic structure](#3)
4. [Variables](#4)
5. [In/outputs](#5)
5. [Conditions](#6)
5. [Loops](#7)
5. [Pointers](#8)
5. [References](#9)
5. [](#10)
5. [](#11)
5. [](#12)

The mid tier (OOP CLI)

5. [](#13)
5. [](#14)
5. [](#15)
5. [](#16)
5. [](#17)

Advanced (GUI)

## Introduction <a name="1"></a>

Since I'm busy learning C++, why not writing it here ?

This is hence a C++ cookbook for beginners :suspect:

## The g++ compiler <a name="2"></a>

To compile your code, use this line :

```
g++ main.cpp User.cpp -w -lSDL2 -lSDL2_ttf -o main
```

You compile two files with the dependancies ```lSDL2``` et ```lSDL2_ttf``` avec comme nom de sortie ```main```

To run your code :
```
./main
```

## Basic structure <a name="3"></a>

Any code will require a main function to work. Your working code has to be in the brackets :
```
int main(){}
```

Included packages are written like this and have to be outside the main function :

```
#include <nameofyourpackage>
```

The others functions are placed before the main function or after (in which case you will have to forward the declaration by typing the function name before the main, but with a semicolon instead of curly braces).

```
int functionplacedbefore(){}

int functionplacedafter();

int main(){}

int functionplacedafter(){}
```
A void function is a type of function in programming that does not return a value when it is executed but may perform certain tasks or operations within the program : 

```
void functionIdontWantToGetAnOutputFrom(){}
```

Every instruction you type, should have a semicolon at the end of it ```;```

## Variables <a name="4"></a>

Integers (which value can go from -2147483648 to 2147483647) are declared as :

```
int variableName = value;
```

Doubles can represent any numerical value in the compiler, including decimal values :

```
double variableName = value;
```

Floats. You can use an f placed right after the variable value to mention explicitly that the number is float. Otherwise the compiler will see it as double and which will never match to a float parameter given in the function :

```
float variableName = valuef;
```
## Inputs and outputs
## Conditions
```
if(){}
```

## Loops
Two types of loops in C++ : While and Do While.
The first one checks the condition prior to running the code inside of it :
```
while(condition){}
```
While the other runs at least one time and the condition is checked after one run of the loop :
```
do{}
while(condition);
```
The instruction to break out of a loop is simply :
```
break;
```
### Pointers 

A pointer is a variable that holds the memory address of another variable. A pointer needs to be dereferenced with the * operator to access the memory location it points to

A pointer can either be declared and initialized later :
```
int i = 3; 
int *pointer;
pointer = &i;
```

Or at the same time like this :

```
int i = 3; 
int *pointer = &i; 
```

Here is an example :
```
#include <iostream>

using namespace std;

int main()
{
int myVariable = 5;
int *pointer = &myVariable;
cout << "the pointer points towards the address " << pointer << " where is stored the value " << *pointer;

return 0;
}

```

### References

A reference variable is an alias, that is, another name for an already existing variable. A reference, like a pointer, is also implemented by storing the address of an object. 
A reference can be thought of as a constant pointer (not to be confused with a pointer to a constant value!) with automatic indirection, i.e., the compiler will apply the * operator for you.

Declare your reference like this :
```
int i = 3; 
int &reference = i;
```
⚠️ A reference is always declared and initialized in one step.


### Static Variables And Pass By Reference

You can pass an argument to a function by VALUE or by REFERENCE.
If you pass by value, a temporary copy of this value is created for the function ONLY.


### Classes and objects

> A class in C++ is a user-defined data type that encapsulates data and functions into a single unit, providing a blueprint for creating objects with specific attributes and behaviors.

And therefore, 

> An object is a specific instance of a class, which encapsulates data and methods, allowing for the instantiation and manipulation of the class's attributes and behaviors in a program.

A class is declared before the main function like this :

```
class User {
    public:
        int userId;
        string userName;
};

int main() {}
```
This class has two attributes (```userId``` and ```userName```).

Once the class is created, you can create an object :

```
class User {
    public:
        int userId;
        string userName;
};

int main() {
    User firstUser;
    firstUser.userId = 237;
    cout << firstUser.userId;
    return 0;
}
```

In the main function, we access the public attributes of the object we created (with a dot).

## Methods

Methods are functions that belong to the class.

They are either inside or outside the class definition.

Inside :
```

```

Outside :
```

```

## Constructors



## CLI advanced softwares

## GUI softwares (how to SDL)

How to install 

```
git clone https://github.com/libsdl-org/SDL.git -b SDL2
cd SDL
mkdir build
cd build
../configure
make
sudo make install
```

First we have to make a call for the most important function we will use

```
#include <SDL.h>

int main(int argc, char* args[]){
    SDL_Init(SDL_INIT_EVERYTHING);
    
    return 0;
}
```

As you can read, this function initializes the SDL library 


For creating our first window, we will use this code :

What it does :
* initializes SDL2 and if not, returns a readable error
* Creates a window and if not, returns a readable error
* Sets a boolean that defines if the window should be quitted or not
* 

```
#include <SDL2/SDL.h>

int main(int argc, char* args[]) {
    // Initialize SDL
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        printf("SDL could not initialize! SDL_Error: %s\n", SDL_GetError());
        return 1;
    }
    SDL_Window* window = SDL_CreateWindow("Tonk (master)", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 640, 480, SDL_WINDOW_SHOWN);
    if (window == NULL) {
        printf("Window could not be created! SDL_Error: %s\n", SDL_GetError());
        return 1;
    }
    bool quit = false;
    SDL_Event e;
    while (!quit) {
        while (SDL_PollEvent(&e) != 0) {
            if (e.type == SDL_QUIT) {
                quit = true;
            }
        }
        // Delay to control frame rate (optional)
        SDL_Delay(16);  // Aim for approximately 60 FPS
    }
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}

```

## Helpful links

https://www.geeksforgeeks.org/pointers-vs-references-cpp/

https://www.youtube.com/watch?v=hQ2I8D2ogrs&list=PLSPw4ASQYyynKPY0I-QFHK0iJTjnvNUys&pp=iAQB

https://www.youtube.com/watch?v=FxCC9Ces1Yg&list=PLSPw4ASQYyymu3PfG9gxywSPghnSMiOAW&pp=iAQB
