#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int cnt =1 ;
    int n,m;
    cin >> n >> m;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cout << cnt << " ";
            cnt +=1;
        }
        cout << "\n";
    }
    return 0;
}