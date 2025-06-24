#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    string ans="";
    for (int i =0; i<n; i++) {
        string temp;
        cin >> temp;
        ans+=temp;
    }

    for (int i=0; i<ans.length(); i++) {
        cout << ans[i];
        if (i%5==4) {
            cout << "\n";
        }
    }
    return 0;
}