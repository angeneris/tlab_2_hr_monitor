"""
Module for calculating descriptive statistics on windows of heart rate data.
"""

import pandas as pd
from statistics import mean, stdev 

# Define the function window_max: Calculate maximum of every "n"-size window
def window_max(data: list, n: int) -> list:
    """
    Calculate maximum values of every "n"-size window.

    Args:
        data (list): list of integers representing heart rate samples
        n (int): The size of the window
    Returns:
        list[int]: List of maximums heart rate value from each window
    """
    maximums = []
    for i in range(0, len(data), n):  
        window = data[i:i + n]           
        if window:                       
            maximums.append(max(window))  
    return maximums

# Define the function window_average: Calculate the average of every "n"-size window
def window_average(data: list, n: int) -> list:
    """
    Calculate average values of every "n"-size window.

    Args:
        data (list): list of integers representing heart rate samples
        n (int): The size of the window
    Returns:
        list[int]: List of average heart rate values from each window
"""

    averages = []
    for i in range(0, len(data), n):  # Start, stop, step
        window = data[i:i + n]           # Slice the current window
        if window:                       # Check if the window is non-empty
            averages.append(mean(window))  # Find the avg value in the window
    return averages

def window_stddev(data: list, n: int) -> list:
    """
    Calculate standard deviations within every "n"-size window.

    Args:
        data (list): list of integers representing heart rate samples
        n (int): The size of the window
    Returns:
        list[int]: List of standard deviation heart rate values from each window
"""
    standard_devs = []
    for i in range(0, len(data), n):  
        window = data[i:i + n]  
        if len(window) > 1:  
            # Calculate the standard deviation for the window and round it to 2 decimal places
            windown_std = stdev(window)
            standard_devs.append(round(windown_std, 2))  
        else:
            return standard_devs  # early return if window size is insufficient (len(window) <= 1)
    return standard_devs 