import numpy as np
class Mob:
    city = None
    has_car = False
    time = None
    def __init__(self,city):
        self.city = city
        self.time = 0
    def __eq__(self, other):
        if not isinstance(other, Mob):
            return NotImplemented
        return self.city == other.city and self.has_car == other.has_car

class Test:
    cities_quantity = None
    roads_quantity = None
    connections = None
    distances = None
    mobs_quantity = None
    mobs_cities = None
    cars_quantity = None
    cars_cities = None
    start = None
    goal = None

    def __init__(self,cities_quantity,roads_quantity):
        self.cities_quantity = cities_quantity
        self.roads_quantity = roads_quantity
        self.connections = [None for x in range(self.cities_quantity)]
        #self.connections = np.nan([self.cities_quantity])
        self.distances = [[None for x in range(self.cities_quantity)] for y in range (self.cities_quantity)]
        #self.distances = np.nan([self.cities_quantity , self.cities_quantity])
        self.mobs_cities = []
        self.cars_cities = []

    def set_connection(self,city_1,city_2,distance):
        if (self.connections[city_1-1] == None):
            self.connections[city_1-1] = [city_2]
        else :
            self.connections[city_1 - 1].append(city_2)

        if (self.connections[city_2-1] == None):
            self.connections[city_2-1] = [city_1]
        else :
            self.connections[city_2 - 1].append(city_1)


        (self.distances[city_1-1])[city_2-1] = distance
        (self.distances[city_2-1])[city_1-1] = distance

    def set_mobs(self,quantity,cities):
        self.mobs_quantity = quantity
        for city in cities:
            self.mobs_cities.append(int(city))

    def set_cars(self,quantity,cities):
        self.cars_quantity = quantity
        for city in cities:
            self.cars_cities.append(int(city))

    def set_start_and_goal(self,start,goal):
        self.start = start
        self.goal = goal

    def print_distances(self):
        dist = self.distances
        for i in range(len(dist)):
            print(dist[i])

K = int(input())
tests = []
for index in range (K):
    N, M = input().split()
    N, M = int(N), int(M)
    test = Test(N,M)

    for road_index in range(M):
        u, v, d = input().split()
        u, v, d = int(u), int(v), int(d)
        test.set_connection(u,v,d)

    T = input()
    T = int(T)
    citites = input().split()
    test.set_mobs(T,citites)

    C = input()
    C = int(C)
    citites = input().split()
    test.set_cars(C,citites)

    s, g = input().split()
    s, g = int(s), int(g)
    test.set_start_and_goal(s,g)
    test.print_distances()
    tests.append(test)

