#include <iostream>
#include <climits>
using namespace std;


int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int arr[10];
    int min =INT_MAX;
    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }

    for (int i=0; i<n-1; i++) {
        if (arr[i+1]-arr[i] < min) {
            min=arr[i+1]-arr[i];
        }
    }
    cout << min;
    return 0;
}