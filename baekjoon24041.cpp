#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

int main(){
    long long n,g,k;
    cin>>n>>g>>k;

    vector<long long>s;
    vector<long long>l;
    vector<long long>o;

    for(int i=0;i<n;i++){
        long long si,li,oi;
        cin>>si>>li>>oi;
        s.push_back(si);
        l.push_back(li);
        o.push_back(oi);
    }

    long long end=2000000000;
    long long start=0;
    long long x=0;
    long long prev=0;
    long long dap=0;
    while(start<=end){
       x=start+(end-start)/2;
       //cout<<x<<"\n";
        long long cellNum=0;
        priority_queue<long long>pq;
        for(int i=0;i<n;i++){
            long long tmp=max(1ll,x-l[i]);
            tmp=tmp*s[i];
            cellNum+=tmp;
            if(o[i]==1) pq.push(tmp);
        }
        long tmpK=k;
        if(cellNum>g){
            while(tmpK>0&&pq.size()>0){
                cellNum-=pq.top();
                pq.pop();
                tmpK--;
            }
        }
        //cout<<"cellNum : "<<cellNum<<"\n";
        if(cellNum>g){
            end=x-1;
        }else{
            start=x+1;
            dap=x;
        }
    }
    cout<<dap;

}