#include <iostream>
#include <string>

using namespace std;

string A;

int main() {
    cin >> A;

    // Please write your code here.
    int cnt = 0;
    for (int i =0; i<A.length(); i++) {
        if (A[i] == '(') {
            for (int j = i+1; j<A.length(); j++) {
                if (A[j]==')') {
                    cnt+=1;
                }
            }
        }
    }
    cout << cnt;
    return 0;
}