#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int num=1;
    for (int i=1; i<=n; i++) {
        for (int j=0; j<i; j++) {
            cout << num << " ";
            num +=1;
        }
        cout << "\n";
    }
    return 0;
}