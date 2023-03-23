import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import warnings
import scipy as sp

from networkx import number_of_nodes, adjacency_matrix
from networkx.algorithms import community

warnings.simplefilter('ignore')


# plot a network
def plotNetwork(network, communities = [1, 1, 1, 1, 1, 1]):
    np.random.seed(123) #to freeze the graph's view (networks uses a random view)
    A = np.matrix(network["mat"])
    G = nx.from_numpy_matrix(A)
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(4, 4))  # image is 8 x 8 inches
    nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu, node_color=communities)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.show()


def read_graph_from_gml(file_path):
    try:
        with open(file_path) as f:
            data = f.read()
            graph = nx.parse_gml(data, label='id')
            return graph
    except IOError:
        print(f"Could not read file a:{file_path}.")
        return None


def dictionary_from_graph(graph):
    net={}
    net["noNodes"] = nx.number_of_nodes(graph)
    matrix = nx.to_numpy_array(graph)
    net["mat"]= matrix
    return net


# identify the communities (by a tool) and plot them
def greedyCommunitiesDetectionByTool(network):
    # Input: a graph
    # Output: list of comunity index (for every node)

    from networkx.algorithms import community

    A = np.matrix(network["mat"])
    G = nx.from_numpy_matrix(A)
    communities_generator = community.girvan_newman(G)
    top_level_communities = next(communities_generator)
    sorted(map(sorted, top_level_communities))
    communities = [0 for node in range(network['noNodes'])]
    index = 1
    for community in sorted(map(sorted, top_level_communities)):
        for node in community:
            communities[node] = index
        index += 1
    return communities

# load a network
crtDir =os.getcwd()

#dolphins
filePath = os.path.join(crtDir,  'data/real/dolphins', 'dolphins.gml')
network = read_graph_from_gml(filePath)
net1 = dictionary_from_graph(network)
assert(net1["noNodes"]==62)
plotNetwork(net1, greedyCommunitiesDetectionByTool(net1))

#football
filePath = os.path.join(crtDir,  'data/real/football', 'football.gml')
network = read_graph_from_gml(filePath)
net2 = dictionary_from_graph(network)
assert(net2["noNodes"]==115)
plotNetwork(net2, greedyCommunitiesDetectionByTool(net2))

#karate
filePath = os.path.join(crtDir,  'data/real/karate', 'karate.gml')
network = read_graph_from_gml(filePath)
net3 = dictionary_from_graph(network)
assert(net3["noNodes"]==34)
plotNetwork(net3, greedyCommunitiesDetectionByTool(net3))

#krebs
filePath = os.path.join(crtDir,  'data/real/karate', 'karate.gml')
network = read_graph_from_gml(filePath)
net4 = dictionary_from_graph(network)
assert(net4["noNodes"]==34)
plotNetwork(net4, greedyCommunitiesDetectionByTool(net4))

#random examples
example1 = nx.gnm_random_graph(23, 100)
net5=dictionary_from_graph(example1)
assert (net5["noNodes"] == 23)
plotNetwork(net5, greedyCommunitiesDetectionByTool(net5))

example2 = nx.gnm_random_graph(43, 120)
net6=dictionary_from_graph(example2)
assert (net6["noNodes"] == 43)
plotNetwork(net6, greedyCommunitiesDetectionByTool(net6))

example3 = nx.gnm_random_graph(59, 150)
net7=dictionary_from_graph(example3)
assert (net7["noNodes"] == 59)
plotNetwork(net7, greedyCommunitiesDetectionByTool(net7))

example4 = nx.gnm_random_graph(64, 200)
net8=dictionary_from_graph(example4)
assert (net8["noNodes"] == 64)
plotNetwork(net8, greedyCommunitiesDetectionByTool(net8))

example5 = nx.gnm_random_graph(78, 200)
net9=dictionary_from_graph(example5)
assert (net9["noNodes"] == 78)
plotNetwork(net9, greedyCommunitiesDetectionByTool(net9))

#map
filePath = os.path.join(crtDir,  'data/real/map', 'map.gml')
network = read_graph_from_gml(filePath)
net10 = dictionary_from_graph(network)
assert(net10["noNodes"]==4)
plotNetwork(net10, greedyCommunitiesDetectionByTool(net10))