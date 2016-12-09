def standard_deviation(x):
    """
    calculates the standard deviation.  Does not correct for bias

    inputs
    ------
    x: list of all floats/integers

    returns:
    float - standard deviation
    """
    
    for elem in x:
        if isinstance(elem, int) != True and isinstance(elem, float) != True:
            raise TypeError("List elements must be float or int")  

    if len(x) < 2: return None

    n = len(x)
    mean = sum(x) / n
    ssq = sum((x_i-mean)**2 for x_i in x)
    stdev = (ssq/n)**0.5
    return stdev


def standard_error(x):
    for elem in x:
        if isinstance(elem, int) != True and isinstance(elem, float) != True:
            raise TypeError("List elements must be float or int")  

    if len(x) < 2: return None

    return standard_deviation(x) / len(x) ** 0.5
