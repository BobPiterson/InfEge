//
// 18.05.2024

#include <iostream>
#include <map>

using namespace std;

#define int long long

constexpr int MAXN = 1781758;
int pref[MAXN + 1];
int pref_sum[MAXN + 1];
int arr[MAXN + 1];

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("/mnt/d/Users/Matvei/Developer/Projects/InfEge/Tip27/inputs/39256/27-B.txt", "r", stdin);

    int k = 10;

    int n;
    cin >> n;


    pref[0] = 0;
    pref_sum[0] = 0;
    for (int i = 1; i <= n; ++i) {
        cin >> arr[i];
        pref[i] = (pref[i - 1] + arr[i] % 2) % k;
        pref_sum[i] = pref_sum[i - 1] + arr[i];
    }

    map<int, int> map1;
    map1[0] = 0;
    int mx = -1;
    for (int r = 1; r <= n; ++r) {
        mx = max(mx, pref_sum[r] - pref_sum[map1[k - pref[r]]]);
        if (map1[k - pref[r]] == 0) {
            map1.erase(k - pref[r]);
        }
        if (!map1.contains(pref[r])) {
            map1[pref[r]] = r;
        }
    }

    cout << mx << '\n';
    //
    // int mx2 = 0;
    // for (int l = 1; l <= n; ++l) {
    //     int sm = 0;
    //     int cnt = 0;
    //     for (int r = l; r <= n; ++r) {
    //         sm += arr[r];
    //         cnt += arr[r] % 2;
    //         if (cnt % k == 0) {
    //             mx2 = max(mx2, sm);
    //         }
    //     }
    // }
    //
    // cout << mx2 << '\n';
    return 0;
}
