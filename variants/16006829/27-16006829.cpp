//  
// 01.06.2024

#include <iostream>

using namespace std;

#define int long long

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("/mnt/d/Users/Matvei/Developer/Projects/InfEge/variants/16006829/inputs/27_B.txt", "r", stdin);

    constexpr int m = 80;
    constexpr int b = 50;

    int n;
    cin >> n;

    int arr[n];
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if ((arr[i] > b || arr[j] > b) and (arr[i] + arr[j]) % m == 0) {
                ++cnt;
            }
        }
    }

    cout << cnt << '\n';

    return 0;
}
