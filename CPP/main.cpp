#include <SDL2/SDL.h>
#include <codecvt>
#include <fstream>
#include <iostream>
#include <string>

int main(int argc, char *argv[]) {

// SDL2 init

if (SDL_Init(SDL_INIT_VIDEO) < 0) {
    SDL_Log("SDL could not initialize: %s", SDL_GetError());
    std::cout << "SDL couldn't initialize";
    return 1;
  }
std::cout << "SDL2 loaded\n";

// GUI launch

// User data extraction



return 0;
}
