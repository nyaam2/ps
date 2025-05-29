#include<iostream>
#include<vector>
using namespace std;

int find(int x,vector<int>&parent){
    if(x!=parent[x]) parent[x]=find(parent[x],parent);
    return parent[x];
}
void unionn(int x,int y,vector<int>&parent){
    int rootX=find(x,parent);
    int rootY=find(y,parent);

    if(rootX<rootY){
        parent[rootY]=rootX;
    }else{
        parent[rootX]=rootY;
    }

} 
int main(){
    int G,P;    //G: gate수, P: 비행기 수
    cin>>G;
    cin>>P;

    vector<int>airplaneGates; //비행기
    vector<int>parent(G+1); //부모
    vector<bool>full(G+1); //도킹되었는지 여부

    for(int i=0;i<=G;i++){
        parent[i]=i;
        full[i]=false;
    }

    int dap=0;

    for(int i=0;i<P;i++){
        int tmp;
        cin>>tmp;
        airplaneGates.push_back(tmp);
    }

    for(int i=0;i<airplaneGates.size();i++){
        int airplaneGate=airplaneGates[i];

        //비어있을 경우
        if(full[airplaneGate]==false){

            full[airplaneGate]=true;    dap++;
            if(airplaneGate>1&&full[airplaneGate-1]==true){
                unionn(airplaneGate,airplaneGate-1,parent);
            }
            if(airplaneGate<G&&full[airplaneGate+1]==true){
                unionn(airplaneGate,airplaneGate+1,parent);
            }
        }
        else{
            int ableDockingGate=find(airplaneGate,parent)-1;
            if(ableDockingGate==0){
                cout<<dap;
                return 0;
            }else{
                full[ableDockingGate]=true;   dap++;

                
                unionn(ableDockingGate,airplaneGate,parent);
                if(ableDockingGate-1>=1&&full[ableDockingGate-1]==true){
                    unionn(ableDockingGate,ableDockingGate-1,parent);
                }
            }
        }
    }
    cout<<dap;
}
