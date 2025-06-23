#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[100];
    int n,q;
    cin >> n >> q;
    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }
    for (int i=0; i<q; i++) {
        int a;
        cin >> a;

        if (a==1) {
            int b;
            cin >> b;
            cout << arr[b-1] << "\n";
        }
        else if (a==2) {
            int b;
            cin >>b;
            int idx = 0;
            for (int j=0; j<n; j++) {
                if (arr[j]==b) {
                    idx=j+1;
                    break;
                }
            }
            cout << idx << "\n";
        }
        else if (a==3) {
            int b,c;
            cin >> b>>c;
            for (int i=b-1; i<c; i++) {
                cout << arr[i] << " ";
            }
            cout << "\n";
        }
    }
    return 0;
}