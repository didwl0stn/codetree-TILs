#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr1[100];
    int arr2[100];
    int n;
    cin >> n;
    int cnt = 0;
    for (int i=0; i<n; i++) {
        cin >> arr1[i];
        if (arr1[i]%2==0) {
            arr2[cnt] = arr1[i];
            cnt +=1;
        }
    }
    for (int i=0; i<cnt; i++) {
        cout << arr2[i] << " ";
    }
    return 0;
}