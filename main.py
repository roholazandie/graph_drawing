import argparse
import numpy as np
import networkx as nx
from plotly_visualize import visualize_graph
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser(description="Visualize a graph with different layouts using Plotly.")
    parser.add_argument("--layout", type=str, default="graphviz",
                        choices=["graphviz", "spring", "spectral", "random"],
                        help="Layout algorithm for graph positioning.")
    parser.add_argument("--node_size", type=int, default=20,
                        help="Size of the nodes.")
    parser.add_argument("--output", type=str, default="outputs/graphviz.html",
                        help="Output filename for the visualization.")
    parser.add_argument("--title", type=str, default="Graph Visualization",
                        help="Title for the visualization.")

    args = parser.parse_args()

    # Generate a scale-free graph
    graph = nx.scale_free_graph(100)

    # Generate random edge weights
    edge_weights = np.random.randint(1, 5, len(graph.edges())).tolist()

    # Generate edge colors
    edge_colors = {}
    norm = mcolors.Normalize(vmin=-5, vmax=5)
    cmap = plt.get_cmap('coolwarm')
    for u, v in graph.edges():
        edge_colors[(u, v)] = mcolors.rgb2hex(cmap(norm(np.random.randint(-5, 5))))

    # Visualize the graph
    visualize_graph(
        G=graph,
        layout=args.layout,
        edge_weights=edge_weights,
        edge_colors=edge_colors,
        node_sizes=args.node_size,
        filename=args.output,
        title=args.title
    )


if __name__ == "__main__":
    main()
