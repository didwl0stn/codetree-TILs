// // #include <iostream>
// // #include <string>
// // #include <cmath>
// // using namespace std;

// // string a;

// // int main() {
// //     cin >> a;

// //     // Please write your code here.
// //     for (int i=0; i<a.length(); i++) {
// //         if (a[i]=='0') {
// //             a[i]='1';
// //             break;
// //         }
// //     }

// //     int temp = a.length();

// //     int res = 0;
// //     for (int i =temp-1; i>=0; i--) {
// //         int val = a[temp-i-1] - '0';
        
// //         if (val != 0)
// //             res += pow(val*2,i);
        
     
// //     }
// //     cout << res;

// //     return 0;
// // }
// #include <iostream>
// #include <string>
// #include <cmath>
// using namespace std;

// string a;

// int main() {
//     cin >> a;

//     // 첫 번째 0을 1로 바꿈
//     for (int i = 0; i < a.length(); i++) {
//         if (a[i] == '0') {
//             a[i] = '1';
//             break;
//         }
//     }

//     int res = 0;
//     int len = a.length();
//     for (int i = 0; i < len; i++) {
//         int val = a[i] - '0';
//         res += val * pow(2, len - 1 - i);  // 2진수 계산
//     }

//     cout << res;
//     return 0;
// }

#include <iostream>
#include <string>
using namespace std;

int main() {
    string a;
    cin >> a;

    // 왼쪽부터 처음 만나는 '0'을 '1'로 바꾸기
    for (int i = 0; i < a.length(); i++) {
        if (a[i] == '0') {
            a[i] = '1';
            break;
        }
    }

    // 이진수를 10진수로 변환
    int res = 0;
    for (int i = 0; i < a.length(); i++) {
        res = res * 2 + (a[i] - '0');
    }

    cout << res;
    return 0;
}
