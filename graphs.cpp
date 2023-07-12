#include <iostream>
#include <vector>
#include <list>
#include <string>
using namespace std;

class Edge
{
    public:
    int weight;
    int id;
    
    //constructor
    Edge(int w){
        string s="Null";
        Vertex Destination(0,s);
        Vertex Source(0,s);
        weight = w;
    }

    void setWeight(int w) {
        weight = w;
    }

    int getWeight(){
        return weight;
    }

    //int getDestinationID(){
    //    return DestinationID;
    //}

    //int setDestinationID(int destinationid){
    //    DestinationID = destinationid;
    //}

    //int getSourceID(){
    //    return SourceID;
    //}

    //int setSourceID(int sourceid){
    //    SourceID = sourceid;
    //}
};

class Vertex
{
    public:
    int id;
    string name;
    list<Edge> edgelist;

    Vertex(int vertexId, string vertexName){
        name = vertexName;
        id = vertexId;
    }

    int getID(){
        return id;
    }

    void setID(int vertexId){
        id = vertexId;
    }
};

class Graph {
    public:
    int id;
    int numVertices;
    int numEdges;
    vector<Vertex> vertices;
    vector<Edge> edges;

    Graph(int i=0) {
        id = i;
        numVertices=0;
        numEdges=0;
    }

    void add_vertex(string name)
    {
        Vertex vert(numVertices, name);
        vertices.push_back(vert);
        numVertices += 1;
    }

    void add_vertices(const vector<string> &names){
        for(int i=0; i<names.size(); i++){
            add_vertex(names[i]);
        }
    }

    void add_edge(Vertex v1, Vertex v2){
        Edge edge(1);
        edges.push_back(edge);
        numEdges += 1;
    }

    void showVertices()
    {
        for(int i=0; i<numVertices; i++){
            cout << "Vertice " << i << " id : " << vertices[i].id << " name : "<< vertices[i].name << endl;
        }
    }

    //void showEdges()
    //{
    //    for(int i=0; i<numEdges; i++){
    //        cout << "Edge " << i << " id : " << edges[i].id << " weigth : "<< edges[i].weight << " from : " << edges[i].SourceID.id << " to: " << edges[i].DestinationID.id << endl;
    //    }
    //}
};

int main()
{
    Graph g;
    const char *names[] = {"Paris", "Londres"};
    vector<string> n(names, names+2);
    
    g.add_vertices(n);
    g.add_edge(g.vertices[0], g.vertices[1]);
    g.showVertices();
    //g.showEdges();
    return 0;

}