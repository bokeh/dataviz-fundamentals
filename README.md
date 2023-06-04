# Fundamentals of Data Visualization, in Bokeh 📊

*⚠️ Note: This repository is a WIP, "watch" it to keep up with updates!*

## Project description

This repository hosts Bokeh equivalents for various plots from [*Fundamentals of Data Visualization* by Claus O. Wilke](https://clauswilke.com/dataviz/). It provides a collection of interactive data visualizations implemented using the Bokeh library.

## Table of contents (WIP)

1. Introduction

2. Visualizing amounts
	- Chapter 6.1 - Bar plots
	- Chapter 6.2 - Grouped and stacked bars
	- Chapter 6.3 - Dot plots and heatmaps
3. Visualizing distributions
	- Chapter 7.1 - Single distribution histogram and density plot
	- Chapter 7.2 - Multiple distribution histogram and density plot
	- Chapter 9.1 - Box plots
	- Chapter 9.2 - Ridgeline plots
4. Visualizing proportions
	- Chapter 10.1 - Pie charts
	- Chapter 10.2 - Side-by-side bars
	- Chapter 10.3 - Stacked bars and stacked densities
	- Chapter 10.4 - Partial densities
	- Chapter 11.2 - Mosaic plots and treemaps
	- Chapter 11.4 - Parallel sets
5. Visualizing associations
	- Chapter 12.1 - Scatter plots
	- Chapter 12.4 - Paired data

6. Visualizing geospatial data
	- Chapter 15.2 Layers

7. Conclusion


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
