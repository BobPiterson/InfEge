//  
// 03.06.2024

#include <iostream>

using namespace std;

#define int long long

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("/mnt/d/Users/Matvei/Developer/Projects/InfEge/Tip27/inputs/28131/27_B.txt", "r", stdin);

    constexpr int m = 120;

    int n;
    cin >> n;

    int arr[n];
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    int mx = -1e9;
    pair<int, int> ans;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int sm = arr[i] + arr[j];
            if (arr[i] > arr[j] && sm % m == 0) {
                if (sm > mx) {
                    mx = sm;
                    ans = {arr[i], arr[j]};
                }
            }
        }
    }

    cout << ans.first << ' ' << ans.second << '\n';


    return 0;
}
