#include <bits/stdc++.h>
#include "graphs.h"
#include "graphs_algorithm.h"

using namespace std;

int main(){
    //creating graph
    int a,b,N,M, weight=0;
    cout << "Number of starting nodes: ";
    cin >> N;
    cout << "Number of edges to init: ";
    cin >> M;

    vector<graphEdge> graphEdges;
    int number_of_nodes = N;
    int num_edges = 0;
    Graph graph(graphEdges, num_edges, number_of_nodes);
    graph.Display();

    //input
    for(int i = 0; i < M; i++){
        cout << "Starting node: ";
        cin >> a;
        cout << "Arrival node: ";
        cin >> b;
        cout << "Weight for the edge (0 for no weight): ";
        cin >> weight;
        graphEdge new_edge = {a,b,weight};
        graph.AddEdge(new_edge);
    }

    graph.Display();
    BFS(&graph, 0);
    FloydWarshall(&graph);
    BellmanFord(&graph, 0);
    graph.head_node[0];
    isCyclic(&graph);
    vector<int> parent(graph.number_of_nodes, -1); 
    vector<vector<int> > mat = graph.ConvertToMatrix();
    int flow = FordFulkerson(0, 5, &graph);

    return 0;
}