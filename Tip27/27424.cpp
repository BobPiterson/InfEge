//
// 18.05.2024

#include <iostream>

using namespace std;

#define int long long

constexpr int k = 3;
constexpr int MAXN = 100'000;
pair<int, int> arr[MAXN];

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    freopen("/mnt/d/Users/Matvei/Developer/Projects/InfEge/Tip27/inputs/27424/27-B.txt", "r", stdin);

    int n;
    cin >> n;

    int min_diff = 1e10;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i].first >> arr[i].second;
        if (arr[i].first > arr[i].second) {
            swap(arr[i].first, arr[i].second);
        }
        if (arr[i].first % k != 0 && arr[i].first % k != arr[i].second % k  && (arr[i].second - arr[i].first < min_diff)) {
            min_diff = arr[i].second - arr[i].first;
        }
    }

    int sm = 0;
    for (int i = 0; i < n; ++i) {
        sm += arr[i].second;
    }

    cout << sm << '\n';
    if (sm % k == 0) {
        cout << "DIV\n";
        sm -= min_diff;
    }

    cout << sm << '\n';
    if (sm % k == 0) {
        cout << "DIV\n";
        sm -= min_diff;
    }
    return 0;
}
