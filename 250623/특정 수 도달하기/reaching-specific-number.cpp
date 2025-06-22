#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[10];
    int sums=0;
    cout << fixed;
    cout.precision(1);
    for (int i=0; i<10; i++) {
        cin >> arr[i];
        if (arr[i]>=250) {
            cout << sums << " " << (double)sums/i;
            break;
        }
        sums+=arr[i];
    }
    return 0;
}