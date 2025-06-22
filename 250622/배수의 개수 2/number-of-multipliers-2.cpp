#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int cnt =0;
    for (int i=0; i<10; i++) {
        int temp;
        cin >> temp;
        if (temp%2==1) {
            cnt +=1;
        }
    }
    cout << cnt;
    return 0;
}