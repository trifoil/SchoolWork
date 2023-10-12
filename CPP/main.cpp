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

        // still to do

  // User data file check

  std::ifstream file("userconfig.txt");
  if (file.is_open()) {
    std::cout << "File 'userconfig.txt' exists in the current directory.\n";
  } else {
    std::ofstream newFile("userconfig.txt");
  }

  // USer data extraction

  // User checking

  // User selection prompt

  return 0;
}
