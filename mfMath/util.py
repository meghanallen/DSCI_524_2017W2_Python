def standard_deviation(x):
    n = len(x)
    mean = sum(x) / n
    ssq = sum((x_i-mean)**2 for x_i in x)
    stdev = (ssq/n)**0.5
    return(stdev)

def standard_error(y):
    standard_error = lambda y: standard_deviation(y)/len(y)**0.5
    return(standard_error)
