#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[10];
    int sums=0;
    for (int i=0; i<10; i++) {
        cin >> arr[i];
        sums+=arr[i];
    }
    cout << sums;
    return 0;
}