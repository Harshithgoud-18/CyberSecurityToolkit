"""
Cyber Security Toolkit

Author : Macharla Harshith Goud
Language : Python
Description:
A modular cybersecurity toolkit that includes
password analysis, hashing, DNS lookup, port scanning,
packet sniffing, website security scanning,
password management, vulnerability scanning,
and file encryption.
"""
#Local Modules
import password_checker
import hash_generator
import dns_lookup
import port_scanner
import log_analyzer
import website_scanner
import packet_sniffer
import password_manager
import vulnerability_scanner 
from file_encryption import file_encryption_menu
import activity_logger

# ============================================
# Cyber Security Toolkit - Main Program
# ============================================

# Display the main menu
print("=" * 40)
print("      Cyber Security Toolkit")
print("=" * 40)

print("\n1. Password Strength Checker")
print("2. Text SHA-256 Generator")
print("3. File SHA-256 Generator")
print("4. Compare Two Files")
print("5. DNS Lookup")
print("6. Port Scanner")
print("7. Log Analyzer")
print("8. Website Security Scanner")
print("9. Packet Sniffer")
print("10. Password Manager")
print("11. Vulnerability Scanner")
print("12. File Encryption Tool")
print("0. Exit")


choice = input("\nEnter your choice: ")

#Password Strength Checker Module
if choice == "1":
    
    activity_logger.log_activity("Password Strength Checker")
    
    password = input("Enter Password: ")

    strength = password_checker.check_password(password)

    print("\nPassword Strength:", strength)

    if password_checker.common_password(password):
        print("\nWARNING: Common password detected!")

    suggestions = password_checker.password_suggestion(password)

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
# Text SHA-256 Generator Module
elif choice == "2":
    activity_logger.log_activity("Text SHA-256 Generator")
    
    text = input("Enter text: ")
    

    print("\nSHA-256 Hash:")
    print(hash_generator.generate_hash(text))
#File SHA-256 Generator Module
elif choice == "3":
    activity_logger.log_activity("File SHA-256 Generator")

    filename = "files/" + input("Enter file name: ")
    
    try:
        print("\nSHA-256 File Hash:")
        print(hash_generator.generate_file_hash(filename))

    except FileNotFoundError:
        print("File not found.")
#Compare Two Files Module 
elif choice =="4":
    activity_logger.log_activity("Compare Two Files")
    
    file1 = "files/" + input("Enter first file name: ")
    file2 = "files/" + input("Enter second file name: ")
    try:
        print(hash_generator.common_hash(file1, file2))
    except FileNotFoundError:
        print("One or both files are found.")
#DNS Lookup Module
elif choice =="5":
    activity_logger.log_activity("DNS Lookup")
    
    domain = input("Enter domain name: ")
    hostname = dns_lookup.get_hostname()
    ip = dns_lookup.lookup(domain)
    print("\nComputer Hostname:",hostname)
    print("Domain:",domain)
    print("IP Address:", ip )
#Port Scanner Module
elif choice == "6":
    activity_logger.log_activity("Port Scanner")

    host = input("Enter Host: ")

    services = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        443: "HTTPS"
    }

    ports = [21, 22, 23, 25, 53, 80, 443]

    print("\nScanning...\n")

    for port in ports:
        result = port_scanner.scan_port(host, port)
        print(port, services.get(port, "Unknown"), result)
#Log Analyzer Module
elif choice == "7":
    activity_logger.log_activity("Log Analyzer")
    
    filename = "logs/" + input("Enter log file name: ")
    
    try:
        info, warning, error = log_analyzer.analyze_log(filename)
        print("\n===== Log Analysis Report =====")
        print("INFO   :", info)
        print("WARNING  :", warning)
        print("ERROR  :", error)
    except FileNotFoundError:
        print("Log file not found.")   
#Website Security Scanner Module
elif choice == "8":
    activity_logger.log_activity("Website Security Scanner")
    
    url = input("Enter Website URL (include https://): ")
    
    result = website_scanner.scan_website(url)
    
    print("\n===== Website Scan Report =====")
    
    if isinstance(result, dict):
        
        print("Status Code :", result["Status Code"])
        print("Server :", result["Server"])
        print("Content Type :", result["Content Type"])
        
        print("\nSecurity Headers:")
        
        for header, status in result["Security Headers"].items():
            print(header, ":", status)
    else:
        print(result)
#packet Sniffer Module
elif choice == "9":
    activity_logger.log_activity("Packet Sniffer")
    packet_sniffer.start_sniffer()
#password Manager Module
elif choice == "10":
    activity_logger.log_activity("Password Manager")
    password_manager.password_menu()
#Vulernability Scanner Module
elif choice == "11":
    activity_logger.log_activity("Vulnerability Scanner")
    host = input("Enter Host: ")
    
    start_port = int(input("Start Port: "))
    end_port  = int(input("End Port: "))
    
    ports = vulnerability_scanner.scan_host(host, start_port, end_port)
    
    print("\nOpen Ports Found:", len(ports))
    print("Report saved as scan_report.txt")
#File Encryption Module
elif choice == "12":
    activity_logger.log_activity("File Encryption Tool")
    
    file_encryption_menu()
#Exit Module
elif choice == "0":
    print("\nThank you for using Cyber Security Toolkit!")
#Invaild menu option
else:
    print("Invalid Choice")
    
    