#include <iostream>

using namespace std;

int N;
int nums[1000];
int ans[1001]={0,};
int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }

    // Please write your code here.
    int max = -1;
    int cnt = 0;
    for (int i = 0; i<N; i++) {
        ans[nums[i]]+=1;
        if (ans[nums[i]]==2) {
            ans[nums[i]] = -1000;
        }
    }

    for (int j = 1000; j>=0; j--) {
        if (ans[j]==1) {
            max=j;
            break;
        }
    }
    cout << max;

    return 0;
}
