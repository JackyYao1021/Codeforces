#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>

using namespace std;


void solve() {
    int n, q;
    cin >> n >> q;

    vector<pair<long long, int>> elements(n);

    for (int i = 0; i < n; ++i) {
        long long value;
        cin >> value;
        elements[i] = {value, i};
    }

    sort(elements.begin(), elements.end());

    int mask = 0;

    for (int target = 0; target < n; ++target) {
        int original = elements[target].second;
        mask |= original ^ target;
    }

    if (mask == 0) {
        cout << 0 << '\n';
        return;
    }

    int answer = 1 << (31 - __builtin_clz(mask));

    cout << answer << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        solve();
    }

    return 0;
}