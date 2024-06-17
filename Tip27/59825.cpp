//
// 18.05.2024

#include <iostream>

using namespace std;

#define int long long

constexpr int MAXN = 1'000'000;
int arr[MAXN];
pair<int, int> sorted[MAXN];

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("/mnt/d/Users/Matvei/Developer/Projects/InfEge/Tip27/inputs/59825/27-A.txt", "r", stdin);

    int k, n;
    cin >> k >> n;
    k *= 2;

    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        sorted[i] = {arr[i], i};
    }

    sort(sorted, sorted + n, greater<>());

    int dist = abs(sorted[0].second - sorted[1].second);

    int ans = sorted[0].first + sorted[1].first;
    if (dist >= k) {
        ans += sorted[2].first;
    } else {
        int i1 = sorted[0].second;
        int i2 = sorted[1].second;

        int mx = -1;
        for (int i = 0; i < n; ++i) {
            if (abs(i - i1) >= k || abs(i - i2) >= k) {
                mx = max(mx, arr[i]);
            }
        }
        if (mx == -1) {
            cout << "FAULT\n";
            ans = -1;
        } else {
            ans += mx;
        }
    }

    // int ans2 = 0;
    // for (int i = 0; i < n; ++i) {
    //     for (int j = i + 1; j < n; ++j) {
    //         for (int g = j + 1; g < n; ++g) {
    //             if (g - i >= k) {
    //                 ans2 = max(ans2, arr[i] + arr[j] + arr[g]);
    //             }
    //         }
    //     }
    // }

    cout << ans << '\n';
    // cout << ans2 << '\n';


    return 0;
}
