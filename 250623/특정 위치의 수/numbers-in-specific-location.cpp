#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[10];
    int sum = 0;
    for (int i=0; i<10; i++) {
        cin >> arr[i];
    }
    sum = sum + arr[2] + arr[4] + arr[9];
    cout << sum;
    return 0;
}