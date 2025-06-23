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

    // Please write your code here.
    int max=INT_MIN;
    int second=INT_MIN;

    for (int i=0; i<N; i++) {
        if (max<=A[i]) {
            second = max;
            max = A[i];
        }
        else if (second<=A[i]) {
            second = A[i];
        }
    }
    cout << max << " " << second;
    return 0;
}
