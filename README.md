# Graph Visualization Tool

This repository provides tools to visualize graphs using Plotly. It supports both 2D and 3D visualizations with customizable layouts, node sizes, edge weights, and edge colors.

## Features

- Visualize graphs in 2D or 3D.
- Support for various layout algorithms (`graphviz`, `spring`, `spectral`, `random`).
- Customize node sizes, edge weights, and edge colors.
- Generate output as interactive HTML files.

## Installation

1. Install Graphviz (for Ubuntu):

   ```bash
   sudo apt-get install graphviz libgraphviz-dev pkg-config
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Main Script

To visualize a graph, run the main script with the following command-line arguments:

```bash
python main.py --layout <layout> --node_size <size> --output <output_file> --title <title>
```

### Command-line Options

- `--layout`: Specifies the layout algorithm for positioning the graph. Options: `graphviz`, `spring`, `spectral`, `random`. Default: `graphviz`.
- `--node_size`: Sets the size of the nodes. Default: `20`.
- `--output`: Specifies the output file name for the HTML visualization. Default: `outputs/graphviz.html`.
- `--title`: Sets the title for the visualization. Default: `Graph Visualization`.

### Example

#### 2D Graph Visualization

```bash
python main.py --layout graphviz --node_size 20 --output outputs/graphviz.html --title "2D Graph Visualization"
```

#### 3D Graph Visualization

```bash
python main.py --layout spring --node_size 30 --output outputs/spring_3d.html --title "Spring Layout 3D Visualization"
```

### Additional Layouts

You can add new layout options by extending the `--layout` argument in the script and implementing the corresponding layout logic.

## Repository Structure

- `main.py`: The main script for visualizing graphs.
- `plotly_visualize.py`: Helper functions for 2D and 3D visualizations.
- `outputs/`: Directory for storing the generated HTML files.

## Contributing

Contributions are welcome! Feel free to open issues or create pull requests to improve this repository.

## License

This project is licensed under the MIT License.

## Additional Resources

For more details on using Plotly with Graphviz, check out [this Medium post](https://medium.com/@hilbert.cantor/network-plot-with-plotly-and-graphviz-ebd7778073b).
