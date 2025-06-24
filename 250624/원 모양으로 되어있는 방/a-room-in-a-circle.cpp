#include <iostream>
#include <climits>
#include <cstdlib>
#include <algorithm>

using namespace std;

int n;
int a[1003];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // Please write your code here.
    int ans = INT_MAX;
    for (int i =0; i<n; i++) {
        int temp = 0;
        for (int j=0; j<n; j++) {
            if (i<j) {
                temp += a[j] * (j-i);
            }
            else if (i>j) {
                temp += a[j] * (n-(i-j));
            }
            
        }
        ans = min(ans,temp);
    }
    cout << ans;

    return 0;
}