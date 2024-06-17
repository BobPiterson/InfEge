#include <bitset>
#include <iostream>

using namespace std;

#define int long long

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    for (int N = 0; N < 256; ++N) {
        uint8_t x = ~uint8_t(N);
        int R = (int)(x) - N;
        if (R == 45) {
            cout << N;
            break;
        }
    }
    return 0;
}
