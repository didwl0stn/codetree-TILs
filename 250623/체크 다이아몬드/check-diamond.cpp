#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    for (int i=1; i<=n; i++) {
        for (int j=0; j<n-i; j++) {
            cout << " ";
        }
        for (int j=1; j<=2*i-1; j++) {
            if (j%2==1) {
                cout << "*";
            }
            else {
                cout << " ";
            }
        }
        cout << "\n";
    }

    for (int i=0; i<n-1; i++) {
        for (int j=0; j<i; j++) {
            cout << " ";
        }

        for (int j=0; j<2*(n-1) - (2*i-1); j++) {
            if (j%2==1) {
                cout << "*";
            }
            else {
                cout << " ";
            }
        }
        cout << "\n";
    }
    return 0;
}