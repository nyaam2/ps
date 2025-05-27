#include<iostream>
#include<vector>
#include<string>
using namespace std;
class Solution{
public:

    int find(vector<int>&parent,int i){
        if(parent[i]!=i) parent[i]=find(parent,parent[i]);
        return parent[i];
    }
    void unionFind(int x,int y,vector<int>&parent){
        int px=find(parent,x);
        int py=find(parent,y);
        if(px!=py){
            parent[px]=py;
        }
        
    }
    int regionsBySlashes(vector<string>&grid){
        int n=grid.size();
        int size=n*n*4;
        vector<int> parent(size);

        for(int i=0;i<size;i++)parent[i]=i;

        for(int r=0;r<n;r++){
            for(int c=0;c<n;c++){
                int root=(r*n+c)*4;

                char ch=grid[r][c];
                if(ch==' '){
                    unionFind(root+0,root+1,parent);
                    unionFind(root+1,root+2,parent);
                    unionFind(root+2,root+3,parent);
                }else if(ch=='/'){
                    unionFind(root+0,root+3,parent);
                    unionFind(root+1,root+2,parent);
                }else{
                    unionFind(root+0,root+1,parent);
                    unionFind(root+2,root+3,parent);
                }

                 if(r+1<n){
                    int bottom=((r+1)*n+c)*4;
                    unionFind(root+2,bottom,parent);
                    }
                if(c+1<n){
                    int right=(r*n+c+1)*4+3;
                    unionFind(root+1,right,parent);
                }
            }
           
        }
        int dap=0;
        for(int i=0;i<size;i++){
            if(find(parent,i)==i)dap++;
        }
        return dap;
    }

};