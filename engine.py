class Engine:

    def __init__(self):
        self.results = set()

    def add(self, items):
        self.results.update(items)

    def export(self):
        return sorted(self.results)