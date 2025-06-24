#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    string s;
    cin >> s;
    string ans1 = "No";
    string ans2 = "No";
    for (int i=0; i<s.length() - 1; i++) {
        if (s.substr(i,2) == "ee") {
            ans1 = "Yes";
        }
        if (s.substr(i,2) == "ab") {
            ans2 = "Yes";
        }
    }

    cout << ans1 << " " << ans2;
    return 0;
}