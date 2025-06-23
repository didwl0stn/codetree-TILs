#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int answer[11] = {0,};
    int arr[100];
    for (int i = 0; i<100; i++) {
        cin >> arr[i];
        if (arr[i]==0) 
            break;
        answer[arr[i]/10]+=1;
    }
    for (int i=10; i>=1; i--) {
        cout << i*10 << " - " << answer[i] << "\n";
    }
    return 0;
}