from plotly.graph_objs import *
from plotly.offline import plot as offpy
import networkx as nx
from typing import Optional, Union, List, Dict
from networkx.drawing.nx_agraph import graphviz_layout


def reformat_graph_layout(G, layout):
    '''
    this method provide positions based on layout algorithm
    :param G:
    :param layout:
    :return:
    '''
    if layout == "graphviz":
        positions = graphviz_layout(G)
    elif layout == "spring":
        positions = nx.fruchterman_reingold_layout(G, k=0.5, iterations=1000)
    elif layout == "spectral":
        positions = nx.spectral_layout(G, scale=0.1)
    elif layout=="random":
        positions = nx.random_layout(G)
    else:
        raise Exception("please specify the layout from graphviz, spring, spectral or random")

    return positions


import plotly.graph_objects as go


def visualize_graph(
        G: nx.Graph,
        node_labels: Optional[Dict[int, str]] = None,
        node_sizes: Union[int, List[int]] = 10,
        edge_weights: Union[int, List[int]] = 10,
        edge_colors: Union[str, Dict[tuple, str]] = 'black',
        layout: str = "graphviz",
        filename: str = "networkx",
        title: str = ""
) -> None:
    """
    Visualize a NetworkX graph using Plotly.

    Parameters:
        G (nx.Graph): The input graph to visualize.
        node_labels (Optional[Dict[int, str]]): Labels for the nodes. Defaults to None.
        node_sizes (Union[int, List[int]]): Size(s) for the nodes. Defaults to 10.
        edge_weights (Union[int, List[int]]): Width(s) for the edges. Defaults to 10.
        edge_colors (Union[str, Dict[tuple, str]]): Color(s) for the edges. Defaults to 'black'.
        layout (str): Layout algorithm to use for positioning. Defaults to "graphviz".
        filename (str): Output filename for the HTML visualization. Defaults to "networkx".
        title (str): Title for the graph visualization. Defaults to an empty string.
    """
    positions = reformat_graph_layout(G, layout)

    # Ensure edge_weights and node_sizes are lists
    edge_weights = (
        [edge_weights] * len(G.edges())
        if isinstance(edge_weights, int)
        else edge_weights
    )

    node_sizes = (
        [node_sizes] * len(G.nodes())
        if isinstance(node_sizes, int)
        else node_sizes
    )

    # Initialize edge traces
    edge_traces = []
    for edge, edge_weight in zip(G.edges(), edge_weights):
        x0, y0 = positions[edge[0]]
        x1, y1 = positions[edge[1]]

        match edge_colors:
            case str() as color:
                edge_color = color
            case dict() as color_map:
                edge_color = color_map.get(edge, 'black')
            case _:
                edge_color = 'black'

        edge_trace = go.Scatter(
            x=[x0, x1],
            y=[y0, y1],
            line=dict(width=edge_weight, color=edge_color),
            hoverinfo='none',
            mode='lines'
        )
        edge_traces.append(edge_trace)

    # Initialize node trace
    node_x, node_y, node_colors = [], [], []
    for node in G.nodes():
        x, y = positions[node]
        node_x.append(x)
        node_y.append(y)
        node_colors.append(len(list(G.neighbors(node))))  # Color based on degree

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        text=[node_labels.get(node, str(node)) for node in G.nodes()] if node_labels else list(G.nodes()),
        mode='markers+text',
        textfont=dict(family='Calibri (Body)', size=15, color='white'),
        marker=dict(
            size=node_sizes,
            color=node_colors,
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(
                thickness=15,
                title='Node Degree',
                xanchor='left',
                titleside='right'
            )
        )
    )

    # Assemble the figure
    fig = go.Figure(
        data=edge_traces + [node_trace],
        layout=go.Layout(
            title=f'<br>{title}',
            titlefont=dict(size=16),
            showlegend=False,
            width=1500,
            height=800,
            hovermode='closest',
            margin=dict(b=20, l=350, r=5, t=200),
            annotations=[dict(
                text="",
                showarrow=False,
                xref="paper", yref="paper",
                x=0.005, y=-0.002)],
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
        )
    )

    # Render the figure
    fig.write_html(filename, auto_open=True)




