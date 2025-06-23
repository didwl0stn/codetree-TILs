#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n1,n2;
    cin >> n1>>n2;
    int arr1[100];
    int arr2[100];
    int answer = 0;

    for (int i=0; i<n1; i++) {
        cin >> arr1[i];
    }

    for (int i=0; i<n2; i++) {
        cin >> arr2[i];
    }

    for (int i=0; i<n1-n2+1; i++) {
        if (arr1[i] == arr2[0]) {
            for (int j=1; j<n2; j++) {
                if (arr1[i+j]==arr2[j]) {
                    if (j==n2-1) {
                        answer = 1;
                    }
                }
                else {
                    break;
                }
            }
        }
    }

    if (answer==1) {
        cout << "Yes";
    }
    else {
        cout << "No";
    }
    return 0;
}