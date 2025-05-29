#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int cnt = 1;
    int arr[4];
    
    for (int i =0; i<n; i++) {
        for (int i=0; i<n; i++) {
        arr[i] = cnt;
        cnt+=1;
        }
        if (i%2==0) {
            for (int j = 0; j<n; j++) {
                cout << arr[j];
            }
        }
        if(i%2!=0) {
            for (int j = n-1; j>=0; j--) {
                cout << arr[j];
            }
        }
        cnt = 1;
        cout << "\n";
    }
    return 0;
}