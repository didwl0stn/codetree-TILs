#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a,b;
    cin >>a>>b;
    int sums=0;
    for (int i=a; i<=b; i++) {
        sums+=i;
    }
    cout << sums;
    return 0;
}