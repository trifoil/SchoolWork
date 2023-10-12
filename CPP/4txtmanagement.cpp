#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class User {
public:
    string name;
    int number;
    string characters;

    void inputUserDetails() {
        cout << "Enter your name: ";
        cin.ignore();
        getline(cin, name);
        cout << "Enter a number: ";
        cin >> number;
        cout << "Enter a string of characters: ";
        cin.ignore();
        getline(cin, characters);
    }
};

int main() {
    User user1, user2;

    // Input for the first user
    cout << "User 1 Details:\n";
    user1.inputUserDetails();

    // Input for the second user
    cout << "\nUser 2 Details:\n";
    user2.inputUserDetails();

    // Store data in a text file
    ofstream outfile("user_data.txt");
    if (outfile.is_open()) {
        outfile << "User 1 Details:\n";
        outfile << "Name: " << user1.name << "\n";
        outfile << "Number: " << user1.number << "\n";
        outfile << "Characters: " << user1.characters << "\n";
        outfile << "User 2 Details:\n";
        outfile << "Name: " << user2.name << "\n";
        outfile << "Number: " << user2.number << "\n";
        outfile << "Characters: " << user2.characters << "\n";
        outfile.close();
        cout << "User data has been saved to 'user_data.txt'.\n";
    } else {
        cerr << "Unable to open the file for writing.\n";
    }

    // Display data from the text file
    ifstream infile("user_data.txt");
    if (infile.is_open()) {
        string line;
        cout << "\nUser data from the file:\n";
        while (getline(infile, line)) {
            cout << line << endl;
            if (line.empty())
                cout << "........\n";
        }
        infile.close();
    } else {
        cerr << "Unable to open the file for reading.\n";
    }

    return 0;
}
