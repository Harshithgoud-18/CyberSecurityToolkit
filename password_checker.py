"""
Password Strength Checker Module

This module checks the strength of a password,
detects common passwords, and provides suggestions
to improve password security.
"""

# List of commonly used weak passwords
common_passwords = ["password","123456","admin","qwerty"]
def check_password(password):
    """
    Check the strength of a password.
    
    Args:
       password (str): Password entered by the user.
       
    Returns:
       str: Weak, Medium, or strong. 
    """
    score = 0
    #check length
    if len(password) >= 8:
        score +=1
    #check uppercase
    if any(char.isupper() for char in password):
        score +=1
    # check lowercase
    if any(char.islower() for char in password):
        score +=1
    #check digits
    if any(char.isdigit() for char in password):
        score +=1
    #check special charcater
    special = '!@#$%^&*'
    if any(char in special for char in password):
        score +=1
        
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"    
    
def password_suggestion(password):
    """
    Generate suggestions to improve password strength.

    Args:
        password (str): User password.

    Returns:
        list: Suggestions to improve the password.
    """
    suggestions=[]
    if len(password) <=8:
        # Check password length
        suggestions.append("Use at least 8 characters")
    if not any(char.isupper() for char in password):
        # Check uppercase letters
        suggestions.append("Add Uppercase letters")
    if not any(char.islower() for char in password):
        # Check lowercase letters
        suggestions.append("Add Lowercase letters")
    if not any(char.isdigit() for char in password):
        # Check numeric digits
        suggestions.append("Add digits")
    special="!@#$%^&*"
    if not any(char in special for char in password):
        # Check special characters
        suggestions.append("Add special characters")
        
    return suggestions

def common_password(password):
   """
    Check whether the password is commonly used.

    Args:
        password (str): Password entered by the user.

    Returns:
        bool: True if password is common, otherwise False.
    """   
   return password.lower() in common_passwords
