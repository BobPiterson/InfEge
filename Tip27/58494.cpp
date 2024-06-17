//  
// 18.05.2024

#include <iostream>

using namespace std;

#define int long long
int cnt[9][9];

int arr[3342138];

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("/mnt/d/Users/Matvei/Developer/Projects/InfEge/Tip27/inputs/58494/27-B.txt", "r", stdin);

    int n;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    int ans = 0;
    for (int r = 0; r < n; ++r) {
        for (int x = 0; x < 9; ++x) {
            for (int y = 0; y < 9; ++y) {
                if ((arr[r] % 9 + x) % 9 == (r % 9 - y + 9) % 9) {
                    ans += cnt[x][y];
                }
            }
        }
        ++cnt[arr[r] % 9][r % 9];
    }

    cout << ans << '\n';
    // 0 1 2 3 4 5 6 7 8 9 10 11 12 13
    // 0 1 2 3 4 5 6 7 8 0 1  2  3  4
    //

    return 0;
}