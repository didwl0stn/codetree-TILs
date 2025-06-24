#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <climits>

using namespace std;

int n;
int x[100];
int y[100];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x[i] >> y[i];
    }

    // Please write your code here.
    int minDis = INT_MAX;
    for (int i=1; i<n-1; i++) {
        int temp = 0;
        int ex_x = 0;
        int ex_y=0;
        for (int j=1; j<n; j++) {
            if (j!=i) {
                temp += abs(x[j] - ex_x) + abs(y[j] - ex_y);
                ex_x = x[j];
                ex_y = y[j];
            }
            else {
                
            }
           
        }
        minDis = min(minDis,temp);
    }

    cout << minDis;
    return 0;
}