#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    string input;
    cout << "Enter a string: ";
    cin >> input;

    int n = input.size();

    string output = "";

    for(int i=n-1; i>=0; i--)
    {
        output += input[i];
    }

    cout << "Reversed String: " << output;
}
