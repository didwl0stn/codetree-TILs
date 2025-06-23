#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr1[100];
    int arr2[100];
    for (int i=0; i<100; i++) {
        cin >> arr1[i];
        if (arr1[i] == 0) {
            for (int j=0; j<i; j++) {
                cout << arr2[j] << " ";
            }
            break;
        }

        if (arr1[i] %2==0) {
            arr2[i] = arr1[i]/2;
        }
        else {
            arr2[i] = arr1[i]+3;
        }
    }
    return 0;
}
