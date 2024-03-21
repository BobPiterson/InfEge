//  
// 17.03.2024

#include <iostream>

using namespace std;

bool f(int x, int y, int z, int w) {
    return (x <= (y == w)) && (y == (w <= z));
}

int main() {
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);

    cout << "xyzwf\n";
    for (int x = 0; x < 2; ++x) {
        for (int y = 0; y < 2; ++y) {
            for (int z = 0; z < 2; ++z) {
                for (int w = 0; w < 2; ++w) {
                    if (f(x, y, z, w)) {
                        cout << x << y << z << w << f(x, y, z, w) << '\n';
                    }
                }
            }
        }
    }

    return 0;
}


/*
0 0 1 0 0
0 0 0 1 1
0 1 0 0 1
0 1 1 0 1
0 1 1 1 1


 */