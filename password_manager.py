"""
Password Manager Module

This module securely stores, retrieves, searches,
and deletes user passwords using Fernet encryption.
Passwords are stored in JSON format.
"""

#Standard Library 
import json
import os
# Third-Party Library
from cryptography.fernet import Fernet

PASSWORD_FILE = "data/passwords.json"
KEY_FILE = "keys/secret.key"

# Generate encryption key
def generate_key():
    """
    Generate an encryption key if it does not exist.
    """
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)
            
# Load existing passwords
def load_key():
    """
    Load the encryption key.

    Returns:
        bytes: Encryption key.
    """
    with open(KEY_FILE, "rb") as file:
        return file.read() 
    
# Encrypt password before saving
def encrypt_password(password):
    """
    Encrypt a password.

    Args:
        password (str): Plain text password.

    Returns:
        str: Encrypted password.
    """

    key = load_key()

    cipher = Fernet(key)

    encrypted = cipher.encrypt(password.encode())

    return encrypted.decode()

# Decrypt password after saving
def decrypt_password(password):
    """
    Decrypt an encrypted password.

    Args:
        password (str): Encrypted password.

    Returns:
        str: Original password.
    """

    key = load_key()

    cipher = Fernet(key)

    decrypted = cipher.decrypt(password.encode())

    return decrypted.decode()
   
# Save updated password list
def save_password(website, username, password):
    """
    Save a new website credential.
    """
    encrypted = encrypt_password(password)
    data = []
    
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    
    data.append({
        "website": website,
        "username": username,
        "password": encrypted
    })
    
    with open(PASSWORD_FILE, "w") as file:
        json.dump(data, file, indent=4)
        
    print("Password saved successfully.")
    
# Display decrypted passwords
def view_passwords():
    """
    Display all saved passwords.
    """
    if not os.path.exists(PASSWORD_FILE):
        print("NO passwords saved.")
        return
    
    with open(PASSWORD_FILE, "r") as file:
        data = json.load(file)
        
    print("\n===== Saved Password =====\n")
    
    for account in data:
        print("Website :", account["website"])
        print("Username:", account["username"])
        print("Password:", decrypt_password(account["password"]))
        print("-"*30)
        
def search_password(website):
    """
    Search for a password by website.
    """
    if not os.path.exists(PASSWORD_FILE):
        print("No passwords saved.")
        return
    
    with open(PASSWORD_FILE,"r") as file:
        data = json.load(file)
        
    for account in data:
        if account["website"].lower() == website.lower():
            print("\nPassword Found\n")
            print("website :", account["website"])
            print("username:", account["username"])
            print("Password:", decrypt_password(account["password"]))
            return
    print("Website not found.")

def delete_password(website):
    """
    Delete a saved password.
    """
    if not os.path.exists(PASSWORD_FILE):
        print("No passwords saved.")
        return
    with open(PASSWORD_FILE, "r") as file:
        data = json.load(file)
    updated_data = []
    found = False
    
    for account in data:
        if account["website"].lower() == website.lower():
            found = True
        else:
            updated_data.append(account)
    with open(PASSWORD_FILE, "w") as file:
        json.dump(updated_data, file, indent=4)
        
    if found:
        print("Password deleted successfully.")
    else:
        print("website not found.")





def password_menu():
    """
    Display the Password Manager menu.
    """
    generate_key()
    
    while True:
        print("\n" + "=" * 30)
        print("    PASSWORD MANAGER")
        print("=" * 30)
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Delete Password")
        print("5. Exit")
        
        choice = input("\nEnter your choice:")
        
        if choice == "1":
            website = input("Website: ")
            username = input("Username: ")
            password = input("Password: ")
            
            save_password(website, username, password)
            
        elif choice == "2":
            
            view_passwords()
        
        elif choice == "3":
            website = input("Enter Website: ")
            search_password(website)
        
        elif choice == "4":
            website = input("Enter Website to Delete: ")
            delete_password(website)
        
        elif choice == "5":
            print("Exiting Password Manager...")
            break
        
        else:
            print("Invalid Choice")
            
if __name__ == "__main__":
    password_menu()