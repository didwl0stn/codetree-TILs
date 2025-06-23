#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int ans[10] = {0,};
    int arr[100];
    for (int i=0; i<100; i++) {
        cin >> arr[i];
        if (arr[i]==0) 
            break;
        ans[arr[i]/10] +=1;
    }
    for (int i=1; i<10; i++) {
        cout << i << " - " << ans[i] << "\n";
    }
    return 0;
}