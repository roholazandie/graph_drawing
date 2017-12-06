from plotly_visualize import visualize_graph_3d
import networkx as nx

def get_edge_weights(G):
    weights = [G[u][v]['weight'] for u, v in G.edges()]
    return weights


def get_node_sizes(G):
    node_sizes = nx.get_node_attributes(G, 'importance').values()
    return node_sizes


def get_node_labels(G):
    return G.nodes()



graph = nx.read_gpickle("graph.gpickle")
node_sizes = get_node_sizes(graph)
edge_weights = get_edge_weights(graph)
node_labels = get_node_labels(graph)
layout = "graphviz"
filename= "outputs/"+layout+"3d.html"
visualize_graph_3d(graph, node_labels, node_sizes, filename=filename, title="3D visualization")
