def quantile (series, alpha=0.05):
    """Calculate the lower and upper confidence interval
    
    args:
        Series [int]: The size of the series
        alpha [float]: The significance value
    Return:
        Return the lower and upper confidence interval 
        of the number of the series as a tuple
    
    """
    
    #values = [int(random.random()*10) for i in range(series)]

    sorted_values = sorted(series)
    sorted_values

    n = len(sorted_values)
    lower_idx = round(n*alpha/2)
    upper_idx = round(n*(1-alpha/2))-1

    return sorted_values[lower_idx], sorted_values[upper_idx]
 
# check if it works
quantile([1,23,4,5,56,48,17,4,5,1,6,8,7,520])