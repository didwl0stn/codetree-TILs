#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int count = 0;
    for (int i =1; i<=100; i++) {
        count += i;
        if (count>=n) {
            cout << i;
            break;
        }
    }
    return 0;
}