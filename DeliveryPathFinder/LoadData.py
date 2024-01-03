import csv
from pathlib import Path
from Hub import Hub
from Package import Package
from DistanceGraph import DistanceGraph
from PackagePropertyTable import PackagePropertyTable
from Location import Location

hub = Hub()

# with open(Path(__file__).parent/'Data/Packages.csv', mode='r') as packages:    
with open(Path(__file__).parent/'Data/updated_package.csv', mode='r') as packages:
    package_list = hub.package_list
    package_reader = csv.reader(packages, delimiter=',')
    count = 0
    for row in package_reader:
        if count > 0:
            package_id = int(row[0])
            package = Package(package_id=row[0], package_weight=row[6], special_note=row[7],
                                    delivery_address=row[1], delivery_city=row[2], delivery_zip=row[4],
                                    delivery_deadline=row[5], delivery_state=row[3])
            package_list[package_id - 1] = package
        count += 1

# with open(Path(__file__).parent/'Data/Distances.csv', mode='r') as distances:
with open(Path(__file__).parent/'Data/distance_matrix.csv', mode='r') as distances:
    distance_graph = DistanceGraph()
    distance_reader = csv.reader(distances, delimiter=',')
    count = 0
    locations = []

    for row in distance_reader:
        if count > 0:
            address = str(row[0])
            # address = str(row[1])[1:-8]
            location = Location(address)

            if location.label == "Hanoi":
                location.label = 'hub'
                distance_graph.hub_vertex = location
            distance_graph.add_vertex(location)
            for package in package_list:
                if package.delivery_address == location.label:
                    package.location = location 

            for path in range(2, len(row)):
                if row[path] == '0.0':
                    break
                else:
                    # print("v.label: ", location.label)
                    v = list(distance_graph.adjacency_list.keys())[path - 2]
                    # print("secondV_label: ", v.label)
                    # print("weight: ", str(float(row[path])))
                    distance_graph.add_undirected_edge(location
                                                       , list(distance_graph.adjacency_list.keys())[path - 2]
                                                       , float(row[path]))

        count += 1
    print("##############################")
    print(count)
    for v in distance_graph.adjacency_list:
        print("v.label: ", v.label)
        print("v.distance: ", v.distance)
        print("v.predecessor: ", v.predecessor)

def load_packages():
    return package_list


def load_distances():
    return distance_graph


def main():
    # Your existing code here...

    loaded_packages = load_packages()
    loaded_distances = load_distances()

    # Display specific attributes of loaded packages
    # for package in loaded_packages:
    #     print(f"Package ID: {package.package_id}")
    #     print(f"Delivery Address: {package.delivery_address}")
    #     print(f"Delivery Location: {package.location}")
    #     # Print other relevant attributes...

    # for vertex, edges in distance_graph.adjacency_list.items():
    #     print(f"Các cạnh kề của đỉnh {vertex.label}:")
    #     for edge in edges:
    #         weight = distance_graph.edge_weights[(vertex, edge)]
    #         print(f"{vertex.label} - {edge.label}, Trọng số: {weight}")
    #     print()

if __name__ == "__main__":
    main()
