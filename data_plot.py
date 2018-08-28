
def normalizer(data):
    min_data = min(data)
    amplitude = max(data) - min_data

    offset = min_data if min_data >= 0 else -min_data

    return offset, scale_factor




def scatter(plot_func, size, data1, data2):
    width, height = size
