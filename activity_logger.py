"""
Activity Logger Module

This module records user activities performed
within the Cyber Security Toolkit.
"""

# Standard Library
from datetime import datetime

LOG_FILE = "logs/activity.log"

def log_activity(activity):
    """
    Record a user activity in the activity log.

    Args:
        activity (str): Name of the activity performed.
    """
    
    # Get current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Append activity to the log file
    with open(LOG_FILE, "a") as file:
        file.write(f"{current_time} - {activity}\n")