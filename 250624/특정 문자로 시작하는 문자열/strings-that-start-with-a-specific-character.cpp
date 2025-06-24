#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int cnt=0;
    int sum=0;
    string arr[20];
    char c;
    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }
    cin >> c;
    for (auto i : arr) {
        if (i[0] == c) {
            cnt+=1;
            sum+=i.length();
        }
    }
    cout << fixed;
    cout.precision(2);
    cout << cnt << " " << (double)sum/cnt;
    return 0;
}