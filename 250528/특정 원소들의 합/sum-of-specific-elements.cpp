#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int mat[4][4];
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            cin >> mat[i][j];
        }
    }
    int total =0;
    for (int i=0; i<4; i++) {
        for (int j=0; j<=i; j++) {
            total += mat[i][j];
        }
    }

    cout << total;
    return 0;
}