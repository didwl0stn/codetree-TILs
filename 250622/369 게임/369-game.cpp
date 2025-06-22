#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    for (int i=1; i<=n; i++) {
        if (i%3==0) {
            cout << "0 ";
        }
        else {
            int a = i/10;
            int b = i%10;
            if ((a==3||a==6||a==9) || (b==3||b==6||b==9)) {
                cout << "0 ";
            }
            else {
                cout << i << " ";
            }
        }
    }
    return 0;
}