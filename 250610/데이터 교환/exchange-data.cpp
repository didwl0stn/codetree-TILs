#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a=5;
    int b=6;
    int c=7;
    int temp = b;
    b=a;
    a=c;
    c=temp;
    cout << a << "\n" << b << "\n" << c;
    return 0;
}