#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int aa,ab,ba,bb;
    cin >> aa >> ab;
    cin >> ba >> bb;
    if (aa > ba && ab > bb) {
        cout << 1;
    }
    else {
        cout << 0;
    }
    return 0;
}