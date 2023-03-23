class ResultsProcessor:
    def __init__(self, results):
        self.results = results
    
    def scan(self):
        for key, value in self.results.items():
            print("[{}] {}: {}".format(key[0], key[1], value))