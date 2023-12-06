#include <bits/stdc++.h>
#include "graphs.h"
#include "bipartite.h"
#include "graphs_algorithm.h"

using namespace std;

int main(){
    //creating graph
    int a,b,N,M, weight=0;
    cout << "Number of starting nodes: ";
    cin >> N;
    cout << "Number of edges to init: ";
    cin >> M;

    
    int number_of_nodes = N;
    int num_edges = 0;
    Graph graph(number_of_nodes);

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
    BellmanFord(&graph, 0, 3);
    //graph.head_node[0];
    //isCyclic(&graph);
    //vector<int> parent(graph.number_of_nodes, -1); 
    //vector<vector<int> > mat = graph.ConvertToMatrix();
    //int flow = FordFulkerson(0, 5, &graph);

    const int jobs = 3;
    const int worker = 3;

    int array[jobs][worker] = {{8, 5, 9}, {4, 2, 4}, {7, 3, 8}};

    // Convertir le tableau statique en un vecteur 2D
    std::vector<std::vector<int> > costs;
    for (int i = 0; i < jobs; ++i) {
        std::vector<int> row(array[i], array[i] + worker);
        costs.push_back(row);
    }  
    std::vector<int> myVector;

    vector<int> answers;
    answers = BipartiteGraph::Hungarian(costs);
    for(int i = 0; i < jobs; i++){
        cout << "Job " << i << " cost at least : " << answers[i] << endl;
    }

    return 0;
}