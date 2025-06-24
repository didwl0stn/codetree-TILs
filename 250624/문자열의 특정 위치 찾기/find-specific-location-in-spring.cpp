#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    string s;
    char c;
    cin >> s >> c;
    int idx = -1;
    if (s.find(c) != string::npos) {
        idx = s.find(c);
    }
    if (idx==-1) {
        cout << "No";
    }
    else {
        cout << idx;
    }
    return 0;
}