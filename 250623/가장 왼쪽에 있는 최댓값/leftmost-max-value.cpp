#include <iostream>
#include <climits>
using namespace std;

int N;
int a[1000];

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> a[i];
    }

    // Please write your code here.
    
    
    while(true) {
        int max = INT_MIN;
        int idx = -1;
        for (int i=0; i<N; i++) {
            if (max<a[i]) {
                max = a[i];
                idx = i;
            }
        }
        cout << idx + 1 << " ";
        N=idx;
        if (idx==0) {
            break;
        }
 
 }    

    return 0;
}
