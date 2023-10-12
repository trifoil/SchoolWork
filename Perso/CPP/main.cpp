#include <SDL2/SDL.h>
#include <codecvt>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

// User class

class User {
public:
  string username;
  string userId;
  int configLayout;
  int cameraView;
  int connectionType;

  User(const std::string &name)
      : username(name), configLayout(0), cameraView(0) {}
};

int main(int argc, char *argv[]) {

  // SDL2 init

  if (SDL_Init(SDL_INIT_VIDEO) < 0) {
    SDL_Log("SDL could not initialize: %s", SDL_GetError());
    cout << "SDL couldn't initialize";
    return 1;
  }
  cout << "SDL2 loaded\n";

  // GUI launch

  // User data file check

  ifstream file("userconfig.txt");
  if (file.is_open()) {
    cout << "File 'userconfig.txt' exists in the current directory.\n";
  } else {
    ofstream newFile("userconfig.txt");
  }

  // User data extraction

  // User checking

  // User selection prompt
  cout << "users have been found in the config file";
  cout << "do you want to select one (1) or create one (2)";
  cout << "no user exists in the config file";
  
  cout << "Enter your name: ";
  string name;
  cin >> name;

  User user(name);

  // main loop

  while (true) {
  }

  return 0;
}
