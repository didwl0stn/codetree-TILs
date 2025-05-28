#include <iostream>

using namespace std;

int st, ed;

int main() {
    cin >> st >> ed;

    // Please write your code here.
    int cnt = 0;
    for (int i = st; i<=ed; i++) {
        int div_cnt=0;
        for (int j=1; j<=i; j++) {
            if (i%j==0)
                div_cnt+=1;
        }
        if (div_cnt==3) {
            cnt +=1;
        }
    }
    cout << cnt;

    return 0;
}
