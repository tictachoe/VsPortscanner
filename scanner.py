import socket
import threading
import networking

class PortScanner:
    def __init__(self, target, ports, timeout):
        self.target = target
        self.ports = self._parse_ports(ports)
        self.timeout = timeout

    # Parses ports into a range of ports or a list
    def _parse_ports(self, ports):
        if "-" in ports:
            start_port, end_port = ports.split("-")
            return range(int(start_port), int(end_port) + 1)
        else:
            return [int(port) for port in ports.split(",")]
    
    # Scans the ports checking if they are open or closed
    # if open it checks for the service
    def _scan_port(self, ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    service = socket.getservbyport(port)
                    return "open ({})".format(service)
                else:
                    return "closed"
        except:
            return "error"

    # Function that creates the threads that run the _scan_port function
    # uses a lambda function to update the dict with the results of the scan
    def scan(self):
        results = {}
        threads = []
        if "/" in self.target:
            network = networking.generate_ips(self.target)
            for ip in network:
                for port in self.ports:
                    t = threading.Thread(target=lambda x, y: results.update({(x, y): self._scan_port(x, y)}), args=(ip, port))
                    threads.append(t)
                    t.start()
        else:
            ip = networking.resolve_hostname(self.target)
            for port in self.ports:
                t = threading.Thread(target=lambda x, y: results.update({(str(x), y): self._scan_port(str(x), y)}), args=(ip, port))
                threads.append(t)
                t.start()

        for t in threads:
            t.join()
        
        return results