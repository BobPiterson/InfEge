//  
// 03.06.2024

#include <iostream>

using namespace std;

#define int long long

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("/mnt/d/Users/Matvei/Developer/Projects/InfEge/Tip27/inputs/37162/27_B.txt", "r", stdin);

    constexpr int m = 89;

    int n;
    cin >> n;

    int arr[n];
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    int mx = -1e9;
    int mn_len = 1e9;
    for (int l = 0; l < n; ++l) {
        int sm = 0;
        for (int r = l; r < n; ++r) {
            sm += arr[r];
            if (sm % m == 0 && sm >= mx) {
                if (sm == mx) {
                    mn_len = min(mn_len, r - l + 1);
                } else {
                    mx = sm;
                    mn_len = r - l + 1;
                }
            }
        }
    }

    cout << mn_len << '\n';

    return 0;
}
