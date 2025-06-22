#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a,b;
    cin >> a >> b;
    if (a>0) {
        while(b--) {
            cout << a;
        }
    }
    else {
        cout << 0;
    }
    return 0;
}