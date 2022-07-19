class Queue():

    def __init__(self):
        self.data = []

    def add(self, data):
        self.data.append(data)

    def pop(self):
        item = self.data[0]
        self.data = self.data[1:]
        return item
    
    def summary(self):
        for i in self.data: print("car {}".format(i.id))

class Graph():

    def __init__(self):
        self.graph = {}
        self.edges = {}
        self.nodes = {}
        pass
    
    def add_node(self, id):
        new_node = Node(id)
        self.nodes[id] = new_node

    def add_edge(self, id, source_id, target_id, weight=0):
        if source_id not in self.nodes.keys():
            source_node = Node(source_id)
            self.nodes[source_id] = source_node
        else:
            source_node = self.nodes[source_id]
        if target_id not in self.nodes.keys():
            target_node = Node(target_id)
            self.nodes[target_id] = target_node
        else:
            target_node = self.nodes[target_id]

        edge = Edge(id, source_node, target_node, weight)
        source_node.exit_edges[edge.id] = edge
        target_node.in_edges[edge.id] = edge
        self.edges[id] = edge
        self.graph[source_node] = {target_node: edge}

    def summary(self):
        for source, value in self.graph.items():
            for target, val in value.items():
                print("From node {} to node {} edge {} weight {}".format(source.id, target.id, val.id, val.weight))
        for node in self.nodes.values():
            print("node {} cars {}".format(node.id, node.in_cars.summary()))

class City_Plan(Graph):

    def __init__(self):
        super().__init__()

class Node():

    def __init__(self, id):
        self.id = id
        self.in_cars = Queue()
        self.in_edges = {}
        self.exit_edges = {}
        pass

    def add_car(self, car):
        self.in_cars.add(car)

    def leave_car(self, edge):
        car = self.in_cars.pop()
        edge.cars.add(car)
        return car

    def summary(self):
        print("in cars:")
        self.in_cars.summary()
            

class Edge():

    def __init__(self, id, source_node, target_node, weight):
        self.id = id
        self.source = source_node
        self.target = target_node
        self.weight = weight
        self.cars = Queue()
        pass

class Car():

    def __init__(self, id):
        self.id = id
        pass

class Traffic_Light():

    def __init__(self):
        pass
