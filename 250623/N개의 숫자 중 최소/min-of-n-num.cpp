#include <iostream>
#include <climits>
using namespace std;

int N;
int A[100];

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    int min = INT_MAX;
    int cnt = 0;
    // Please write your code here.
    for (int i=0; i<N; i++) {
        if (A[i]==min) {
            cnt+=1;
        }
        else if (A[i]<min) {
            min = A[i];
            cnt = 1;
        }
    }
    cout << min << " " << cnt;
    return 0;
}
