# Step 1: Import Required Libraries
import numpy as np
import pandas as pd
import scipy.io as sio  # For reading MATLAB files
import matplotlib.pyplot as plt

# Step 2: Load the Data
# Provide the path to the sample .mat file in the data folder
data_path = "../data/sample_data.mat"

# Load the MATLAB data file
try:
    mat_data = sio.loadmat(data_path)
    print("Data successfully loaded.")
except FileNotFoundError:
    print(f"Error: The file {data_path} was not found.")

# Step 3: Explore the Data
# Check the structure of the loaded data
print("\nKeys in the dataset:")
print(mat_data.keys())

# Example: Access a specific part of the data (modify based on the actual dataset structure)
if "SUB01" in mat_data:
    subject_data = mat_data["SUB01"]
    print("\nAvailable attributes for subject data:")
    print(subject_data.dtype.names)

# Step 4: Perform Basic Analysis
# Example: Print demographic info if available
if "subjectInfo" in subject_data.dtype.names:
    subject_info = subject_data["subjectInfo"]
    print("\nSubject Demographic Information:")
    print(subject_info)

# Example: Visualize one type of data (e.g., joint angles or markers)
if "Markers" in subject_data.dtype.names:
    marker_data = subject_data["Markers"]
    print("\nMarkers Data Shape:")
    print(marker_data.shape)
    
    # Plot a sample marker trajectory
    plt.plot(marker_data[:, 0], marker_data[:, 1])
    plt.title("Sample Marker Trajectory")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.show()
