#include <SDL2/SDL.h>
#include <fstream>
#include <iostream>
#include <string>

int main(int argc, char *argv[]) {

if (SDL_Init(SDL_INIT_VIDEO) < 0) {
    SDL_Log("SDL could not initialize: %s", SDL_GetError());
    return 1;
  }
}