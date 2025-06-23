#include <iostream>
#include <climits>
using namespace std;

int main() {
    // Please write your code here.

    int min = INT_MAX;
    int max = INT_MIN;

    while(true) {
        int temp;
        cin >> temp;

        if (temp==999 || temp==-999) {
            break;
        }
        if (min>temp) {
            min = temp;
        }
        if (max<temp) {
            max = temp;
        }
    }

    cout << max << " " << min;
    return 0;
}