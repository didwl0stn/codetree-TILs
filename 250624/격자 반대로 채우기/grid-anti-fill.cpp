#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int arr[10][10];
    int cnt = 1;
    for (int i=n-1; i>=0; i--) {
        if ((n-i)%2==1) {
            for (int j=n-1; j>=0; j--) {
            arr[j][i] = cnt;
            cnt +=1;
        }
        }
        else if ((n-i)%2==0) {
            for (int j=0; j<n; j++) {
                arr[j][i] = cnt;
                cnt +=1;
        }
        }
        
    }

    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}