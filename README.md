NOAA Temperature Analysis

Project Overview

This project analyzes and visualizes NOAA temperature data from Ann Arbor, Michigan, United States for the years 2005-2015. The objective is to identify record high and low temperatures, detect record-breaking temperatures in 2015, and map the weather stations contributing to the dataset.
Dataset

The analysis is based on two files:
1.	temperature.csv – Contains daily temperature records from 2005-2015.
2.	BinSize.csv – Provides bin size details for the dataset.
Variables in temperature.csv
•	id : Station identification code
•	date : Date in YYYY-MM-DD format
•	element : Type of measurement (e.g., TMAX or TMIN)
•	value : Temperature value (in tenths of degrees Celsius)
Tasks & Implementations

1.	Data Cleaning & Preprocessing
*	Remove leap day (Feb 29) records to maintain consistency.
*	Convert temperature values from tenths of degrees Celsius to standard degrees.
*	Separate temperature data for 2005-2014 and 2015.
  
2.	Visualization of Temperature Trends
*	Plot record high and low temperatures from 2005-2014 using a line graph.
*	Shade the area between record high and low temperatures.
  
3.	Identifying Record-breaking Temperatures in 2015
*	Overlay a scatter plot for days in 2015 when new record highs or lows were set.
  
4.	Mapping Weather Stations
*	Use Folium to visualize the locations of weather stations contributing to the dataset.
  
5.	Temperature Summary for 2015
*	Provide insights into temperature trends for the year 2015.

Required Libraries
•	Pandas – For data processing
•	Matplotlib & Seaborn – For plotting temperature trends
•	NumPy – For data manipulation
•	Folium – For station mapping
•	Geopandas (if needed) – For geospatial analysis

How to Run the Notebook 
Clone the repository:
git clone https://github.com/athulyasiji/NOAA_Temperature_Analysis.git
cd NOAA_Temperature_Analysis
1.	Install dependencies:
pip install -r requirements.txt
2.	Open the Jupyter Notebook:
   jupyter notebook
3.	Run NOAA_Temperature_Analysis.ipynb.

NOAA_Temperature_Analysis/
│── datasets/
│   ├── temperature.csv
│   ├── BinSize.csv
│── outputs/
│   ├── map.html
│   ├── temperature_plot.png
│── NOAA_Temperature_Analysis.ipynb
│── README.md
│── requirements.txt

Author
Athulya Siji


