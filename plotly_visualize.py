from plotly.graph_objs import *
from plotly.offline import plot as offpy
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout




def reformat_graph_layout(G, layout):
    '''
    this method provide positions and reformatted graph to be used by
    plotly. node_labels also different in graphviz and other formats
    :param G:
    :param layout:
    :return:
    '''
    if layout == "graphviz":
        keys = G.nodes()
        values = range(len(G.nodes()))
        dictionary = dict(zip(keys, values))
        node_labels = {v: k for k, v in dictionary.items()}
        G = nx.relabel_nodes(G, dictionary)
        positions = graphviz_layout(G)
    elif layout == "spring":
        positions = nx.fruchterman_reingold_layout(G, k=0.5, iterations=1000)
        keys = G.nodes()
        node_labels = dict(zip(keys, keys))
    elif layout == "spectral":
        positions = nx.spectral_layout(G, scale=0.5)
        keys = G.nodes()
        node_labels = dict(zip(keys, keys))
    elif layout=="random":
        positions = nx.random_layout(G)
        keys = G.nodes()
        node_labels = dict(zip(keys, keys))
    else:
        raise Exception("please specify the layout from graphviz, spring, spectral or random")

    return G, positions, node_labels


def visualize_graph(G, node_sizes, node_weights, layout="graphviz", filename ="netwrokx", title=""):
    G, positions, node_labels = reformat_graph_layout(G, layout)

    edge_trace = Scatter(
        x=[],
        y=[],
        line=Line(width=[], color='rgba(136, 136, 136, .8)'),
        hoverinfo='none',
        mode='lines')

    for edge in G.edges():
        x0, y0 = positions[edge[0]]
        x1, y1 = positions[edge[1]]
        edge_trace['x'] += [x0, x1, None]
        edge_trace['y'] += [y0, y1, None]

    for weight in node_weights:
        edge_trace['line']['width'].append(weight)

    node_trace = Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers+text',
        textfont=dict(family='Calibri (Body)', size=25, color='black'),
        opacity=100,
        # hoverinfo='text',
        marker=Marker(
            showscale=True,
            # colorscale options
            # 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' |
            # Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
            colorscale='Jet',
            reversescale=True,
            color=[],
            size=[],
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line=dict(width=2)))

    for node in G.nodes():
        x, y = positions[node]
        node_trace['x'].append(x)
        node_trace['y'].append(y)

    for adjacencies in G.adjacency_list():
        node_trace['marker']['color'].append(len(adjacencies))

    for node in G.nodes():
        node_trace['text'].append(node_labels[node])

    for size in node_sizes:
        node_trace['marker']['size'].append(size)

    fig = Figure(data=Data([edge_trace, node_trace]),
                 layout=Layout(
                     title='<br>' + title,
                     titlefont=dict(size=16),
                     showlegend=False,
                     width=1500,
                     height=800,
                     hovermode='closest',
                     margin=dict(b=20, l=350, r=5, t=200),
                     # family='Courier New, monospace', size=18, color='#7f7f7f',
                     annotations=[dict(
                         text="",
                         showarrow=False,
                         xref="paper", yref="paper",
                         x=0.005, y=-0.002)],
                     xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                     yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))

    offpy(fig, filename=filename, auto_open=True, show_link=False)


