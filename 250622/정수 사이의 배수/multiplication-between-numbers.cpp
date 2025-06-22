#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a,b;
    cin >> a>>b;
    int sums=0;
    int cnt = 0;
    for (int i=a; i<=b; i++) {
        if (i%5==0 || i%7==0) {
            sums+=i;
            cnt +=1;
        }
    }
    cout.precision(1);
    cout << fixed;

    cout << sums << " " << (double)sums/cnt;
    return 0;
}