class ResultsProcessor:
    def __init__(self, results):
        self.results = results
    
    def get_open_ports(self):
        return [port for port, status in self.results.items() if status == "open"]
    
    def get_closed_ports(self):
        return [port for port, status in self.results.items() if status == "closed"]
    
    def get_error_ports(self):
        return [port for port, status in self.results.items() if status == "error"]
    
    def get_summary(self):
        open_ports = self.get_open_ports()
        closed_ports = self.get_closed_ports()
        error_ports = self.get_error_ports()

        summary = f"Scan results for {self.results['target']}:\n"
        summary += f"{len(open_ports)} ports open, "
        summary += f"{len(closed_ports)} ports closed, "
        summary += f"{len(error_ports)} ports with errors."

        return summary