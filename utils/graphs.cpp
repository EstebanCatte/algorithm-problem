#include <bits/stdc++.h>
using namespace std;
#include <typeinfo>
#include <vector>

//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

struct Node
{
    int value, weight;
    Node* next;
};

struct graphEdge {
    int source, destination;
};


class Graph {

    // Create a new node for the adjacency list
    Node* getNeighbourVertex(int destination, Node* head_node){
        Node* new_node = new Node;
        new_node->value = destination;
        new_node->next = head_node;
        new_node->weight = 0;

        return new_node;
    }

    int number_of_nodes;
    int number_of_edges;
    
    public:
        Node **head_node;

        //constructor
        Graph(vector<graphEdge> graphEdges, int num_of_edge, int num_of_node){
            this->number_of_nodes = num_of_node;
            this->number_of_edges = num_of_edge;
            // dynamic memory allocation
            head_node = new Node*[num_of_node]();

            // initialize headnode for every edge of graph
            for (int k = 0; k < num_of_node; k++) {
                head_node[k] = NULL;
            }

            if(num_of_edge > 0){
                for (int k = 0; k < num_of_edge; k++){
                    int source = graphEdges[k].source;
                    int destination = graphEdges[k].destination;

                    Node* new_node = getNeighbourVertex(destination, head_node[source]);
                    head_node[source] = new_node;
                }
            }
        }

        //destructor
        ~Graph() {
            for (int k = 0; k < number_of_nodes; k++) {
                delete[] head_node[k];
            }
            delete[] head_node;
        }


    void AddEdge(graphEdge edge){
        int source = edge.source;
        int destination = edge.destination;
        Node* new_node = getNeighbourVertex(destination, head_node[source]);
        head_node[source] = new_node;
        number_of_edges+=1;
    }


    Node* GetEdge(graphEdge edge){
        int source = edge.source;
        int destination = edge.destination;
        Node *node;
        node = head_node[source];
        while (node != NULL){
            if (node->value == destination){
                return node;
            }
            node = node->next;   
        }
    }


    void SetEdgeWeight(graphEdge edge, int weight){
        Node *node = GetEdge(edge);
        node->weight = weight;
    }


    void Display(){
        cout << "=== Current Graph status ===" << endl;
        Node *display_node;
        for (int k = 0; k < number_of_nodes; k++) {
            display_node = head_node[k];
            cout << k;
            while (display_node != NULL){
                cout << " —> " << display_node->value << "(" << display_node->weight << ")";
                display_node = display_node->next;
            }
            cout << endl;
        }
    }

};

int main(){
    //creating graph
    int a,b,N,M;
    scanf("%d %d", &N, &M);

    vector<graphEdge> graphEdges;
    int number_of_nodes = N;
    int num_edges = 0;
    Graph graph(graphEdges, num_edges, number_of_nodes);
    graph.Display();

    //input
    for(int i = 0; i < M; i++){
        scanf("%d %d", &a, &b);
        graphEdge new_edge = {a-1,b-1};
        graph.AddEdge(new_edge);
    }
    
    graph.Display();

    return 0;
}