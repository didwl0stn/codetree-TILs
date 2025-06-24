#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <climits>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int arr[20][20];
    int maxs = INT_MIN;
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> arr[i][j];
        }
    }
    for (int i=0; i<n; i++) {
        for (int j=0; j<n-2; j++) {
            int temp = arr[i][j] + arr[i][j+1] + arr[i][j+2];
            maxs = max(maxs,temp);
        }
    }
    cout << maxs;

    return 0;
}