#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int ans[7] = {0,};
    int arr[10];
    for (int i=0; i<10; i++) {
        cin >> arr[i];
        ans[arr[i]] += 1;
    }
    for (int i=1; i<=6; i++) {
        cout << i << " - " << ans[i] << "\n";
    }
    return 0;
}