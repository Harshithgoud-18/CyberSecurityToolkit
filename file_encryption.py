"""
File Encryption Tool

Description:
    A cybersecurity utility that encrypts and decrypts files
    using Fernet symmetric encryption.

Features:
    - Generate encryption key
    - Encrypt files
    - Decrypt files
    - Store files in separate folders

Library:
    cryptography.fernet
"""

from cryptography.fernet import Fernet
import os


# Encryption key file
KEY_FILE = os.path.join("keys", "secret.key")


def create_folders():
    """
    Creates required folders for file management.
    """
    folders = [
        "keys",
        "files",
        "encrypted",
        "decrypted"
        ]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)



def generate_key():
    """
    Generates a new encryption key and saves it.
    """

    if os.path.exists(KEY_FILE):
        print("\nEncryption key already exists!")
        return


    key = Fernet.generate_key()


    with open(KEY_FILE, "wb") as file:
        file.write(key)


    print("\nEncryption key generated successfully!")




def load_key():
    """
    Loads encryption key from secret.key file.

    Returns:
        Encryption key
    """

    if not os.path.exists(KEY_FILE):
        print("\nKey not found! Generate key first.")
        return None


    with open(KEY_FILE, "rb") as file:
        return file.read()




def encrypt_file():
    """
    Encrypts a file from files folder
    and saves it in encrypted folder.
    """

    filename = input("\nEnter file name to encrypt: ")


    input_file = "files/" + filename


    if not os.path.exists(input_file):

        print("\nFile not found in files folder!")
        return



    key = load_key()


    if key is None:
        return



    cipher = Fernet(key)



    with open(input_file, "rb") as file:
        data = file.read()



    encrypted_data = cipher.encrypt(data)



    output_file = "encrypted/" + filename + ".encrypted"



    with open(output_file, "wb") as file:
        file.write(encrypted_data)



    print("\nFile encrypted successfully!")
    print("Saved:", output_file)





def decrypt_file():
    """
    Decrypts encrypted file from encrypted folder
    and saves original file in decrypted folder.
    """

    filename = input("\nEnter encrypted file name: ")


    input_file = "encrypted/" + filename



    if not os.path.exists(input_file):

        print("\nEncrypted file not found!")
        return



    key = load_key()


    if key is None:
        return



    cipher = Fernet(key)



    with open(input_file, "rb") as file:
        encrypted_data = file.read()



    decrypted_data = cipher.decrypt(encrypted_data)



    original_filename = filename.replace(".encrypted", "")



    output_file = "decrypted/" + original_filename



    with open(output_file, "wb") as file:
        file.write(decrypted_data)



    print("\nFile decrypted successfully!")
    print("Saved:", output_file)





def file_encryption_menu():
    """
    Displays File Encryption Tool menu.
    """

    create_folders()


    while True:

        print("\n================================")
        print("       FILE ENCRYPTION TOOL")
        print("================================")

        print("1. Generate Encryption Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Back to Main Menu")


        choice = input("\nEnter your choice: ")



        if choice == "1":

            generate_key()



        elif choice == "2":

            encrypt_file()



        elif choice == "3":

            decrypt_file()



        elif choice == "4":

            break



        else:

            print("\nInvalid choice!")




# Run independently
if __name__ == "__main__":

    file_encryption_menu()