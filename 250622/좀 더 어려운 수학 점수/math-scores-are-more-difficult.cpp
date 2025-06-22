#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int aa,ab,ba,bb;
    cin >> aa>>ab>>ba>>bb;
    if (aa>ba) {
        cout << 'A';
    }
    else if (aa<ba) {
        cout << 'B';
    }
    else {
        if (ab>bb) {
            cout << 'A';
        }
        else {
            cout << 'B';
        }
    }
    return 0;
}