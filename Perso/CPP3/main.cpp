#include <iostream>
#include <string>

using namespace std;

class User {
public:
  void writeHello() {
    cout << "Hello world";
  }

  void setUserName(string name){
    userName = name;
  }

  string returnUserName(){
    
    return userName;
  }

private:
  string userName;
};
int main() {

  User userOne ;
  userOne.setUserName("augi");
  cout << userOne.returnUserName() << endl;

  return 0;
}
