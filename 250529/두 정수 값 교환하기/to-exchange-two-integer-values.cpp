#include <iostream>

using namespace std;

int n, m;

void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
    cout << a << " " << b << "\n";
}
int main() {
    cin >> n >> m;
    swap(n,m);
    // Please write your code here.

    return 0;
}