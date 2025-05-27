#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a,b,c;
    cin >> a >> b >> c;
    if (a > b) {
        if (a < c) {
            cout << a;
        }
    }
    if (a > c) {
        if (a < b) {
            cout << a;
        }
    }
    if (b > a) {
        if (b < c) {
            cout << b;
        }
    }
    if (b > c) {
        if (b < a) {
            cout << b;
        }
    }
    if (c > b) {
        if (c< a) {
            cout << c;
        }
    }
    if (c > a) {
        if (c < b) {
            cout << c;
        }
    }
    return 0;
}