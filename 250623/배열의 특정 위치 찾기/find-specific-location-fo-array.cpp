#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[10];
    int a_sum = 0;
    int b_sum =0;
    int b_cnt=0;
    for (int i=0; i<10; i++) {
        cin >> arr[i];
        if (i%2==1) {
            a_sum+=arr[i];
        }
        if (i%3==2) {
            b_sum+=arr[i];
            b_cnt+=1;
        }
    }
    cout.precision(1);
    cout << fixed;

    cout << a_sum << " " << (double)b_sum/b_cnt;
    return 0;
}