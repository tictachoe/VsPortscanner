import socket
import ipaddress

def resolve_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.error:
        return None

def generate_ips(cidr): 
    ip_network = ipaddress.ip_network(cidr, strict=False)

    return [str(ip) for ip in ip_network.hosts()]