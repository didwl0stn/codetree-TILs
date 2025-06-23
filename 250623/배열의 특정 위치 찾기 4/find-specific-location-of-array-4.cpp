#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[10];
    int sums=0;
    int cnt=0;
    for (int i=0; i<10; i++) {
        cin >> arr[i];
        if (arr[i]==0) {
            cout << cnt << " " << sums;
            break;
        }
        else if (arr[i]%2==0) {
            cnt +=1;
            sums+=arr[i];
        }

        if (i==9) {
            cout << cnt << " " << sums;
        }
    }
    return 0;
}