//  
// 03.06.2024

#include <iostream>
#include <array>
#include <set>
#include <vector>

using namespace std;

#define int long long

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("/mnt/d/Users/Matvei/Developer/Projects/InfEge/Tip27/inputs/64957/27_B.txt", "r", stdin);

    constexpr int m = 105;

    int n;
    cin >> n;

    array<vector<int>, m> arr{};
    for (int i = 0; i < n; ++i) {
        int val;
        cin >> val;
        arr[val % m].emplace_back(val);
    }

    vector<int> all;
    for (int i = 0; i < m; ++i) {
        sort(arr[i].begin(), arr[i].end(), greater<>());
        all.emplace_back(arr[i][0]);
        all.emplace_back(arr[i][1]);
        all.emplace_back(arr[i][2]);
    }
    int mx = 0;

    for (int i = 0; i < all.size(); ++i) {
        for (int j = i + 1; j < all.size(); ++j) {
            for (int k = j + 1; k < all.size(); ++k) {
                int sm = all[i] + all[j] + all[k];
                if (sm % m == 0) {
                    mx = max(mx, sm);
                }
            }
        }
    }
    cout << mx << '\n';

    return 0;
}
