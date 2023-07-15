#include <iostream>
using namespace std;
#include <typeinfo>

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
        Graph(graphEdge graphEdges[], int num, int number_of_nodes){
            this->number_of_nodes = number_of_nodes;
            this->number_of_edges = num;
            // dynamic memory allocation
            head_node = new Node*[number_of_nodes]();

            // initialize headnode for every edge of graph
            for (int k = 0; k < number_of_nodes; k++) {
                head_node[k] = NULL;
            }

            for (int k = 0; k < num; k++){
                int source = graphEdges[k].source;
                int destination = graphEdges[k].destination;

                Node* new_node = getNeighbourVertex(destination, head_node[source]);
                head_node[source] = new_node;
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
    graphEdge graphEdges[] = {{0, 1}, {1, 2}, {2, 0}, {2, 1}, {3, 2}, {4, 1}, {3, 4}};

    int number_of_nodes = 5;
    int num_edges = sizeof(graphEdges)/sizeof(graphEdges[0]);

    // create the graph
    Graph graph(graphEdges, num_edges, number_of_nodes);

    graph.Display();

    graphEdge new_edge = {4,0};
    graph.AddEdge(new_edge);
    graph.SetEdgeWeight(new_edge, 12);
    graph.Display();

    return 0;
}