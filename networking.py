import socket
import ipaddress

# Resolves hostname to ip address
def resolve_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.error:
        return None

# Generates the ips in the network from cidr notation
def generate_ips(cidr): 
    ip_network = ipaddress.ip_network(cidr, strict=False)

    return [str(ip) for ip in ip_network.hosts()]