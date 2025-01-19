# Data Folder

This folder contains preliminary data samples for the project.

## Dataset Description

The dataset includes lower-limb kinematics and kinetics of 20 participants walking on surfaces with varying stiffness levels (1000 kN/m, 80 kN/m, 40 kN/m, and 25 kN/m) and at different speeds (0.8 m/s, 1.0 m/s, and 1.2 m/s). Data were collected using a Vicon motion capture system and a robotic treadmill.

This data can be used for:
- Identifying gait patterns and muscle activation profiles.
- Designing better controllers for prosthetic limbs and robotic walkers.
- Developing improved rehabilitation protocols and adaptive assistive devices.

## Files in this Folder

- **sample_data.mat**: A subset of the original dataset for testing and analysis purposes. Contains data from one participant in MATLAB `.mat` format.

## Data Dictionary

| **Variable Name**    | **Description**                                                                                      |
|-----------------------|----------------------------------------------------------------------------------------------------|
| Markers              | 3D positions of reflective markers on the body, sampled at 100 Hz.                                  |
| Joint Angles         | Angles of joints during motion, sampled at 100 Hz.                                                  |
| Forces               | Ground reaction forces, sampled at 65 Hz.                                                          |
| EMG                  | Muscle activation data, sampled at 2000 Hz.                                                        |
| Heart Rate           | Participant heart rate resampled to 100 Hz for synchronization.                                     |

## Source

The dataset is sourced from the open-access repository:  
Angelidou, C., Chambers, V., Hobbs, B., Karakasis, C., Artemiadis, P. (2025). "Kinematics, kinetics, and muscle activations during human locomotion over compliant terrains".  
Accessed from: [NeurIPS Datasets and Benchmarks](https://neurips.cc/datasets).

