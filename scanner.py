import socket
import threading
import networking

class PortScanner:
    def __init__(self, target, ports, timeout):
        self.target = networking.resolve_hostname(target) or target
        self.ports = self._parse_ports(ports)
        self.timeout = timeout
    
    def _parse_target(self, target):
        if "/" in target:
            first_ip, cidr = target.split("/")

    def _parse_ports(self, ports):
        if "-" in ports:
            start_port, end_port = ports.split("-")
            return range(int(start_port), int(end_port) + 1)
        else:
            return [int(port) for port in ports.split(",")]
    
    def _scan_port(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                result = sock.connect_ex((self.target, port))
                if result == 0:
                    return "open"
                else:
                    return "closed"
        except:
            return "error"
    
    def scan(self):
        results = {}
        threads = []
        for port in self.ports:
            t = threading.Thread(target=lambda x: results.update({x: self._scan_port(x)}), args=(port,))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
        
        return results