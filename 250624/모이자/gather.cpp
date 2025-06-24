#include <iostream>
#include <climits>
#include <cstdlib>
using namespace std;

int n;
int A[100];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    // Please write your code here.
    int mins = INT_MAX;
    for (int i = 0; i<n; i++) {
        int temp=0;
        for (int j=0; j<n; j++) {
            temp += A[j] * abs(i-j);
        }
        mins = min(mins,temp);
    }
    cout << mins;

    return 0;
}