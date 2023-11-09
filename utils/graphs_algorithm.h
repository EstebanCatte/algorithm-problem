#ifndef graphs_algorithm
#define graphs_algorithm

#include "graphs.h"
#include <bits/stdc++.h>
using namespace std;
#define INF 2147483647

//shortest path problems between all pairs of vertices
void FloydWarshall(Graph *graph)
{
    vector<vector<int> > Mat = graph->ConvertToMatrix();
    cout << "===========================" << endl;
    cout << "       Floyd Warshall      " << endl;
    cout << "===========================" << endl;
    int V = graph->number_of_nodes;
    int i, j, k;
    for (k = 0; k < V; k++) {
        for (i = 0; i < V; i++) {
            for (j = 0; j < V; j++) {
                if (Mat[i][j] > (Mat[i][k] + Mat[k][j]) && (Mat[k][j] != INF && Mat[i][k] != INF)){
                    Mat[i][j] = Mat[i][k] + Mat[k][j];
                }
            }
        }
    }
    graph->PrintMatrix(Mat);
}


// The main function that finds shortest distances from src
// to all other vertices using Bellman-Ford algorithm.  The
// function also detects negative weight cycle
void BellmanFord(Graph* graph, int src)
{
    cout << "===========================" << endl;
    cout << "        Bellman Ford       " << endl;
    cout << "===========================" << endl;

    int V = graph->number_of_nodes;
    int E = graph->GetNumEdges();
    int dist[V];
 
    // Initialize distances from src to all other
    // vertices as INFINITE
    for (int i = 0; i < V; i++)
        dist[i] = INF;
    dist[src] = 0;
 
    // Relax all edges |V| - 1 times. A simple
    // shortest path from src to any other vertex can have
    // at-most |V| - 1 edges
    for (int i = 1; i <= V - 1; i++) {
        for (int j = 0; j < E; j++) {
            int u = graph->edge_list[j].source;
            int v = graph->edge_list[j].destination;
            int weight = graph->edge_list[j].weight;
            if (dist[u] != INF && dist[u] + weight < dist[v]){
                dist[v] = dist[u] + weight;
            }
        }
    }
 
    // check for negative-weight cycles.  The above
    // step guarantees shortest distances if graph doesn't
    // contain negative weight cycle.  If we get a shorter
    // path, then there is a cycle.
    for (int i = 0; i < E; i++) {
        int u = graph->edge_list[i].source;
        int v = graph->edge_list[i].destination;
        int weight = graph->edge_list[i].weight;
        if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) {
            cout << "Graph contains negative weight cycle" << endl;
            return; // If negative cycle is detected, simply
                    // return
        }
    }
    cout << "Vertex Distance from Source" << endl;
    for (int i = 0; i < V; i++)
        cout << i << "\t\t" << dist[i] << endl;
    return;
}


//Explore the graph vertically
bool dfsCheck(int node, Graph* graph, vector<int> &vis, vector<int> &pathVis) {
    vis[node] = 1;
    pathVis[node] = 1;

    Node *obj = NULL;
    if (sizeof(graph->head_node[node]) != 0){
        obj = graph->head_node[node];
    }
    while (obj != NULL){
        if (!vis[obj->value]){
            if (dfsCheck(obj->value, graph, vis, pathVis) == true)
                return true;
        }
        // if the node has been previously visited
        // but it has to be visited on the same path
        else if (pathVis[obj->value]) {
            return true;
        }
        obj = obj->next;
    }
    pathVis[node] = 0;
    return false;
}


// Function to detect cycle in a directed graph.
//Recursively, use DFS search
bool isCyclic(Graph* graph) {
    int V = graph->number_of_nodes;
    vector<int> vis(V, 0);
    vector<int> pathVis(V, 0);

    for (int i = 0; i < V; i++) {
        if (!vis[i]) {
            if (dfsCheck(i, graph, vis, pathVis) == true){
                cout << "Cycle detected" << endl;
                return true;
            }
        }
    }
    cout << "No Cycle detected" << endl;
    return false;
}


//Detect if a path is possible between <source> and <target>
//Use BFS search and a matrix with 0's for empty edges (contrary to INF)
int IsPathExist(int source, int target, int n, vector<int>& parent,vector<vector<int> >& graph)
{
    fill(parent.begin(),parent.end(),-1);
    parent[source] = -2;
    queue<pair<int,int> > q;
    q.push({source,1e9});
    while(!q.empty()){
        int u = q.front().first;
        int cap = q.front().second;
        q.pop();
        for(int v=0;v<n;v++){
            if(u!=v && graph[u][v]!=0 && parent[v]==-1){
                parent[v] = u;
                //Updating the minimum capacity
                int min_cap = min(cap,graph[u][v]);
                if(v==target){
                    return min_cap;
                }
                q.push({v,min_cap});
            }
        }
    }
    return 0;
}


//Max Flow algorithm between two points if the path exists
int FordFulkerson(int source, int target, Graph *graph)
{
    vector<vector<int> > mat = graph->ConvertToMatrix(0);
    int n = graph->number_of_nodes;
    vector<int> parent(n,-1);
    int max_flow = 0;
    int min_cap = 0;
    while(min_cap = IsPathExist(source,target,n,parent,mat)){
        max_flow += min_cap;
        int v = target;
        while(v!=source){
            int u = parent[v];
            mat[u][v] -= min_cap;
            mat[v][u] += min_cap;
            v=u;
        }
    }
    cout << "Maximum Flow Using Ford Fulkerson Algo: " << max_flow << endl;
    return max_flow;
}


//Explore the graph horizontally without going multiple times on the same node
//Useful because the adjency list may contain multiple object for the same vertex
void BFS(Graph *graph, int source)
{
    cout << "===========================" << endl;
    cout << "       BFS ALGORITHM       " << endl;
    cout << "===========================" << endl;
    vector<bool> visited;
    visited.resize(graph->number_of_nodes, false);
    list<int> queue;
    // Mark the current node as visited and enqueue it
    visited[source] = true;
    queue.push_back(source);

    while (!queue.empty()) 
    {
        source = queue.front();
        cout << source << " ";
        queue.pop_front();
        // ====PUT GOAL HERE====
        // Get all adjacent vertices of the dequeued
        // vertex s.
        // If an adjacent has not been visited,
        // then mark it visited and enqueue it
        for (int k = 0; k < graph->number_of_nodes; k++)
        {
            if (!visited[k]) 
            {
                visited[k] = true;
                queue.push_back(k);
            }
        }
    }
    cout << endl;
}



#endif