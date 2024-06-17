//  
// 01.06.2024

#include <iostream>

using namespace std;

#define int long long

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("/mnt/d/Users/Matvei/Developer/Projects/InfEge/variants/16006829/inputs/26.txt", "r", stdin);

    int s, n;
    cin >> s >> n;

    int arr[n];
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    sort(arr, arr + n);

    int cnt = 0;
    int sm = 0;
    int last_idx = -1e9;
    for (int i = 0; i < n; ++i) {
        if (sm + arr[i] <= s) {
            cnt += 1;
            sm += arr[i];
            last_idx = i;
        }
    }

    sm -= arr[last_idx];

    int mx = 0;
    for (int i = last_idx + 1; i < n; ++i) {
        if (sm + arr[i] <= s) {
            mx = arr[i];
        }
    }

    cout << cnt << ' ' << mx << '\n';




    return 0;
}
