#include <bits/stdc++.h>
#include <string>

#define INF 1000000001
using namespace std;

struct Node
{
    int value, weight;
    Node* next;
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


/*
THIS FUNCTIONS COMPUTES THE BEST VALUE FOR A COMPAGNY TO MAKE 2 PROJECTS.
ASSUME THAT V IS A LIST WHERE V[i] is the value for project i; THIS FUNCTION
COMPUTES THE BEST VALUE TO MAKE DEPENDING DEPENDENCIES DESCRIBED IN A AND B.
B IS THE LIST OF PROJECTS THAT HAVE A REQUIREMENT
A[i] is the project required for B[i]
*/
int solution(vector<int> &V, vector<int> &A, vector<int> &B) {
    int num_projects = V.size();
    Graph graph(num_projects);
    
    for(int i = 0; i < num_projects; i++){
        for(int j = 0; j < num_projects; j++){
            graphEdge new_edge = {i,j,V[i]};
            graph.AddEdge(new_edge);
        }
    }

    int num_constraint = B.size();

    for(int i=0; i<num_constraint; i++){
        for(int j=0; j<num_projects; j++){
            Node *node = graph.head_node[j];
            while (node != NULL){
                if (node->value == B[i] && j != A[i]){
                    node->weight = -INF;
                }
                node = node->next;   
            }
        } 
    }
    
    graph.Display();
    int gain = 0;
    for(int i=0; i<num_projects; i++){
        Node* first = graph.head_node[i];
        int val1 = 0;
        while(first != NULL){
            val1 = first->weight;
            Node* second = graph.head_node[first->value];
            int val2 = 0;
            while(second != NULL){
                val2 = second->weight;
                if (i != first->value){

                    //flag computation
                    int flag = 0;
                    for(int a=0; a<B.size(); a++){
                        if (i==B[a]){
                            flag=1;
                        }
                    }
                    //flag tracks if the first project is a project that needs a dependance
                    if (val1+val2 > gain and flag == 0){
                        gain = val1+val2;
                    }
                    //case where 1 project is enough;
                    if (val1 > gain and flag == 0){
                        gain = val1
                    }
                }
                second = second->next;
            }
            first = first->next;
        }
    }
    cout << "SOLUTION IS " << gain << endl;
    return gain;
}


int main(){
    int arr[] = {1,1,5};
    std::vector<int> V(arr, arr + sizeof(arr) / sizeof(arr[0]));

    int arr2[] = {0,1};
    std::vector<int> A(arr2, arr2 + sizeof(arr2) / sizeof(arr2[0]));

    int arr3[] = {2,2};
    std::vector<int> B(arr3, arr3 + sizeof(arr3) / sizeof(arr3[0]));

    solution(V,A,B);
    return 0;
}
