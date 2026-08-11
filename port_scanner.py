"""
Port Scanner Module

This module scans a specific TCP port on a target host
and determines whether the port is open or closed.
"""

# Standard Library
import socket

def scan_port(host,port):
    """
    Scan a TCP port on a remote host.

    Args:
        host (str): Target hostname or IP address.
        port (int): Port number to scan.

    Returns:
        str: "Open" if the port is open, otherwise "Closed".
    """ 
     # Create a TCP socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
     # Set timeout to avoid waiting indefinitely 
    sock.settimeout(1)
     # Attempt to connect to the target port
    result = sock.connect_ex((host,port))
     # Close the socket
    sock.close()
    
    # Return scan result
    if result == 0:
        return "Open"
    else:
        return "Closed"
    