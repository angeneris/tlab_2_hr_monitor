"""
The main Python module that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import window_max, window_average, window_stddev
from cleaner import filter_nondigits, filter_outliers, clean_heart_rate_data

import matplotlib.pyplot as plt

def run(filename: str, n: int = 5) -> None:  # Default n to 5
    """
    Process heart rate data from the specified file, clean it, calculate metrics, 
    and save visualizations using an n-sized window.

    Args:
        filename (str): The path to the data file (e.g., 'data/data1.txt').
        n (int): The size of the window for rolling calculations (default is 5).

    Steps:
        1. Read the file into a list of strings.
        2. Use `filter_nondigits` to clean the data and remove invalid entries.
        3. Use `filter_outliers` to remove unrealistic heart rate samples (<30 or >250).
        4. Calculate rolling maximums, averages, and standard deviations using an n-sized window.
        5. Save the plots to the `images/` folder:
            - Rolling maximums -> 'images/maximums.png'
            - Rolling averages -> 'images/averages.png'
            - Rolling standard deviations -> 'images/stdevs.png'

    Returns:
        list[int], list[int], list[int]: You will return the maximums, averages, and stdevs (in this order).
    """  
    data = []

    # open file and read into the `data` list
    with open(filename, 'r') as heart_rates_file:
        for line in heart_rates_file:
            data.append(line.strip())  
    print("Data read from file:", data)  # Debug 

    # Clean data by removing non-digit entries and outliers
    clean_data = clean_heart_rate_data(data)
    print("Cleaned data after removing non-digits and outliers:",clean_data)  # Debug

    # Ensure cleaned_data is not empty and return empty lists if there's no valid data
    if not clean_data:
        return [], [], []  

    # Calculate rolling metrics using the n-sized window
    maximums = window_max(clean_data, n)  
    averages = window_average(clean_data, n)  
    stdevs = window_stddev(clean_data, n)  

    # Return all 3 lists
    return maximums, averages, stdevs


if __name__ == "__main__":
    run("data/data1.txt")
