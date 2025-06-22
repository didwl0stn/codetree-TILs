#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    double arr[5];
    double sums=0;
    cout << fixed;
    cout.precision(1);
    for (int i=0; i<n; i++) {
        cin >>arr[i];
        sums+=arr[i];
    }
    double res = sums/n;
    cout << res << "\n";
    if (res>=4.0) {
        cout << "Perfect";
    }
    else if (res >=3.0) {
        cout << "Good";
    }
    else {
        cout << "Poor";
    }
    return 0;
}