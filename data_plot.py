

class NormalIter:
    def __init__(self, data, scale=1):
        self.data = data
        self.min_data = min(data)
        self.max_data = max(data)

        self.amplitude = self.max_data - self.min_data
        self.normalize_factor = 1 / self.amplitude

        self.offset = self.min_data if self.min_data >= 0 else -self.min_data
        self.scale = scale

    def single(self, item):
        return (item - self.offset) * self.normalize_factor * self.scale

    def __iter__(self):
        for item in self.data:
            yield self.single(item)



def scatter(plot_func, size, data1, data2):
    width, height = size
    for x, y in zip(NormalIter(data1, width), NormalIter(data2, height)):
        plot_func(x, y)
