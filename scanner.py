import socket
import threading
import networking

class PortScanner:
    def __init__(self, targets, ports, timeout):
        self.targets = self._parse_targets(targets)
        self.ports = self._parse_ports(ports)
        self.timeout = timeout
    
    def _parse_targets(self, targets):
        #resolved_targets = networking.resolve_hostname(targets)
        resolved_targets = targets
        if "/" in resolved_targets:
            return networking.generate_ips(targets)
        elif "," in resolved_targets:
            return [str(target) for target in targets.split(",")]
        else:
            return str(resolved_targets)

    def _parse_ports(self, ports):
        if "-" in ports:
            start_port, end_port = ports.split("-")
            return range(int(start_port), int(end_port) + 1)
        else:
            return [int(port) for port in ports.split(",")]
    
    def _scan_port(self, port):
        #print(self.targets)
        for ip in self.targets:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(self.timeout)
                    result = sock.connect_ex((ip, port))
                    if result == 0:
                        return "open"
                    else:
                        return "closed"
            except:
                return "error"
    
    def scan(self):
        results = {}
        threads = []
        for ips in self.targets:
            for port in self.ports:
                t = threading.Thread(target=lambda x: results.update({x: self._scan_port(x)}), args=(port,))
                threads.append(t)
                t.start()
        
        for t in threads:
            t.join()
        
        return results