#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int cnt = 1;
    int arr[9][9];

    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            if (i%2==0) {
            arr[j][i] = cnt;
            cnt +=1;
            }

            if (i%2!=0) {
                arr[j][i] = n-cnt+1;
                cnt +=1;
            }
        }
        cnt = 1;
    }

    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cout << arr[i][j];
        }
        cout << "\n";
    }
    return 0;
}