
"""
Module for filtering heart rate data.
"""

def filter_nondigits(list_of_heart_rates: list) -> list:
    """  
    Cleaner Function 1: Filter Non-Digits

    Args:
        list_of_heart_rates (list): List of heart rate values, some of which may not be numeric.

    Returns:
        list[int]: A list of integers containing only valid numeric heart rate values.
    """
    new_list_of_rates = [] 
    for heart_rate in list_of_heart_rates:
        heart_rate = heart_rate.strip() 
        if heart_rate and heart_rate.isdigit():
            new_list_of_rates.append(int(heart_rate))
    return new_list_of_rates

def filter_outliers(data: list) -> list:
    """
    Cleaner Function 2: Filter Outliers

    Args:
        data (list): List of integers representing heart rate values.

    Returns:
        list[int]: A list of integers with values outside the range of greater than or equal to 30 and less than or equal to 250 removed.
    """
    no_outliers = []
    for heart_rate in data:
        if 30 <= heart_rate <= 250:  
            no_outliers.append(heart_rate)  
    return no_outliers

# Function to clean heart rate data by calling both filter functions
def clean_heart_rate_data(list_of_heart_rates: list) -> list:
    """
    Combine both filter functions to clean heart rate data.

    Args:
        list_of_heart_rates (list): Raw heart rate data with potential non-digit values and outliers.

    Returns:
        list[int]: Cleaned list of heart rate values.
    """
    cleaned_data = filter_nondigits(list_of_heart_rates)
    cleaned_data = filter_outliers(cleaned_data)
    
    return cleaned_data