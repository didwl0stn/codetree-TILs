#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int sums=0;
    for (int i=n; i<=100; i++) {
        sums += i;
    }
    cout << sums;
    return 0;
}