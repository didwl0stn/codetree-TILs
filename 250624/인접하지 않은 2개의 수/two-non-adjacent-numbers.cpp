#include <bits/stdc++.h>

using namespace std;

int n;
int numbers[100];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
    }

    // Please write your code here.
    int maxVal = INT_MIN;
    for (int i=0; i<n-2; i++) {
        
        for (int j=i+2; j<n; j++) {
            maxVal = max(maxVal, numbers[i] + numbers[j]);
        }
    }
    cout << maxVal;
    return 0;
}