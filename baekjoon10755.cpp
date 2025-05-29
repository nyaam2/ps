#include<iostream>
#include<vector>
#include<set>
using namespace std;

class Solution {

public:
    int find(int x,vector<int>&parent){
        if(parent[x]!=x)parent[x]=find(parent[x],parent);
        return parent[x];
    }
    void unionn(int x,int y,vector<int>&parent,vector<int>&rank){
        int rootX=find(x,parent);
        int rootY=find(y,parent);

        if(rank[rootX]<rank[rootY]){
            parent[rootX]=rootY;
        }
        else if(rank[rootY]<rank[rootX]){
            parent[rootY]=rootX;
        }else{
            parent[rootY]=rootX;
            rank[rootX]++;
        }

    }
    int numIslands(vector<vector<char>>& grid) {
        int n=grid[0].size();
        int m=grid.size();
        set<int>s;
        vector<int>parent(n*m);
        vector<int>rank(n*m);
        for(int i=0;i<n*m;i++){
            parent[i]=i;
            rank[i]=0;
        }
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]=='1'){
                   
                    if(j<n-1&&grid[i][j+1]=='1') unionn(i*n+j,i*n+(j+1),parent,rank);
                    if(i<m-1&&grid[i+1][j]=='1') unionn(i*n+j,(i+1)*n+j,parent,rank);
                   
                    
                     
                }
            }
        }
        int dap=0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                
                if(grid[i][j]=='1'&&parent[i*n+j]==i*n+j)dap++;
        }
        }

        return dap;
    }
};