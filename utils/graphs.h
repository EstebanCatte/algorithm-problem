#ifndef graphs
#define graphs

#include <bits/stdc++.h>
using namespace std;

#define INF 2147483647
#define MAX_NODE 99


struct Node
{
    //value is the name or the id of the node
    //weigth is a cost to stay on the node
    int value, weight;
    Node* next;

    void print(){
        if (this == NULL){
            cout << "Node is NULL" << endl;
            return;
        }
        if (this->next != NULL){
            cout << "Node value: " << this->value << " | weight: " << this->weight << " | next node is :" << next->value << endl;
        }else{
            cout << "Node value: " << this->value << " | weight: " << this->weight << " | next node is : NULL" << endl;
        }
        
    }
};

struct graphEdge {
    //weight is a cost going from source to destination
    int source, destination, weight;
};


class Graph {

    //Adjancy list data struct
    //meaning that multiple object may be created for the same node, edges are unique
    vector<vector<int> > matrix;

    // Create a new node for the adjacency list
    Node* CreateNode(int destination, Node* head_node){
        Node* new_node = new Node;
        new_node->value = destination;
        new_node->next = head_node;
        new_node->weight = 0;
        return new_node;
    }

    public:
        //Add a new edge to the graph depending edge object. 
        //If the connection already exist, it just changes the weight.
        void AddEdge(graphEdge edge)
        {
            int source = edge.source;
            int destination = edge.destination;
            if (GetEdge(edge) == NULL){
                Node* new_node = CreateNode(destination, head_node[source]);
                new_node->weight = edge.weight;
                head_node[source] = new_node;
                this->edge_list.push_back(edge);
            }
            else{
                Node* existing_node = GetEdge(edge);
                existing_node->weight = edge.weight;
            }
        }


        int number_of_nodes;
        vector<graphEdge> edge_list;
        Node **head_node;

        //constructor
        Graph(int num_of_node){
            this->number_of_nodes = num_of_node;
            vector<graphEdge> graphEdges;
            this->edge_list = graphEdges;
            // dynamic memory allocation
            head_node = new Node*[num_of_node]();

            // initialize headnode for every edge of graph
            for (int k = 0; k < num_of_node; k++) {
                head_node[k] = NULL;
            }
        }


        //destructor
        ~Graph() {
            for (int k = 0; k < number_of_nodes; k++) {
                delete[] head_node[k];
            }
            delete[] head_node;
        }


    void init_edges(vector<graphEdge> graphEdges)
    {
        if(sizeof(graphEdges) > 0){
            for (int k = 0; k < sizeof(graphEdges); k++){
                this->AddEdge(this->edge_list[k]);
            }
        }
    }
    

    int GetNumEdges()
    {
        return this->edge_list.size();
    }


    //Return destination node object for a given edge object
    //No need to have the origin due to the adjency list data struct (stored in first places)
    Node* GetEdge(graphEdge edge)
    {
        int source = edge.source;
        int destination = edge.destination;
        Node *node = head_node[source];
        while (node != NULL){
            if (node->value == destination){
                return node;
            }
            node = node->next;   
        }
        return NULL;
    }


    //Set Weight between two nodes
    void SetEdgeWeight(graphEdge edge, int weight)
    {
        Node *node = GetEdge(edge);
        node->weight = weight;
    }


    // Function to convert adjacency list to adjacency matrix
    vector<vector<int> > ConvertToMatrix(int fill_with = INF)
    {   
        int V = this->number_of_nodes;
        vector<vector<int> > matrix(V, vector<int>(V, fill_with));
    
        for (int i = 0; i < V; i++) {
            Node *node = head_node[i];
            while (node != NULL){
                matrix[i][node->value] = node->weight;
                if (node->next != NULL) 
                {
                    node = node->next; 
                }else{
                    break;
                }
            }
        }
        this->matrix = matrix;
        return matrix;
    }


    // Function to display adjacency matrix
    void PrintMatrix(vector<vector<int> > matrix)
    {
        int V = this->number_of_nodes;
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (matrix[i][j] == INF)
                {
                    cout << "INF" << "   ";
                    continue;
                }
                cout << matrix[i][j] << "   ";
            }
            cout << endl;
        }
        cout << endl;
    }

    void Display()
    {
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

#endif