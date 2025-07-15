#include <iostream>
#include <stack>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    stack<pair<int, int>> st; // (키, 같은 키 개수)
    ll ans = 0;

    for(int i=0;i<n;i++){
        int a; cin>>a;
        int cnt=1;
        while(!st.empty()&&st.top().first<=a){

            ans+=st.top().second;

            if(st.top().first==a){
                cnt+=st.top().second;
            }
            st.pop();
        }

        if(!st.empty()){
            ans+=1;
        }

        cout<<ans<<"\n";

        st.push({a,cnt});
    }
    cout<<ans;
}
