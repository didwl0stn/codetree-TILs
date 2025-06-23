#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    int cnt = 0;
    int i=1;
    while(cnt !=2) {
        cout << n*i << " ";
        if (n*i %5 ==0) 
            cnt +=1;
        i+=1;
    }
    return 0;
}