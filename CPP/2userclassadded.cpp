#include <SDL2/SDL.h>
#include <iostream>
#include <string>

class User {
public:
    std::string username;
    std::string userId;
    int configLayout;
    int cameraView;

    User(const std::string& name) : username(name), configLayout(0), cameraView(0) {
        // Generate a random 4-digit user ID starting with '#'
        userId = "#" + std::to_string(rand() % 9000 + 1000);
    }
};

int main(int argc, char* argv[]) {
    // Initialize SDL
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        SDL_Log("SDL could not initialize: %s", SDL_GetError());
        return 1;
    }

    // Prompt the user for their name
    std::cout << "Enter your name: ";
    std::string name;
    std::cin >> name;

    // Create a User object
    User user(name);

    // Display user information
    std::cout << "User Information:\n";
    std::cout << "Name: " << user.username << std::endl;
    std::cout << "User ID: " << user.userId << std::endl;
    std::cout << "Config Layout: " << user.configLayout << std::endl;
    std::cout << "Camera View: " << user.cameraView << std::endl;

    // Create a window
    SDL_Window* window = SDL_CreateWindow(
        "SDL2 Window",
        SDL_WINDOWPOS_UNDEFINED,
        SDL_WINDOWPOS_UNDEFINED,
        640, 480,  // Window size (width x height)
        SDL_WINDOW_SHOWN
    );

    if (!window) {
        SDL_Log("Window creation failed: %s", SDL_GetError());
        return 1;
    }

    // Create a renderer with a black background
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255); // Set background color to black
    SDL_RenderClear(renderer); // Clear the screen with the background color
    SDL_RenderPresent(renderer); // Present the renderer

    // Event loop
    bool quit = false;
    SDL_Event event;
    while (!quit) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                quit = true;
            }
        }

        // Your game logic goes here

        // Rendering can go here (if needed)
    }

    // Cleanup and quit
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
