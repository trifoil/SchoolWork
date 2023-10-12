#include <iostream>

using namespace std;

int main()
{
int myVariable = 5;
int *pointer = &myVariable;
cout << "the pointer points towards the address " << pointer << " where is stored the value " << *pointer;

return 0;
}
