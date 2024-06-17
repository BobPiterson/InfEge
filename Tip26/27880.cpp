//  
// 22.04.2024

#include <iostream>

using namespace std;

#define int long long

signed main() {
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);

    freopen(R"(/mnt/d/Users/Matvei/Developer/Projects/InfEge/Tip26/inputs/27880.txt)", "r", stdin);

    int s, n;
    cin >> s >> n;

    int arr[n];
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    sort(arr, arr + n);

    int cnt = 0;
    int sm = 0;

    for (int i = 0; i < n; ++i) {
        if (sm + arr[i] > s) {
            break;
        }
        sm += arr[i];
        ++cnt;
    }

    sm -= arr[cnt - 1];
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        if (sm + arr[i] > s) {
            ans = arr[i - 1];
            break;
        }
    }

    cout << cnt << ' ' << ans << '\n';


    return 0;
}
