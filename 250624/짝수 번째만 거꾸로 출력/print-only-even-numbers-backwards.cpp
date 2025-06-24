#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    string s;
    cin >> s;
    int len = s.length();
    if (len%2==0) {
        for (int i=len-1; i>=0; i-=2) {
            cout << s[i];
        }
    }
    else {
        for (int i=len-2; i>=0; i-=2) {
            cout << s[i];
        }
    }
    
    return 0;
}