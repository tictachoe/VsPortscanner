import socket

def resolve_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.error:
        return None