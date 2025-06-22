#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        int temp;
        cin >> temp;
        if (temp%2==1 && temp%3==0) {
            cout << temp <<"\n";
        }
    }
    return 0;
}