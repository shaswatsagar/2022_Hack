// undirected weighted graph representation using adjacency list
#include<iostream>
#include<vector>
using namespace std;
int main(){
int V,E;
cout<<"enter no. of vertices and edges: "<<endl;
cin>>V>>E;
vector<pair<int,int>> vec[V+1];
for(int i=1; i< E+1; i++){
    int u,v, wt;
    cout<< "enter edges and weight"<<endl;
    cin>>u>>v>>wt;
    vec[u].push_back({v,wt});
    vec[v].push_back({u,wt});
} 
for(int i=1; i<V+1;i++){
cout<<"\n"<<i<<"-->";
    for(auto x: vec[i]){
    cout<<x.first <<" "<< x.second<<" ";
    }
    }
    return 0;
    }