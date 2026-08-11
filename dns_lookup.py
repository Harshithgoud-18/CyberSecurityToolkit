"""
DNS Lookup Module

This module provides functions to retrieve the IP address
of a domain and the hostname of the local computer.
"""
#Standard Library
import socket

def lookup(domain):
    """
    Retrieve the IP address of a given domain.

    Args:
        domain (str): Domain name entered by the user.

    Returns:
        str: IP address if successful, otherwise an error message.
    """
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return "Invalid domain or unable to resolve."
    
def get_hostname():
    """
    Retrieve the hostname of the local computer.

    Returns:
        str: Computer hostname.
    """    
    return socket.gethostname()
   