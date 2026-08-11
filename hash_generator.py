"""
SHA-256 Hash Generator Module

This module generates SHA-256 hashes for
text and files and compares two files
using their hash values.
"""
#Standard Library
import hashlib

# Generate SHA-256 hash
def generate_hash(text):
    """
    Generate SHA-256 hash for text.

    Args:
        text (str): Input text.

    Returns:
        str: SHA-256 hash.
    """
    hash_value = hashlib.sha256(text.encode()).hexdigest()
    return hash_value

def generate_file_hash(filename):
    """
    Generate SHA-256 hash for a file.

    Args:
        filename (str): Path to the file.

    Returns:
        str: SHA-256 hash.
    """
    # Create SHA-256 object
    sha256 = hashlib.sha256()
    # Read file in binary mode
    with open(filename,"rb") as file:
        while True:
            # Read file in chunks
            chunk = file.read(4096)
            
            if not chunk:
                break
            sha256.update(chunk)
        return sha256.hexdigest()

def common_hash(file1,file2):
    """
    Compare two files using SHA-256 hashes.

    Args:
        file1 (str): First file.
        file2 (str): Second file.

    Returns:
        str: Comparison result.
    """
    hash1 = generate_file_hash(file1)
    hash2 = generate_file_hash(file2)
    if hash1 == hash2:
        return "File ars identical."
    else:
        return "File are different."