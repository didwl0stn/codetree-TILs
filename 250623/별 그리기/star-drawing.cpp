#include <iostream>

using namespace std;

int n;

int main() {
    cin >> n;

    // Please write your code here.
    for (int i=1; i<=n; i++) {
        for (int j=0; j< n-i; j++) {
            cout << " ";
        }

        for (int j=0; j<2*(i-1) +1; j++) {
            cout << "*";
        }
        cout << "\n";
    }

    for (int i=1; i<=n-1; i++) {
        for (int j=0; j<i; j++) {
            cout << " ";
        }
        for (int j=0; j<2*(n-1)-(2*i-1); j++) {
            cout << "*";
        }
        cout << "\n";
    }

    return 0;
}
