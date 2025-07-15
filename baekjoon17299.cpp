#include<iostream>
#include<map>
#include<stack>
#include<vector>
#include<unordered_map>
using namespace std;

int main(){
    unordered_map<int,int>m;
    map<int,int>m2;
    stack<int>s1;
    stack<int>s2;

    ios::sync_with_stdio(false);
	cin.tie(NULL);

    int n;
    cin>>n;
    vector<int>result(n);

    for(int i=0;i<n;i++){
        int a;
        cin>> a;
        m[a]++;
        
        s1.push(a);
    }
    

    for(int i=n-1;i>=0;i--){
        int p=s1.top(); s1.pop();
        if(!s2.empty()){
            while(!s2.empty()&&m[s2.top()]<=m[p]){
                s2.pop();
            }
            if(!s2.empty()&&m[p]<m[s2.top()]) result[i]=s2.top();
            else result[i]=-1;

            s2.push(p);

        }else{
            s2.push(p);
            result[i]=-1;
        }
    }
    for(int i=0;i<n;i++){
        cout<<result[i]<<" ";
    }
}