
def calculate_std_dev(arr):
    n = len(arr)
    mean = sum(arr) / n
    variance = sum((x - mean) ** 2 for x in arr) / (n - 1)
    std_dev = variance ** 0.5
    return std_dev
