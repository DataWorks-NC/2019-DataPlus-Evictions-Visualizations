# Evictions
The Data+ Durham evictions team is tasked with creating visualizations to further three research questions within Durham, NC.

1) Do rises in evictions follow rises in rent, and for whom? 

2) What are the community-level costs of evictions?
  
3) How can we accessibly display eviction trends spatially over the past 20 years?

Over the course of a ten-week period, the Durham Evictions team at Data+, alongside the oversight of Dataworks, will begin to answer these questions while providing meaningful visualizations that can be used to further research on eviction trends in Durham with the hopes of providing policymakers with the tools and evidence to argue for legislative changes. 

# Tech/Framework Used
[![py-3.7](https://img.shields.io/badge/Python-3.7-blue.svg)](https://www.python.org/downloads/)

Packages:

[![npy](https://img.shields.io/badge/Numpy-1.16.4-green.svg)](https://pypi.org/project/numpy/)
[![scpy](https://img.shields.io/badge/Scipy-1.3.0-green.svg)](https://pypi.org/project/scipy/)
[![pd](https://img.shields.io/badge/Pandas-0.24.2-green.svg)](https://pypi.org/project/pandas/)
[![gpd](https://img.shields.io/badge/GeoPandas-0.5.0-green.svg)](https://pypi.org/project/geopandas/)
[![bkh](https://img.shields.io/badge/Bokeh-1.2.0-green.svg)](https://pypi.org/project/bokeh/)
[![psycopg2](https://img.shields.io/badge/psycopg-2.8.3-firebrick.svg)](https://pypi.org/project/psycopg2/)
[![DateTime](https://img.shields.io/badge/DateTime-4.3-green.svg)](https://pypi.org/project/DateTime/) 

# Features
1) Interactive chloropleth map
2) Interactive heatmap
3) Monthly categorical heatmap (individual years normalized for comparison)

# Prerequisites

You need to have pipenv installed and configured correctly before getting started.

# Installation
1) Clone repo from git

2) Change directory to repo location

Terminal:
```
pipenv install
pipenv shell
```

# How to Use?
Terminal:

`bokeh serve interactive/`

# Credits
Data+ Team: Rodrigo Araujo, Ellis Ackerman, Samantha Miezio

DataWorks Team: John Killeen, L’Tanya Durante, Tim Stallmann

Project Manager: Libby McClure

Legal Aid/Eviction Diversion Program: Peter Gilbert

# License
![Data+Logo](https://bigdata.duke.edu/sites/bigdata.duke.edu/files/site-images/image002-2.jpg)

