#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        for (int j=0; j<i; j++) {
            cout << "  ";
        }
        for (int j=0; j<2*n-(i*2+1); j++) {
            cout << "* ";
        }
        cout << "\n";
    }

    for (int i=1; i<n; i++) {
        for (int j=1; j<n-i; j++) {
            cout << "  ";
        }

        for (int j=0; j<2*i+1; j++) {
            cout << "* ";
        }
        cout << "\n";
    }
    return 0;
}