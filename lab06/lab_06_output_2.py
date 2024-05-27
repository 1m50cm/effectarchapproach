class DataAnalyzer:
    def __init__(self, data):
        self.data = data
        self.total = sum(self.data)
        self.count = len(self.data)

    def set_data(self, new_data):
        self.data = new_data
        self.total = sum(self.data)
        self.count = len(self.data)

    def get_total(self):
        return self.total

    def get_count(self):
        return self.count

    def calculate_average(self):
        return self.total / self.count if self.count != 0 else 0

    def calculate_minimum(self):
        return min(self.data) if self.data else None

    def calculate_maximum(self):
        return max(self.data) if self.data else None
