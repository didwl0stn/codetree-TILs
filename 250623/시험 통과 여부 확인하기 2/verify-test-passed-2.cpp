#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int cnt = 0;
    int n; 
    cin >> n;
    for (int i=0; i<n; i++) {
        int arr[4];
        int sum = 0;
        for (int j=0;j<4;j++) {
            cin >> arr[j];
            sum += arr[j];
        }
        if (sum/4 >= 60) {
            cout << "pass\n";
            cnt+=1;
        }
        else {
            cout << "fail\n";
        }
    }
    cout << cnt;
    return 0;
}