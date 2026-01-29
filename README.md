# NFL Games Interactive Visualization

This project contains a Jupyter notebook that explores NFL game data and creates an interactive visualization using Plotly.

## Dataset

The dataset used is the **NFL Games Data (games.csv)** from the nflverse/nfldata GitHub repository:
- **Source**: https://github.com/nflverse/nfldata
- **Direct URL**: https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv
- Contains game-level data with 1000+ rows covering multiple NFL seasons (1999+)

## Setup

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

3. **Open the notebook**:
   - Open `visualization.ipynb` in Jupyter
   - Run all cells (Cell → Run All) or run cells sequentially

## Features

The notebook includes:
- **Dataset description**: Information about the NFL games dataset
- **Data loading and exploration**: Loading data from GitHub and exploring its structure
- **Research question**: Analysis of home vs away scoring patterns across NFL teams
- **Interactive visualization**: Plotly scatter plot with:
  - **Team dropdown filter**: Select individual teams or view all teams
  - **Season slider**: Filter games by season range (up to selected season)
  - **Hover tooltips**: Detailed game information on hover
  - **Zoom and pan**: Interactive exploration of the data
- **Interpretation**: Key insights and patterns to observe

## Visualization Details

The interactive scatter plot shows:
- **X-axis**: Points scored by a team
- **Y-axis**: Points allowed (opponent's score)
- **Color**: Different teams (each team has its own color)
- **Bubble size**: Margin of victory (larger = bigger win/loss margin)
- **Interactive controls**: Team dropdown and season slider

## Sharing the Visualization

### Option 1: HTML Export (Recommended for Static Sharing)
1. Run all cells in the notebook
2. Export to HTML:
   ```python
   # Add this cell at the end of the notebook
   fig.write_html("nfl_visualization.html")
   ```
3. Share the HTML file - it will work offline with full interactivity

### Option 2: Google Colab
1. Upload `visualization.ipynb` to Google Colab
2. Run all cells
3. Share the Colab link (File → Share)

### Option 3: GitHub with nbviewer
1. Upload the notebook to a GitHub repository
2. Share the nbviewer link: `https://nbviewer.org/github/YOUR_USERNAME/YOUR_REPO/blob/main/visualization.ipynb`
3. Note: Interactive Plotly visualizations work in nbviewer

### Option 4: Jupyter Notebook Viewer
1. If you have a public URL for your notebook, you can view it directly
2. Interactive features work in Jupyter Notebook Viewer

## Requirements

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- Internet connection (for downloading the dataset)

## Three.js Multi-View Visualization

This project also includes a Three.js-based visualization with multiple 3D views of the NFL data.

### Setup for Three.js Visualization

1. **Export the data** (run the export cell in the notebook or run the Python script):
   ```bash
   python export_data_for_threejs.py
   ```
   Or run the "Export Data for Three.js Visualization" cell in the notebook.

2. **Open the visualization**:
   - Open `nfl_threejs_visualization.html` in a web browser
   - Make sure `nfl_data.json` is in the same directory

### Three.js Visualization Features

The Three.js visualization includes **8 different view modes**:

1. **3D Scatter Plot**: Points scored vs points allowed vs season (3D space)
2. **3D Bar Chart**: Team performance bars showing average points scored
3. **3D Line Graph**: Season trends in scoring patterns
4. **Particle System**: Animated particle representation of games
5. **Network Graph**: Team connections based on game relationships
6. **3D Heatmap**: Team performance across seasons in 3D grid
7. **Spiral Timeline**: Spiral visualization of season progression
8. **Team Towers**: Stacked segments showing team performance over seasons

### Controls

- **View Mode Dropdown**: Switch between different visualization types
- **Auto Rotate**: Toggle automatic scene rotation
- **Rotation Speed**: Adjust rotation speed
- **Point Size**: Adjust size of data points
- **Season Filter**: Filter data by season
- **Reset Camera**: Return to default camera position
- **Toggle Labels**: Show/hide team and season labels

### Interaction

- **Left Click + Drag**: Rotate the camera
- **Right Click + Drag**: Pan the view
- **Scroll Wheel**: Zoom in/out
- **Hover**: See details about data points (in some views)

## Notes

- The dataset is downloaded directly from GitHub when you run the notebook
- No authentication or API keys required
- The Plotly visualization works in Jupyter notebooks, HTML exports, and most notebook viewers
- The Three.js visualization requires a modern web browser with WebGL support
- For the Three.js visualization, you need to export the data to JSON first (see above)
