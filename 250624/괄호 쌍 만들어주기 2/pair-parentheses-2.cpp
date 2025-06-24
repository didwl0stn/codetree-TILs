#include <iostream>
#include <string>
#include <climits>
#include <cstdlib>
#include <cmath>
#include <vector>
using namespace std;

int main() {
    // Please write your code here.
    string s;
    cin >> s;
    int cnt = 0;
    for (int i=0; i<s.length()-2; i++) {
        if (s.substr(i,2)=="((") {
            for (int j = i+2; j < s.length(); j++) {
                if (s.substr(j,2) == "))") {
                    cnt +=1;
                }
            }
        }
    }
    cout << cnt;
    return 0;
}