//  
// 01.06.2024

#include <iostream>

using namespace std;

#define int long long

constexpr int MAXN = 1000000;
int arr[MAXN];
pair<int, int> sorted[MAXN];

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("/mnt/d/Users/Matvei/Developer/Projects/InfEge/variants/16006836/inputs/27_A.txt", "r", stdin);

    int n, k;
    cin >> n >> k;

    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        sorted[i] = {arr[i], i};
    }

    sort(sorted, sorted + n);

    int mn = 1e9;
    //
    // for (int i = 0; i < 3; ++i) {
    //     mn *= sorted[i].first;
    // }

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            for (int g = j + 1; g < n; ++g) {
                if (abs(i - j) >= k && abs(j - g) >= k) {
                    mn = min(mn, arr[i] * arr[j] * arr[g]);

                    if (mn == arr[i] * arr[j] * arr[g]) {
                        cout << arr[i] << ' ' << arr[j] << ' ' << arr[g] << '\n';
                    }
                }
            }
        }
    }

    cout << mn << '\n';


    return 0;
}
