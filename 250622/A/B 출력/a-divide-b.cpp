#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    int a,b;
    cin >> a >> b;
    cout << a/b << ".";
    a = (a%b) * 10;
    for (int i=1; i<21; i++) {
        int m = a/b;
        cout << m;
        a = (a%b)*10;
    }
    

    return 0;
}