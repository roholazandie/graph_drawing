# Graph Drawing using Plotly+Graphviz
This project shows a usecase of using graphviz layout on plotly network plot.
You can read more about this repository [this](https://medium.com/@hilbert.cantor/network-plot-with-plotly-and-graphviz-ebd7778073b) medium post.


# Installation
First of all you need to install the graphviz package(for ubuntu):

`> sudo apt-get install graphviz libgraphviz-dev pkg-config`

And then install the requirements.txt file:

`> pip install -r requirements.txt`

the only requirements are plotly and networkx and pygraphviz.

# Motivation
The motivation of writing this script is to provide a more easier and appealing network plots
using beautiful plotly plots and graphviz layout.

# Usage
After installation of requirements then you can take a look at the main script. There are couple of ways to call the visualize_graph method.
In the simplest format you just need to pass the graph (in networkx format).

`visualize_graph(G)`

in full format you can specify node labels, node sizes, edge weights, layout, file_name and title of the
plot. Here is one call:

`visualize_graph(G, node_labels, node_sizes, edge_weights, layout, filename="outputs/test.html", title="My title")`

You should be careful about the order of the parameters list. Just use networkx call to edges and nodes lists.

You can also use the 3d version of the graph visualization which is based on spring layout.
for 3d usage you can do like this:
`visualize_graph_3d(graph, node_labels, node_sizes, filename="outputs/test.html")`
