#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int arr[10][10] = {0,};
    int m;
    cin >> m;
    for (int i=0; i<m; i++) {
        int r,c;
        cin >> r >> c;
        arr[r][c] = 1;
    }

    for (int i=1; i<=n; i++) {
        for (int j=1; j<=n; j++) {
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}