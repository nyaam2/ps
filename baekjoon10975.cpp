#include<iostream>

#include<vector>
#include<deque>
#include<algorithm>

using namespace std;

int main(){
    int n;
    cin>>n;

    vector<int>v;
    vector<int>sortedV;
    bool visited[50]={};

    for(int i=0;i<n;i++){

        int tmp;
        cin>>tmp;
        v.push_back(tmp);
        sortedV.push_back(tmp);

    }

    sort(sortedV.begin(),sortedV.end());
    int dap=0;
    for(int i=0;i<n;i++){
        int idx=0;
        for(int j=0;j<n;j++){
            if(v[i]==sortedV[j]){
                idx=j;
                break;
            }
        }
        if(idx==0){
            if(visited[idx+1]==false){
                dap++;
                visited[idx]=true;
            }
        }
        else if(idx==n-1){
            if(visited[idx-1]==false){
                dap++;
                visited[idx]=true;
            }
        }
        else if(visited[idx-1]||visited[idx+1]){
            visited[idx]=true;
            continue;
        }else{
            visited[idx]=true;
            dap++;
        }
    }
    cout<<dap<<"\n";


    

    

   
    

    

}
