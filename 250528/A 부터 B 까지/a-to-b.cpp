#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a,b;
    cin >> a >> b;
    while (a<=b) {
        cout << a << " ";
        if (a%2==0) {
            a+=3;
        }
        else
            a *=2;
    }
    return 0;
}