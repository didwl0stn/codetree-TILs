#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int cnt1 = 0;
    int cnt2 = 0;
    for (int i=0; i<10; i++) {
        int temp;
        cin >> temp;
        if (temp%3==0)
            cnt1 +=1;
        if (temp%5==0)
            cnt2+=1;
    }
    cout << cnt1 << " " << cnt2;
    return 0;
}