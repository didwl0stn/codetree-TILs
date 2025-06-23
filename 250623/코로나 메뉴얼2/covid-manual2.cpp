#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int cnt=0;
    int arr[4] = {0,};
    for (int i=0; i<3; i++) {
        char c;
        int t;
        cin >> c >> t;

        if (c=='Y' && t>=37) {
            cnt+=1;
            arr[0]+=1;
        }
        else if (c=='N' && t>=37) {
            arr[1]+=1;
        }
        else if (c=='Y' && t<37) {
            arr[2]+=1;
        }
        else {
            arr[3]+=1;
        }
    }
    for (int i=0; i<4; i++) {
        cout << arr[i] << " ";
    }
    if (cnt>=2) {
        cout << 'E';
    }
    return 0;
}