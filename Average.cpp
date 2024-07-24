//Week-1-Q1
#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Enter the size of Array: ";
    cin >> n;

    int arr[n];
    for(int i=0; i<n; i++)
    {
        cout << "Enter " << i << " element: ";
        cin >> arr[i];
    }

    cout << "Arr = {";
    for(int i=0; i<n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << "}";

    return 0;
}
