#include<iostream>
#include<vector>
using namespace std;

int find(int x,vector<int>&parent){
    if(parent[x]!=x) parent[x]=find(parent[x],parent);
    return parent[x];
}
void unionn(int x,int y,vector<int>&parent,vector<int>&rank){
    int rootX=find(x,parent);
    int rootY=find(y,parent);

    if(rank[rootX]<rank[rootY]){
        parent[rootX]=rootY;
    }
    else if(rank[rootX]>rank[rootY]){
        parent[rootY]=rootX;
    }
    else{
        parent[rootY]=rootX;
        rank[rootX]++;
    }
}

int main(){
    int n,m;
    cin>>n>>m;
   ios_base::sync_with_stdio(0);
cin.tie(0);
cout.tie(0);
    

    vector<int>parent(n+1);
    vector<int>rank(n+1);

    for(int i=0;i<=n;i++){
        parent[i]=i;
    }
    for(int i=0;i<m;i++){
        int d,a,b;
        cin>>d>>a>>b;
      
        if(d==0){
            unionn(a,b,parent,rank);
        }else{
            int pa=find(a,parent);
            int pb=find(b,parent);
            if(pa!=pb) cout<<"NO"<<"\n";
            else cout<<"YES"<<"\n";
        }
        
    }
}
