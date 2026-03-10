# Electrical Power Data Analysis using Python

This project analyzes three-phase electrical power quality data using Python. The dataset used in this project was collected in 2024 during a power quality monitoring activity using a power quality analyzer connected to the main panel of an airport site in the Philippines. The original analysis was performed using Excel, and this repository revisits the dataset using Python for deeper data visualization and imbalance detection.

## Features

- Cleans raw electrical datasets
- Calculates three-phase current imbalance
- Classifies imbalance conditions
- Generates summary reports
- Visualizes current trends

## Technologies Used

Python  
Pandas  
NumPy  
Matplotlib  

## Engineering Analysis

The project calculates current imbalance using the IEEE/NEMA formula:

Imbalance (%) = Max Deviation from Average Current / Average Current × 100

Thresholds used:

Normal < 10%  
Warning 10–15%  
Critical > 15%

