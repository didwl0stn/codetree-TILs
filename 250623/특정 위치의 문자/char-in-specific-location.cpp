#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    char arr[6] = {'L','E','B','R','O','S'};
    char c;
    cin >> c;
    int idx = -1;
    for (int i = 0; i<6; i++) {
        if (c==arr[i]) 
            idx=i;
    }
    if (idx==-1) {
        cout << "None";
    }
    else
        cout << idx;
    return 0;
}