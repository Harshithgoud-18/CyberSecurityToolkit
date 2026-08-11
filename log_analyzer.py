"""
Log Analyzer Module

This module analyzes log files and counts the number of
INFO, WARNING, and ERROR messages.
"""
def analyze_log(filename):
    """
    Analyze a log file and count log levels.

    Args:
        filename (str): Path to the log file.

    Returns:
        tuple: Number of INFO, WARNING, and ERROR entries.
    """

     # Initialize counters
    info = 0
    warning = 0
    error = 0
    
     # Open the log file
    with open(filename, "r") as file:
        # Read each line
        for line in file:
             # Count INFO messages
            if "INFO" in line:
                info += 1
             # Count WARNING messages
            elif "WARNING" in line:
                warning += 1
             # Count ERROR messages
            elif "ERROR" in line:
                error += 1
    # Return the counts
    return info, warning, error