#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    double arr[8];
    double sums = 0;
    for (int i=0; i<8; i++) {
        cin >> arr[i];
        sums += arr[i];
    }
    cout << fixed;
    cout.precision(1);
    cout << (double)sums/8;
    return 0;
}