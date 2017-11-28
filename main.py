'''
In this script we try to compare the result of graph drawing
with different layouts with plotly visualization library
Here we use a predefined graph saved as pickle format
you can use any other graph as input to the function
'''

import networkx as nx
from plotly_visualize import visualize_graph

def get_node_weights(G):
    weights = [G[u][v]['weight'] for u, v in G.edges()]
    return weights


def get_node_sizes(G):
    node_sizes = nx.get_node_attributes(G, 'importance').values()
    return node_sizes


if __name__ == "__main__":
    graph = nx.read_gpickle("graph.gpickle")
    node_sizes = get_node_sizes(graph)
    node_weights = get_node_weights(graph)
    visualize_graph(graph, node_sizes, node_weights, layout="graphviz", filename="spring.html", title="")

