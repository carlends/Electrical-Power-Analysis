# Electrical Power Data Analysis using Python

This project analyzes three-phase electrical power quality data using Python.

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
