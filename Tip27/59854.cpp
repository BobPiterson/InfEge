//
// 18.05.2024

#include <iostream>
#include <set>

using namespace std;

#define int long long

constexpr int MAXN = 5'000'001;
int arr[MAXN];

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("/mnt/d/Users/Matvei/Developer/Projects/InfEge/Tip27/inputs/59854/27-B.txt", "r", stdin);

    int k, n;
    cin >> k >> n;

    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    int ans1 = 0;
    // for (int r = 0; r < n; ++r) {
    //     for (int l = 0; l < r - k; ++l) {
    //         ans1 = max(ans1, arr[r] + arr[l]);
    //     }
    // }

    // int ans2 = 0;
    // set<int, greater<>> set1;
    // for (int r = 0; r < n; ++r) {
    //     if (!set1.empty()) {
    //         ans2 = max(ans2, *set1.begin() + arr[r]);
    //     }
    //     if (r - k >= 0) {
    //         set1.insert(arr[r - k]);
    //     }
    // }

    int ans2 = 0;
    int mx = -1e9;
    for (int r = 0; r < n; ++r) {
        ans2 = max(ans2, mx + arr[r]);
        if (r - k >= 0) {
            mx = max(mx, arr[r - k]);
        }
    }

    cout << ans1 << '\n';
    cout << ans2 << '\n';

    return 0;
}
