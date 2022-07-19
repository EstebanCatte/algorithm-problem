from objects import City_Plan
from objects import Car


def test():
    num_cars = 3

    city1 = City_Plan()
    city1.add_edge(0, 0, 1, 10)
    city1.add_edge(1, 1, 0, 5)
    city1.summary()

    cars = []
    for i in range(0, num_cars):
        cars.append(Car(id=i))

    city1.nodes[0].add_car(cars[1])
    city1.nodes[0].add_car(cars[0])
    city1.nodes[0].summary()


f = open("C:/Users/Esteban/Desktop/Github/algorithm-problem/google hash/2021-traffic_lights/a.txt", "r")
time, num_intersection, num_street, num_cars, score = map(int, f.readline().split())
city = City_Plan()
for street in range(int(num_street)):
    source_node, target_node, id, lenght = f.readline().split()
    city.add_edge(id, source_node, target_node, lenght)

for car_id in range(int(num_cars)):
    data = list(f.readline().split())
    path_length, start_node, path = data[0], data[1], data[2:]
    city.nodes[start_node].add_car(Car(id=car_id))
city.summary()

    