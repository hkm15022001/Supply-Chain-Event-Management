class PackagePropertyTable: 

    def __init__(self, size):
        self.table = []
        self.keys = []
        for i in range(size):
            self.table.append([])

    def create(self, key, value):
        bucket = hash(key) % len(self.table)
        self.table[bucket].append(value)
        self.keys.append(key)

    def read(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        if len(bucket_list) > 0:
            return bucket_list
        else:
            print("No packages found for address, do nothing.")
            return []

    def delete(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        if bucket in bucket_list:
            bucket_list.remove(bucket)

class Location:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.predecessor = None

    def __str__(self):
        return str(self.label)



def dijkstra_shortest_path(graph, start_location):
    unvisited_queue = []
    for v in graph.adjacency_list:
        unvisited_queue.append(v)

    start_location.distance = 0

    while len(unvisited_queue) > 0:
        smallest = 0

        for e in range(1, len(unvisited_queue)):
            if unvisited_queue[e].distance < unvisited_queue[smallest].distance:
                smallest = e

        current_location = unvisited_queue.pop(smallest)

       
        for adj_vertex in graph.adjacency_list[current_location]:

            edge_weight = graph.edge_weights[(current_location, adj_vertex)]
            alternative_path_distance = current_location.distance + edge_weight
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.predecessor = current_location



def get_shortest_path(start_location, end_location):
    path = ''
    current_location = end_location
    while current_location is not start_location:
        if current_location is None:
            break
        path = " -> " + str(current_location.label) + path
        current_location = current_location.predecessor
    path = start_location.label + path
    return path


from PackagePropertyTable import PackagePropertyTable

class Hub:
    def __init__(self, capacity=40):
        self.package_list = [None] * capacity
        self.start_time = 8
        self.drivers = ['Bill', 'Ted']
        self.finish_time = 0
        self.count = 0
        self.total_distance = 0
        self.packages_delivered = 0
        self.wrong_address = []

    def get_packages_by_weight(self, packages):
        packages_by_weight = PackagePropertyTable(40)
        for package in packages:
            if package is not None:
                packages_by_weight.create(package.delivery_weight, package)
        return packages_by_weight

    def get_packages_by_zip(self, packages):
        packages_by_zip = PackagePropertyTable(40)
        for package in packages:
            if package is not None:
                packages_by_zip.create(package.delivery_zip, package)
        return packages_by_zip

    def get_packages_by_city(self, packages):
        packages_by_city = PackagePropertyTable(40)
        for package in packages:
            if package is not None:
                packages_by_city.create(package.delivery_city, package)
        return packages_by_city

    def get_packages_by_id(self, packages):
        packages_by_id = PackagePropertyTable(40)
        for package in packages:
            if package is not None:
                packages_by_id.create(package.package_id, package)
        return packages_by_id

    def get_packages_by_status(self, packages):
        packages_by_status = PackagePropertyTable(40)
        for package in packages:
            if package is not None:
                packages_by_status.create(package.delivery_status, package)
        return packages_by_status

    def get_packages_by_address(self, packages):
        packages_by_address = PackagePropertyTable(40)
        for package in packages:
            if package is not None:
                packages_by_address.create(package.delivery_address, package)
        return packages_by_address

    def get_packages_by_deadline(self, packages):
        packages_by_deadline = PackagePropertyTable(40)
        for package in packages:
            if package is not None:
                packages_by_deadline.create(package.delivery_deadline, package)
        return packages_by_deadline

    def get_packages_by_arrival(self, packages):
        packages_by_arrival = PackagePropertyTable(40)
        for package in packages:
            if package is not None:
                packages_by_arrival.create(package.arrival_time, package)
        return packages_by_arrival


# %%
from Location import Location

class DistanceGraph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}
        self.hub_vertex = Location(None)

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def remove_directed_edge(self, from_vertex, to_vertex):
        self.edge_weights.pop([from_vertex, to_vertex])
        self.adjacency_list[from_vertex].pop(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    def remove_undirected_edge(self, vertex_a, vertex_b):
        self.remove_directed_edge(vertex_a, vertex_b)
        self.remove_directed_edge(vertex_b, vertex_a)


# %%
import datetime

def get_formatted_time(time):
    hh = int(time)
    mm = (time * 60) % 6
    ss = (time * 3600) % 60
    return "%d:%02d:%02d" % (hh, mm, ss)

def get_hours_float(time):
    times = []

    for x in time.split(':'):
        times.append(int(x))

    time = datetime.time(times[0], times[1], times[2])
    return float(time.hour + time.minute / 60 + time.second / 3600)


# %%
from PackagePropertyTable import PackagePropertyTable

class Truck:

    def __init__(self, truck_id, driver=""):
        self.MAX_LOAD = 16
        self.AVG_MPH = 18
        self.driver = driver
        self.delivery_queue = []
        self.priority_delivery_queue = []
        self.truck_id = truck_id
        self.packages_delivered = 0
        self.package_count = 0
        self.distance = 0
        self.time = 0
        self.path = []
        self.current_location = None
        self.start_time = 0

    def __str__(self):
        return ('Truck ID: ' + self.truck_id.__str__()
                + '\nStart Time: ' + self.start_time.__str__()
                + '\nDistance: ' + self.distance.__str__()
                + '\nPackage Count: ' + self.package_count.__str__()
                + '\nFinish Time: ' + self.finish_time.__str__()
                + '\nMAX_LOAD: ' + self.MAX_LOAD.__str__()
                + '\nAVG_MPH: ' + self.AVG_MPH.__str__()
                + '\nDriver: ' + self.driver.__str__()
                + '\n\n'
                )

    def load_on_truck(self, package):
        if self.package_count < 16:
            package.delivery_status = 'loaded'
            package.truck_id = self.truck_id
            if package.priority:
                self.priority_delivery_queue.append(package)
                print('    result:', package.package_id, 'PRIORITY - loaded on truck', self.truck_id)
            elif package.is_special == True:
                self.delivery_queue.append(package)
                print('    result:', package.package_id, 'SPECIAL - loaded on truck', self.truck_id)
            else:
                print('    result:', package.package_id, 'loaded on truck', self.truck_id)
                self.delivery_queue.append(package)
            self.package_count += 1
            return True
        else:
            print('Package: ', package.package_id, 'unable to load package. Truck: ', self.truck_id, 'is full.')
            return False


def dijkstra_shortest_path(graph, start_location):
    unvisited_queue = []
    for v in graph.adjacency_list:
        unvisited_queue.append(v)

    start_location.distance = 0

    while len(unvisited_queue) > 0:
        smallest = 0

        for e in range(1, len(unvisited_queue)):
            if unvisited_queue[e].distance < unvisited_queue[smallest].distance:
                smallest = e

        current_location = unvisited_queue.pop(smallest)

        for adj_vertex in graph.adjacency_list[current_location]:
            int("adj_vertex.predecessor: ", adj_vertex.predecessor)

            edge_weight = graph.edge_weights[(current_location, adj_vertex)]
            alternative_path_distance = current_location.distance + edge_weight
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.predecessor = current_location



def get_shortest_path(start_location, end_location):
    path = ''
    current_location = end_location
    while current_location is not start_location:
        if current_location is None:
            break
        path = " -> " + str(current_location.label) + path
        current_location = current_location.predecessor
    path = start_location.label + path
    return path


# %%
import csv
from pathlib import Path
from Hub import Hub
from Package import Package
from DistanceGraph import DistanceGraph
from PackagePropertyTable import PackagePropertyTable
from Location import Location

hub = Hub()

with open(Path(__file__).parent/'Data/updated_package.csv', mode='r',encoding='utf-8') as packages:
    package_list = hub.package_list
    package_reader = csv.reader(packages, delimiter=',')
    count = 0
    for row in package_reader:
        if count > 0:
            package_id = int(row[0])
            package = Package(package_id=row[0], package_weight=row[2], special_note=row[3],
                                    delivery_address=row[1])
            package_list[package_id - 1] = package
        count += 1

with open(Path(__file__).parent/'Data/distance_matrix1.csv', mode='r',encoding='utf-8') as distances:
    distance_graph = DistanceGraph()
    distance_reader = csv.reader(distances, delimiter=',')
    count = 0
    locations = []

    for row in distance_reader:
        if count > 0:
            address = str(row[0])
            # address = str(row[1])[1:-8]
            location = Location(address)

            if location.label == "Hà Nội":
                location.label = 'hub'
                distance_graph.hub_vertex = location
            distance_graph.add_vertex(location)
            for package in package_list:
                if package.delivery_address == location.label:
                    package.location = location 

            for path in range(3, len(row)):
                if row[path] == '0.0':
                    break
                else:
                    v = list(distance_graph.adjacency_list.keys())[path - 3]
                   
                    distance_graph.add_undirected_edge(location
                                                       , list(distance_graph.adjacency_list.keys())[path - 3]
                                                       , float(row[path]))

        count += 1

def load_packages():
    return package_list


def load_distances():
    return distance_graph



import copy
import LoadData
import Time
import ShortestPath

from Hub import Hub
from Truck import Truck
from Package import Package
from Location import Location



# Total runtime complexity = O(N) + O(N^3) + O(N^3) + O(N^3) = O(N^3)
def process_optimize():
    packages = LoadData.load_packages()
    distance_graph = LoadData.load_distances()

    hub = Hub()
    print("<------------Processing and loading special packages on trucks---------------->")
    trucks = [Truck(1, hub.drivers[0]), Truck(2, hub.drivers[1]), Truck(3)]
    packages_by_id = hub.get_packages_by_id(packages)
    unloaded_packages = []

    # Run-time complexity: O(N) * O(1) = O(N)
    for package in packages:
        print("Package: ", package.package_id, "and special note: ", package.special_note)
       
        if package.delivery_status == 'loaded':
           print("    result: ", package.package_id, "Has already been loaded.  Nothing to do.") 
        else:
            print("    result: ", package.package_id, "Not special, will be loaded after special packages are processed/loaded.")
            unloaded_packages.append(package)
    print("<------------Special packages loaded---------------->\n")
    
    # load all remainder of packages on trucks optimized for distance
    print("<------------Load packages---------------->")
    packages_by_address = hub.get_packages_by_address(unloaded_packages)
    loaded_packages = []
    # O(N) * (O(1) + O(N^2) + O(N) + O(1)) = O(N^3)
    while len(unloaded_packages) > 0:
        for truck in trucks:
            if len(unloaded_packages) == 0:
                break
            # if it's the trucks first iteration
            if truck.current_location == None:
                # set the trucks starting location
                truck.current_location = distance_graph.hub_vertex
            for v in distance_graph.adjacency_list:
                v.distance = float('inf')
                v.predecessor = None
            ShortestPath.dijkstra_shortest_path(distance_graph, truck.current_location)
            # find the location with the next closest distance
            closest_distance = float('inf')
            smallest = None
            # Run-time complexity: O(N)
            # print(len(unloaded_packages))
            for i in range(0, len(unloaded_packages)):
                if unloaded_packages[i].location.distance == float('inf'):
                    print("Package that inf",unloaded_packages[i])
                    
                if unloaded_packages[i].location.distance < closest_distance:
                    smallest = i
                    closest_distance = unloaded_packages[i].location.distance
            
            packages_at_stop = packages_by_address.read(unloaded_packages[smallest].location.label)
            if len(packages_at_stop) < (16 - truck.package_count):
                starting_location = truck.current_location
                truck.current_location = unloaded_packages[smallest].location
                
                # load all packages at this address
                # run-time complexity O(1)
                for package in packages_at_stop:
                    print("Package: ", package.package_id, package.location.label)
                    if package.location.label == truck.current_location.label and truck.load_on_truck(package) and package not in loaded_packages:
                        loaded_packages.append(package)
                        unloaded_packages.remove(package)
            else:
                continue
    print("<------------All packages loaded---------------->\n")


if __name__ == "__main__":
    process_optimize()




# %%
