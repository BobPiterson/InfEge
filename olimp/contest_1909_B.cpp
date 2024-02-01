// https://codeforces.com/contest/1909/problem/B

#include <iostream>
#include <vector>
#include <set>

using namespace std;

#define int long long

signed main() {
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        int a[n];
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }

        for (int i = 1; i < 63; ++i) {
            unsigned int d = (1ull << i);
            set<int> set1;
            for (int j = 0; j < n; ++j) {
                set1.insert(a[j] % d);
            }

            if (set1.size() == 2) {
                cout << d << '\n';
                break;
            }
        }
    }

    return 0;
}
