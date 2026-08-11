"""
Website Security Scanner Module

This module scans a website and retrieves basic
security-related information such as HTTP status,
server details, content type, and important
security headers.
"""

# Third-Party Libraries
import requests
def scan_website(url):
    """
    Scan a website and collect security information.

    Args:
        url (str): Website URL (including https://).

    Returns:
        dict: Website scan results if successful.
        str: Error message if the website is unreachable.
    """
    try:
        # Send HTTP GET request
        response = requests.get(url,timeout=5)
        
        result ={}
        
        # Store HTTP status code
        result["Status Code"] = response.status_code
        
        # Retrieve server information
        result["Server"] = response.headers.get("Server","Unknown")
        
        # Retrieve content type
        result["Content Type"] = response.headers.get("Content-Type","Unknown")
        
        # List of important security headers
        security_headers = [
            "Strict-Transport-Security",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Content-Security-Policy"
        ]
        
        headers_found = {}
        
        # Check whether each security header exists
        for header in security_headers:
            
            if header in response.headers:
                headers_found[header] = "Present"
            else:
                headers_found[header] = "Missing"
            
        result["Security Headers"] = headers_found
        
        return result
    except requests.exceptions.RequestException:
        return "Website unreachable"