def visualize_graph_3d(
    G: nx.Graph,
    node_labels: Optional[Dict[int, str]] = None,
    node_sizes: Union[int, List[int]] = 10,
    edge_weights: Union[int, List[int]] = 2,
    edge_colors: Union[str, Dict[tuple, str]] = 'black',
    layout: str = "fr",
    filename: str = "networkx_3d",
    title: str = "3D Graph Visualization"
) -> None:
    """
    Visualize a 3D NetworkX graph using Plotly.

    Parameters:
        G (nx.Graph): The input graph to visualize.
        node_labels (Optional[Dict[int, str]]): Labels for the nodes. Defaults to None.
        node_sizes (Union[int, List[int]]): Size(s) for the nodes. Defaults to 10.
        edge_weights (Union[int, List[int]]): Width(s) for the edges. Defaults to 2.
        edge_colors (Union[str, Dict[tuple, str]]): Color(s) for the edges. Defaults to 'black'.
        layout (str): Layout algorithm to use for positioning. Defaults to "fr".
        filename (str): Output filename for the HTML visualization. Defaults to "networkx_3d".
        title (str): Title for the graph visualization. Defaults to "3D Graph Visualization".
    """
    # Generate 3D positions for the graph
    positions = nx.fruchterman_reingold_layout(G, dim=3) if layout == "fr" else nx.spring_layout(G, dim=3)

    # Ensure edge_weights and node_sizes are lists
    edge_weights = (
        [edge_weights] * len(G.edges())
        if isinstance(edge_weights, int)
        else edge_weights
    )

    node_sizes = (
        [node_sizes] * len(G.nodes())
        if isinstance(node_sizes, int)
        else node_sizes
    )

    # Create edge traces
    edge_traces = []
    for edge, weight in zip(G.edges(), edge_weights):
        x0, y0, z0 = positions[edge[0]]
        x1, y1, z1 = positions[edge[1]]

        match edge_colors:
            case str() as color:
                edge_color = color
            case dict() as color_map:
                edge_color = color_map.get(edge, 'black')
            case _:
                edge_color = 'black'

        edge_traces.append(go.Scatter3d(
            x=[x0, x1, None],
            y=[y0, y1, None],
            z=[z0, z1, None],
            mode='lines',
            line=dict(width=weight, color=edge_color),
            hoverinfo='none'
        ))

    # Create node traces
    node_x, node_y, node_z, node_colors, node_texts = [], [], [], [], []
    for node in G.nodes():
        x, y, z = positions[node]
        node_x.append(x)
        node_y.append(y)
        node_z.append(z)
        node_colors.append(len(list(G.neighbors(node))))  # Degree-based coloring
        node_texts.append(node_labels.get(node, str(node)) if node_labels else str(node))

    node_trace = go.Scatter3d(
        x=node_x,
        y=node_y,
        z=node_z,
        mode='markers+text',
        marker=dict(
            size=node_sizes,
            color=node_colors,
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(
                title='Node Degree',
                thickness=15,
                xanchor='left',
                titleside='right'
            )
        ),
        text=node_texts,
        hoverinfo='text'
    )

    # Configure layout
    axis_settings = dict(
        showbackground=False,
        showline=False,
        zeroline=False,
        showgrid=False,
        showticklabels=False,
        title=''
    )

    layout = go.Layout(
        title=title,
        width=1000,
        height=1000,
        showlegend=False,
        scene=dict(
            xaxis=axis_settings,
            yaxis=axis_settings,
            zaxis=axis_settings
        ),
        margin=dict(t=50, l=0, r=0, b=0)
    )

    # Assemble figure
    fig = go.Figure(data=edge_traces + [node_trace], layout=layout)

    # Save and open
    fig.write_html(f"{filename}.html", auto_open=True)




