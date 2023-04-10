
def calculate_std_dev(arr):
    n = len(arr)
    mean = sum(arr) / n
    variance = sum((x - mean) ** 2 for x in arr) / (n - 1)
    std_dev = variance ** 0.5
    return std_dev

def correlation(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    std_x = sum((xi - mean_x)**2 for xi in x) / (n - 1)
    std_y = sum((yi - mean_y)**2 for yi in y) / (n - 1)
    cov = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / (n - 1)
    return cov / (std_x * std_y)
