#include <iostream>
#include <string>
#include <cstdlib>
#include <algorithm>
using namespace std;

int N;
int A[100];

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    // Please write your code here.
    int cnt = 0;
    for (int i=0; i<N; i++) {
        for (int j=i+1; j<N; j++) {
            for (int k=j+1; k<N; k++) {
                if (A[i]<=A[j] && A[j]<=A[k]) {
                    cnt +=1;
                }
            }
        }
    }
    cout << cnt;
    return 0;
}