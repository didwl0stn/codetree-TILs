#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a,b;
    cin >> a >>b;
    cout.precision(2);
    cout << fixed;
    cout << double(a+b)/(a-b);
    return 0;
}