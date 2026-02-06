# CSE571 Winter 2026 - Homework 1

This homework combines probabilistic robotics concepts including particle filter localization and EKF SLAM.

## Structure

- `problem1_particle_filter/`: Particle filter-based localization
- `problem2_ekf_slam/`: Extended Kalman Filter SLAM
- `shared/`: Shared resources (URDF files, meshes)

## Installation

Follow the [instructions](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html) to install conda for python package management.

Create a conda environment for this homework:
```bash
conda create -n cse571 python=3.9
conda activate cse571
```

Then install the required packages:
```bash
pip install -r requirements.txt
```

### (optional) for Apple Silicon
For Apple Silicon we have to first install pybullet through conda-forge and the proceed to install the other required packages:
```bash
conda install -c conda-forge pybullet
pip install -r requirements.txt
```

## Problem 1: Particle Filter Localization

Navigate to `problem1_particle_filter/` and run:
```bash
python localization.py
```

## Problem 2: EKF SLAM

Navigate to `problem2_ekf_slam/` and run:
```bash
python localization.py
```
