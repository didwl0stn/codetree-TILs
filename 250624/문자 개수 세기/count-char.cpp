#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    string str;
    getline(cin,str);
    char c;
    cin >> c;
    int cnt = 0;
    for (int i=0; i<str.length(); i++) {
        if (str[i]==c) {
            cnt +=1;
        }
    }
    cout<<cnt;
    return 0;
}