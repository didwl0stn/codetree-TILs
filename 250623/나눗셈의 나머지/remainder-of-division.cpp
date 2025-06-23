#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a,b;
    int mod[10] = {0,};
    cin >> a >> b;
    while (a!=0) {
        int temp = a%b;
        mod[temp]+=1;
        a = a/b;
    }
    int sum=0;
    for (int i=0; i<10; i++) {
        sum += mod[i]*mod[i];
    }
    cout << sum;
    return 0;
}