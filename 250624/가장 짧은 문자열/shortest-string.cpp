#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    string s1,s2,s3;
    cin >> s1 >> s2 >> s3;
    int l1 = s1.length();
    int l2 = s2.length();
    int l3 = s3.length();
    int max = 0;
    int min = 0;

    if (l1 > l2 && l1 > l3) 
        max = l1;
   if (l1 < l2 && l1 < l3) 
        min = l1;
    
    if (l2 > l1 && l2 > l3) 
        max = l2;
    
    if (l2 < l1 && l2 < l3) 
        min= l2;
    
    if (l3> l2 && l3 > l1) 
        max = l3;
    
    if (l3 < l2 && l3 < l1) 
        min = l3;
    
    cout << max - min;
    return 0;
}