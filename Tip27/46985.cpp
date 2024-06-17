//
// 18.05.2024

#include <iostream>
#include <map>

using namespace std;

#define int long long

constexpr int MAXN = 2'000'000;
constexpr int k = 999;

int cnt[k];
int arr[MAXN];
int pref[MAXN];

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("/mnt/d/Users/Matvei/Developer/Projects/InfEge/Tip27/inputs/46985/27-B.txt", "r", stdin);

    int n;
    cin >> n;

    for (int i = 1; i < n + 1; ++i) {
        cin >> arr[i];
        pref[i] = (pref[i - 1] + arr[i]) % k;
    }

    int ans = 0;
    cnt[0] = 1;
    for (int r = 1; r < n + 1; ++r) {
        ans += cnt[pref[r]];
        ++cnt[pref[r]];
    }

    cout << ans << '\n';

    // int ans2 = 0;
    // for (int l = 1; l < n + 1; ++l) {
    //     int sm = 0;
    //     for (int r = l; r < n + 1; ++r) {
    //         sm += arr[r];
    //         if (sm % k == 0) {
    //             ++ans2;
    //         }
    //     }
    // }
    //
    // cout << ans2 << '\n';
    return 0;
}
