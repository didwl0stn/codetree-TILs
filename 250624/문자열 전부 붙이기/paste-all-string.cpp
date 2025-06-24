#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    string temp = "";
    for (int i=0; i<n; i++) {
        string a;
        cin >> a;
        temp.append(a);
    }
    cout << temp;
    return 0;
}