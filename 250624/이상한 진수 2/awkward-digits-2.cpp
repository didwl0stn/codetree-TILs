#include <iostream>
#include <string>
#include <cmath>
using namespace std;

string a;

int main() {
    cin >> a;

    // Please write your code here.
    for (int i=0; i<a.length(); i++) {
        if (a.length()==1) {
            cout << 0;
            return 0;
        }
        else if (a[i]=='0') {
            a[i]='1';
            break;
        }
        else if (i== a.length()-1) {
            a[i] = '0';
        }
    }

    int temp = a.length();

    int res = 0;
    for (int i =temp-1; i>=0; i--) {
        int val = a[temp-i-1] - '0';
        
        if (val != 0)
            res += pow(val*2,i);
        
     
    }
    cout << res;

    return 0;
}