#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int arr[100];
    for (int i=0; i<n; i++) {
        cin >> arr[i];
        arr[i] *=arr[i];
    }
    for (int i=0; i<n; i++) {
        cout << arr[i] << " ";
    }
    return 0; }