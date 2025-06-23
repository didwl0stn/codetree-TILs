#include <iostream>
#include <climits>
using namespace std;

int main() {
    // Please write your code here.
    int arr[10];
    for (int i=0; i<10; i++) {
        cin >> arr[i];
    }
    int max=INT_MIN;
    for (int i=0; i<10; i++) {
        if (max<arr[i]) {
            max=arr[i];
        }
    }

    cout << max;
    return 0;
}