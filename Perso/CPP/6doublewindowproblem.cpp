#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>
#include <iostream>
#include <string>

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
      SDL_CreateWindow("Tonk | Main", SDL_WINDOWPOS_CENTERED,
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

  // Button rectangle and state
  SDL_Rect buttonRect = {250, 300, 200, 50};
  bool buttonClicked = false;

  SDL_RenderClear(renderer);
  SDL_RenderCopy(renderer, textTexture, NULL, NULL);

  // Render the button
  SDL_SetRenderDrawColor(renderer, 0, 0, 255, 255);
  SDL_RenderFillRect(renderer, &buttonRect);

  SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
  SDL_RenderDrawRect(renderer, &buttonRect);

  TTF_Font *buttonFont = TTF_OpenFont("Nerd.ttf", 24);
  if (!buttonFont) {
    cerr << "Font loading failed: " << TTF_GetError() << endl;
    SDL_DestroyTexture(textTexture);
    SDL_FreeSurface(textSurface);
    TTF_CloseFont(font);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    TTF_Quit();
    SDL_Quit();
    return 1;
  }

  SDL_Surface *buttonTextSurface =
      TTF_RenderText_Solid(buttonFont, "Open Second Window", {255, 255, 255});
  if (!buttonTextSurface) {
    cerr << "Text rendering failed: " << TTF_GetError() << endl;
    SDL_DestroyTexture(textTexture);
    SDL_FreeSurface(textSurface);
    TTF_CloseFont(font);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    TTF_Quit();
    SDL_Quit();
    return 1;
  }

  SDL_Texture *buttonTextTexture =
      SDL_CreateTextureFromSurface(renderer, buttonTextSurface);
  if (!buttonTextTexture) {
    cerr << "Texture creation failed: " << SDL_GetError() << endl;
    SDL_DestroyTexture(textTexture);
    SDL_FreeSurface(textSurface);
    TTF_CloseFont(font);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    TTF_Quit();
    SDL_Quit();
    return 1;
  }

  SDL_RenderCopy(renderer, buttonTextTexture, NULL, &buttonRect);
  SDL_RenderPresent(renderer);

  SDL_FreeSurface(buttonTextSurface);

  // Event loop
  bool quit = false;
  SDL_Window *secondWindow = nullptr;
  SDL_Renderer *secondRenderer = nullptr;

  SDL_Event e;
  while (!quit) {
    while (SDL_PollEvent(&e)) {
      if (e.type == SDL_QUIT) {
        quit = true;
      } else if (e.type == SDL_MOUSEBUTTONDOWN) {
        int mouseX, mouseY;
        SDL_GetMouseState(&mouseX, &mouseY);
        if (mouseX >= buttonRect.x && mouseX <= buttonRect.x + buttonRect.w &&
            mouseY >= buttonRect.y && mouseY <= buttonRect.y + buttonRect.h) {
          // The button was clicked
          if (secondWindow == nullptr) {
            // Create and show the second window
            secondWindow =
                SDL_CreateWindow("Second Window", SDL_WINDOWPOS_CENTERED,
                                 SDL_WINDOWPOS_CENTERED, 800, 600, SDL_WINDOW_SHOWN);
            if (secondWindow) {
              secondRenderer = SDL_CreateRenderer(
                  secondWindow, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
            }
          }
        }
      }

      if (secondWindow != nullptr) {
        // Handle events for the second window
        while (SDL_PollEvent(&e)) {
          if (e.type == SDL_QUIT) {
            SDL_DestroyRenderer(secondRenderer);
            SDL_DestroyWindow(secondWindow);
            secondRenderer = nullptr;
            secondWindow = nullptr;
          }
        }
      }
    }

    // Introduce a small delay for both the main window and the second window
    SDL_Delay(10);
  }

  // Cleanup and quit
  if (secondRenderer != nullptr) {
    SDL_DestroyRenderer(secondRenderer);
  }
  if (secondWindow != nullptr) {
    SDL_DestroyWindow(secondWindow);
  }

  SDL_DestroyTexture(textTexture);
  SDL_DestroyTexture(buttonTextTexture);
  TTF_CloseFont(font);
  TTF_CloseFont(buttonFont);
  SDL_DestroyRenderer(renderer);
  SDL_DestroyWindow(window);
  TTF_Quit();
  SDL_Quit();

  return 0;
}