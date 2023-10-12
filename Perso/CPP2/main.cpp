#include <iostream>
#include <fstream>
#include <vector>
#include <string>

class User {
public:
    std::string name;
    int number;
    std::string characters;

    User() : name(""), number(0), characters("") {}

    void input() {
        std::cout << "Enter your name: ";
        std::cin >> name;
        std::cout << "Enter a number: ";
        std::cin >> number;
        std::cout << "Enter a string of characters: ";
        std::cin >> characters;
    }

    void display() {
        std::cout << "Name: " << name << std::endl;
        std::cout << "Number: " << number << std::endl;
        std::cout << "Characters: " << characters << std::endl;
    }
};

int main() {
    std::vector<User> users;

    // Input data for two users
    for (int i = 0; i < 2; i++) {
        User user;
        user.input();
        users.push_back(user);
    }

    // Write data to a text file
    std::ofstream file("users.txt");
    if (file.is_open()) {
        for (const User& user : users) {
            file << user.name << " " << user.number << " " << user.characters << std::endl;
        }
        file.close();
    } else {
        std::cerr << "Unable to open the file for writing." << std::endl;
        return 1;
    }

    // Read data from the text file and display a user
    std::ifstream readFile("users.txt");
    if (readFile.is_open()) {
        std::string nameToFind;
        std::cout << "Enter a name to display: ";
        std::cin >> nameToFind;

        bool userFound = false;
        User userToDisplay;

        std::string name, characters;
        int number;
        while (readFile >> name >> number >> characters) {
            if (name == nameToFind) {
                userToDisplay.name = name;
                userToDisplay.number = number;
                userToDisplay.characters = characters;
                userFound = true;
                break;
            }
        }
        readFile.close();

        if (userFound) {
            userToDisplay.display();
        } else {
            std::cout << "User not found in the file." << std::endl;
        }
    } else {
        std::cerr << "Unable to open the file for reading." << std::endl;
        return 1;
    }

    return 0;
}
