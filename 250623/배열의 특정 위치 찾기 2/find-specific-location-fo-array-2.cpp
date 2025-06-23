#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int evenSum=0;
    int oddSum=0;
    int arr[10];
    for (int i=0; i<10; i++) {
        cin >> arr[i];
        if (i%2==0) {
            oddSum+=arr[i];
        }
        else {
            evenSum+=arr[i];
        }
    }
    cout << (oddSum>evenSum ? oddSum - evenSum : evenSum - oddSum);

    return 0;
}