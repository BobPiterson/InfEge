//  
// 14.05.2024

#include <iostream>
#include <set>

using namespace std;

#define int long long

bool check(int sm, bool odd) {
    return sm % 2 == 1 && odd || sm % 2 == 0 && !odd;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("/mnt/d/Users/Matvei/Developer/Projects/InfEge/Tip27/inputs/33772/27-B.txt", "r", stdin);

    int n;
    cin >> n;

    int arr[n][2];
    for (int i = 0; i < n; ++i) {
        cin >> arr[i][0] >> arr[i][1];
        if (arr[i][0] > arr[i][1]) {
            swap(arr[i][0], arr[i][1]);
        }
    }

    int sm = 0;
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        sm += arr[i][0];
        cnt += arr[i][0] % 2;
    }

    bool odd = cnt > n / 2;

    set<int> used;
    for (int i = 0; i < 10; ++i) {
        if (check(sm, cnt > n / 2)) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
            int mn_right = 1e9;
            int mn_right_idx = -1;
            for (int i = 0; i < n; ++i) {
                if (!used.contains(i) && abs(arr[i][0] - arr[i][1]) < mn_right && (
                        odd && arr[i][0] % 2 == 1 && arr[i][1] % 2 == 0 || !odd && arr[i][0] % 2 == 0 && arr[i][1] % 2
                        == 1)) {
                    mn_right = abs(arr[i][0] - arr[i][1]);
                    mn_right_idx = i;
                }
            }
            used.insert(mn_right_idx);
            sm += -arr[mn_right_idx][0] + arr[mn_right_idx][1];
            if (arr[mn_right_idx][0] % 2 == 1) {
                --cnt;
            }
            if (arr[mn_right_idx][1] % 2 == 1) {
                ++cnt;
            }
        }
    }


    cout << sm << '\n';


    return 0;
}
