#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >>n;
    for (int i=0; i<n; i++) {
        for (int j=0; j<=i; j++) {
            cout << "* ";
        }
        cout << "\n";
    }

    for (int i=1;i<n;i++) {
        for (int j=0; j<n-i; j++) {
            cout << "* ";
        }
        cout << "\n";
    }
    return 0;
}