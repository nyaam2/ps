#include<iostream>
#include<stack>
using namespace std;

int main(){

    stack<int>s;

    int n;
    cin>>n;
    int accumulation=0;
    int dap=0;
    for(int i=0;i<n;i++){
        int x,y;
        cin>>x>>y;
        if(!s.empty()){
            if(s.top()<y){
                 if(y!=0) s.push(y);
            }else{
                while(!s.empty()&&s.top()>y){
                    s.pop();
                    dap++;
                }
                while(!s.empty()&&s.top()==y){
                    s.pop();
                }
                if(y!=0) s.push(y);
            }
        }else{
             if(y!=0) s.push(y);
        }
    }
    
    cout<<dap+s.size();



}