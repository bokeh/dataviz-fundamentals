# Fundamentals of Data Visualization, in Bokeh 📊

*⚠️ Note: This repository is a WIP, "watch" it to keep up with updates!*

## Project description

This repository hosts Bokeh equivalents for various plots from [*Fundamentals of Data Visualization* by Claus O. Wilke](https://clauswilke.com/dataviz/). It provides a collection of interactive data visualizations implemented using the Bokeh library.

The full rendered pages of this repository can be found [here](https://bokeh.github.io/dataviz-fundamentals/)

## Table of contents (WIP)

1. Introduction: An overview of the narrative and type of plots to expect.

2. Visualizing amounts
	- Chapter 6.1 - Bar plots: Representing amounts using vertical and horizontal bars
	- Chapter 6.2 - Grouped and stacked bars: Visualizing multiple groups or categories using grouped and stacked bars.
	- Chapter 6.3 - Dot plots and heatmaps: using dots and colors to represent values.

3. Visualizing distributions
	- Chapter 7.1 - Single distribution histogram and density plot: Showing the distribution of a single variable using histograms or density plots.
	- Chapter 7.2 - Multiple distribution histogram and density plot: Comparing multiple distributions using histograms and density plots
	- Chapter 9.1 - Box plots:Illustrating the distribution of data using boxes and whiskers.
	- Chapter 9.2 - Ridgeline plots: Illustrating the density of multiple distributions along a common axis.

4. Visualizing proportions
	- Chapter 10.1 - Pie charts: Dsplaying proportions using pie charts.
	- Chapter 10.2 - Side-by-side bars: Comparing proportions across categories using side-by-side bars.
	- Chapter 10.3 - Stacked bars and stacked densities: representing proportions using stacked bars and stacked density plots.
	- Chapter 10.4 - Partial densities: Visualizing partial densities within a distribution.
	- Chapter 11.2 - Mosaic plots and treemaps: Showing proportions and hierarchical relationships using mosaic plots or treemaps.
	- Chapter 11.4 - Parallel sets: Visualizing categorical data and their associations using parallel sets.

5. Visualizing associations
	- Chapter 12.1 - Scatter plots: Illustrating the relationship between two variables using points on a Cartesian plane.
	- Chapter 12.4 - Paired data: Visualizing associations between paired data points.

6. Visualizing geospatial data
	- Chapter 15.2 Layers: Illustrating geographical data using layers on a map.

7. Conclusion: Summary of the key points and importance of Data visualization using Bokeh.


## Local setup

To run these notebooks locally, follow these steps:

1. Clone the repository:

        git clone https://github.com/bokeh/dataviz-fundamentals.git

2. Navigate to the project directory via the terminal or command prompt.

3. Create a new conda environment and install the required dependencies:

        conda env create -n <name> -f environment.yml

replacing `<name>` with your preferred environment name.

4. Activate the new environment:

        conda activate <name>

5. Open Jupyter notebook via anaconda navigator or via the command line:

        jupyter notebook

6. Open the desired notebook in your web browser and run the cells.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow the guidelines below:

- Fork the repository and create your branch.
- Make your changes and ensure the code follows the project's coding style.
- Test your changes thoroughly.
- Submit a pull request with a clear description of your changes.

## License & Code of Conduct

This project is licensed under the [MIT](https://github.com/clauswilke/dviz.supp/blob/master/LICENSE) and [BSD 3-Clause](https://github.com/bokeh/bokeh/blob/branch-3.1/LICENSE.txt) licence. By contributing to this project, you agree to abide by the [Bokeh Code of Conduct](https://github.com/bokeh/bokeh/blob/branch-3.1/docs/CODE_OF_CONDUCT.md).
