#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    for (int i = 0; i<n; i++) {
        for (int j = 0; j<n-i; j ++) {
            for (int k = 0; k<n-i; k++) {
                cout <<"*";
            }
            cout << " ";
        }
        cout << "\n";
    }
    return 0;
}