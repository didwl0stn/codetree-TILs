#include <iostream>
#include <stack>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int arr1[100];
    for (int i=0; i<n; i++) {
        cin >> arr1[i];
    }

    for (int i=n-1; i>=0; i--) {
        if (arr1[i]%2==0) {
            cout << arr1[i] << " ";
        }
    }
    return 0;
}