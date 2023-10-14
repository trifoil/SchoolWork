#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>
#include <iostream>
using namespace std;

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
    cerr << "SDL initialization failed: " << SDL_GetError() << endl;
    return 1;
  }

// SDL2 ttf init

  if (TTF_Init() < 0) {
    cerr << "SDL_ttf initialization failed: " << TTF_GetError() << endl;
    SDL_Quit();
    return 1;
  }

// Main window creation

  SDL_Window *window =
      SDL_CreateWindow("Tonk | Main ", SDL_WINDOWPOS_CENTERED,
                       SDL_WINDOWPOS_CENTERED, 700, 400, SDL_WINDOW_SHOWN);
  if (!window) {
    cerr << "Window creation failed: " << SDL_GetError() << endl;
    TTF_Quit();
    SDL_Quit();
    return 1;
  }



  SDL_Renderer *renderer = SDL_CreateRenderer(
      window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
  if (!renderer) {
    cerr << "Renderer creation failed: " << SDL_GetError() << endl;
    SDL_DestroyWindow(window);
    TTF_Quit();
    SDL_Quit();
    return 1;
  }

  TTF_Font *font = TTF_OpenFont("Nerd.ttf", 48);
  if (!font) {
    cerr << "Font loading failed: " << TTF_GetError() << endl;
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    TTF_Quit();
    SDL_Quit();
    return 1;
  }

  SDL_Surface *textSurface =
      TTF_RenderText_Solid(font, "Hello, World!", {255, 255, 255});
  if (!textSurface) {
    cerr << "Text rendering failed: " << TTF_GetError() << endl;
    TTF_CloseFont(font);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    TTF_Quit();
    SDL_Quit();
    return 1;
  }

  SDL_Texture *textTexture =
      SDL_CreateTextureFromSurface(renderer, textSurface);
  if (!textTexture) {
    cerr << "Texture creation failed: " << SDL_GetError() << endl;
    SDL_FreeSurface(textSurface);
    TTF_CloseFont(font);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    TTF_Quit();
    SDL_Quit();
    return 1;
  }

  SDL_RenderClear(renderer);
  SDL_RenderCopy(renderer, textTexture, NULL, NULL);
  SDL_RenderPresent(renderer);

  SDL_FreeSurface(textSurface);

  // Event loop

  bool quit = false;
  SDL_Event e;
  while (!quit) {
    while (SDL_PollEvent(&e)) {
      if (e.type == SDL_QUIT) {
        quit = true;
      }
    }

    // Introduce a small delay to reduce CPU usage
    SDL_Delay(10);
  }

  // Cleanup and quit
  SDL_DestroyTexture(textTexture);
  TTF_CloseFont(font);
  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(window);
  TTF_Quit();
  SDL_Quit();

  return 0;
}
