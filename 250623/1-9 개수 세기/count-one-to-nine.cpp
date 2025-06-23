#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int arr[10] = {0,};
    for (int i=0; i<n; i++) {
        int a;
        cin >> a;
        arr[a]+=1;
    }
    for (int i=1; i<10; i++) {
        cout << arr[i] << "\n";
    }
    return 0;
}