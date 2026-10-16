import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    ar_data = np.asarray(data, dtype='float64')
    mean = np.mean(ar_data)
    median = np.median(ar_data)
    ordered_values, counts = np.unique(ar_data, return_counts = True)
    mode = ordered_values[np.argmax(counts)]
    p1 = np.percentile(ar_data,25)
    p2 = np.percentile(ar_data,50)
    p3 = np.percentile(ar_data,75)
    variance = np.var(ar_data)
    standard_deviation = np.std(ar_data)
    interquartile_range= p3 - p1
    return {'mean': mean, 'median': median, 'mode': mode, 'variance': variance, 'standard_deviation': standard_deviation, '25th_percentile':p1,'50th_percentile':p2,'75th_percentile':p3, 'interquartile_range':interquartile_range}
   