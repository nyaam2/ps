#include<iostream>
#include<vector>

#define all(x) (x).begin(), (x).end()

#define INF 0x7FFFFFFF

using namespace std;

using ll = long long;
using ld = long double;
using pii = pair<int,int>;
using pll = pair<ll, ll>;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n, m;
    cin >> n >> m;
    vector<int> arr(n+1);
    for(int i = 0; i < m; i++) {
        int s, e;
        cin >> s >> e;
        if(s < e) continue;
        for(int j = e; j < s; j++) {
            arr[j] = 1;
        }
    }

    for(int i = 1; i <= n; i++) {
        if(n % i) continue;
        bool flag = false;
        for(int j = i; j <= n; j += i) {
            if(arr[j]) {
                flag = true;
                break;
            }
        }
        if(flag) continue;
        cout << n / i;
        return 0;
    }

    return 0;
}