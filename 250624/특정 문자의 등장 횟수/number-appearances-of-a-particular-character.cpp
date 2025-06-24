#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    int cnt1 = 0;
    int cnt2 = 0;
    string s;
    cin >> s;
    for (int i=0; i<s.length()-1; i++) {
        if (s.substr(i,2)=="ee") {
            cnt1 +=1;
        }
        if (s.substr(i,2)=="eb") {
            cnt2 +=1;
        }
    }
    cout << cnt1 << " " << cnt2;
    return 0;
}