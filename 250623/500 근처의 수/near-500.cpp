#include <iostream>
#include <climits>
using namespace std;

int main() {
    // Please write your code here.
    int min = INT_MAX;
    int max=INT_MIN;
    int arr[10];
    for (int i=0; i<10; i++) {
        cin >> arr[i];
        if (arr[i]>max && arr[i]<500) {
            max=arr[i];
        }
        if (arr[i]<min && arr[i]>500) {
            min=arr[i];
        }
    }
    cout << max << " " << min;
    return 0;
}