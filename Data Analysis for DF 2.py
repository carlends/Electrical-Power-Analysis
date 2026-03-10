import pandas as pd
import numpy as np
import os

file_path = "Clean Power Quality Data 1.csv"
df = pd.read_csv(file_path)

df.columns = df.columns.str.strip()

df["IA"] = pd.to_numeric(df["IA"], errors="coerce")
df["IB"] = pd.to_numeric(df["IB"], errors="coerce")
df["IC"] = pd.to_numeric(df["IC"], errors="coerce")

df = df.dropna(subset=["IA", "IB", "IC"])

# Average current
df["Iavg"] = np.mean(df[["IA", "IB", "IC"]], axis=1)

# Deviations from average
df["Deviation_A"] = np.abs(df["IA"] - df["Iavg"])
df["Deviation_B"] = np.abs(df["IB"] - df["Iavg"])
df["Deviation_C"] = np.abs(df["IC"] - df["Iavg"])

# Maximum deviation
df["Max_Deviation"] = np.max(df[["Deviation_A", "Deviation_B", "Deviation_C"]], axis=1)

# Current imbalance percentage
df["Current_Imbalance_%"] = (df["Max_Deviation"] / df["Iavg"]) * 100

# Conditions
conditions = [
    df["Current_Imbalance_%"] <= 10,
    (df["Current_Imbalance_%"] > 10) & (df["Current_Imbalance_%"] <= 15),
    df["Current_Imbalance_%"] > 15
]

choices = ["Normal", "Warning", "Critical"]

# Add default as string
df["Status"] = np.select(conditions, choices, default="Unknown")

output_file = "imbalance_report.csv"
df.to_csv(output_file, index=False)

print("Three-Phase Current Imbalance Report")
print("------------------------------------")
print("Total rows:", len(df))
print("Average imbalance:", round(np.mean(df["Current_Imbalance_%"]), 2), "%")
print("Max imbalance:", round(np.max(df["Current_Imbalance_%"]), 2), "%")
print("Min imbalance:", round(np.min(df["Current_Imbalance_%"]), 2), "%")

print("Normal:", len(df[df["Status"] == "Normal"]))
print("Warning:", len(df[df["Status"] == "Warning"]))
print("Critical:", len(df[df["Status"] == "Critical"]))

print("Report saved as:", output_file)

import matplotlib.pyplot as plt

# Create x-axis using row number
x = range(len(df))

# 1. Plot IA, IB, IC
plt.figure(figsize=(12, 6))
plt.plot(x, df["IA"], label="IA")
plt.plot(x, df["IB"], label="IB")
plt.plot(x, df["IC"], label="IC")
plt.xlabel("Data Point")
plt.ylabel("Current (A)")
plt.title("Three-Phase Current Trend")
plt.legend()
plt.grid(True)
plt.show()

# 2. Plot Current Imbalance %
plt.figure(figsize=(12, 6))
plt.plot(x, df["Current_Imbalance_%"], label="Current Imbalance %")
plt.axhline(10, linestyle="--", label="Warning Threshold (10%)")
plt.axhline(15, linestyle="--", label="Critical Threshold (15%)")
plt.xlabel("Data Point")
plt.ylabel("Imbalance (%)")
plt.title("Current Imbalance Percentage")
plt.legend()
plt.grid(True)
plt.show()

# 3. Plot Status Count
status_counts = df["Status"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(status_counts.index, status_counts.values)
plt.xlabel("Status")
plt.ylabel("Count")
plt.title("Imbalance Status Summary")
plt.grid(axis="y")
plt.show()