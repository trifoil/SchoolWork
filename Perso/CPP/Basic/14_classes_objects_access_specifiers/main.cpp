#include <codecvt>
#include <iostream>
#include <string>
#include <type_traits>

using namespace std;

class User {
public:
  void outputHelloworld() { cout << "hello world\n"; }

  void setUserName(string name) { userName = name; }
  string getUserName() { return userName; }

private:
  string userName;
};

int main() {

  User userExample;
  userExample.setUserName("gugu");
  cout << userExample.getUserName();
  // userExample.outputHelloworld();
  return 0;
}