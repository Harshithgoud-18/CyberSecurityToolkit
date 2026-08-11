"""
Cyber Security Toolkit - Web Interface

A Streamlit-based web interface for the 12 cybersecurity tools
in the Cyber Security Toolkit project.

For educational purposes and authorized security testing only.
"""

import os
import hashlib
import socket
import streamlit as st

# Local modules
import password_checker
import hash_generator
import dns_lookup
import port_scanner
import log_analyzer
import website_scanner
import password_manager
import vulnerability_scanner
import file_encryption

# ============================================================
# CUSTOM UI STYLE
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

h1 {
    text-align: center;
    font-size: 42px;
}

.tool-card {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #30363d;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Cyber Security Toolkit",
    page_icon="🔐",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("🔐 Cyber Security Toolkit")

st.caption(
    "A modular Python cybersecurity toolkit for educational "
    "and authorized security testing."
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🛡️ Security Tools")

tool = st.sidebar.selectbox(
    "Select a Tool",
    [
        "🏠 Dashboard",
        "🔐 Password Strength Checker",
        "🔑 Text SHA-256 Generator",
        "📁 File SHA-256 Generator",
        "📊 Compare Two Files",
        "🌐 DNS Lookup",
        "🔎 Port Scanner",
        "📋 Log Analyzer",
        "🌍 Website Security Scanner",
        "📡 Packet Sniffer",
        "🔒 Password Manager",
        "🛡️ Vulnerability Scanner",
        "🔐 File Encryption Tool",
    ]
)


# ============================================================
# DASHBOARD
# ============================================================

if tool == "🏠 Dashboard":

    st.header("🛡️ Cyber Security Toolkit")

    st.write(
        """
        Welcome to the Cyber Security Toolkit.

        This project combines multiple cybersecurity and
        networking utilities into a single Python application.
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Security Tools", "12")

    with col2:
        st.metric("Programming Language", "Python")

    with col3:
        st.metric("Interface", "Streamlit")

    st.divider()

    st.subheader("Available Tools")

    tools = [
        ("🔐", "Password Strength Checker"),
        ("🔑", "Text SHA-256 Generator"),
        ("📁", "File SHA-256 Generator"),
        ("📊", "Compare Two Files"),
        ("🌐", "DNS Lookup"),
        ("🔎", "Port Scanner"),
        ("📋", "Log Analyzer"),
        ("🌍", "Website Security Scanner"),
        ("📡", "Packet Sniffer"),
        ("🔒", "Password Manager"),
        ("🛡️", "Vulnerability Scanner"),
        ("🔐", "File Encryption Tool"),
    ]

    for icon, name in tools:
        st.write(f"{icon} **{name}**")

    st.divider()

    st.info(
        "⚠️ Use security and network scanning tools only "
        "against systems you own or have explicit permission to test."
    )


# ============================================================
# 1. PASSWORD STRENGTH CHECKER
# ============================================================

elif tool == "🔐 Password Strength Checker":

    st.header("🔐 Password Strength Checker")

    password = st.text_input(
        "Enter Password",
        type="password"
    )

    if st.button("Check Password"):

        if not password:
            st.warning("Please enter a password.")

        else:

            strength = password_checker.check_password(password)

            if strength == "Strong":
                st.success(f"Password Strength: {strength}")

            elif strength == "Medium":
                st.warning(f"Password Strength: {strength}")

            else:
                st.error(f"Password Strength: {strength}")

            if password_checker.common_password(password):
                st.warning(
                    "⚠️ Common password detected!"
                )

            suggestions = password_checker.password_suggestion(
                password
            )

            if suggestions:

                st.subheader("Suggestions")

                for suggestion in suggestions:
                    st.write("• " + suggestion)


# ============================================================
# 2. TEXT SHA-256 GENERATOR
# ============================================================

elif tool == "🔑 Text SHA-256 Generator":

    st.header("🔑 Text SHA-256 Generator")

    text = st.text_area(
        "Enter text",
        height=150
    )

    if st.button("Generate SHA-256"):

        if not text:
            st.warning("Please enter some text.")

        else:

            hash_value = hashlib.sha256(
                text.encode()
            ).hexdigest()

            st.success("SHA-256 Hash Generated")

            st.code(
                hash_value,
                language="text"
            )


# ============================================================
# 3. FILE SHA-256 GENERATOR
# ============================================================

elif tool == "📁 File SHA-256 Generator":

    st.header("📁 File SHA-256 Generator")

    uploaded_file = st.file_uploader(
        "Choose a file"
    )

    if uploaded_file is not None:

        if st.button("Generate File Hash"):

            sha256 = hashlib.sha256()

            while True:

                chunk = uploaded_file.read(4096)

                if not chunk:
                    break

                sha256.update(chunk)

            file_hash = sha256.hexdigest()

            st.success("File SHA-256 Generated")

            st.code(
                file_hash,
                language="text"
            )


# ============================================================
# 4. COMPARE TWO FILES
# ============================================================

elif tool == "📊 Compare Two Files":

    st.header("📊 Compare Two Files")

    file1 = st.file_uploader(
        "Upload First File",
        key="compare_file_1"
    )

    file2 = st.file_uploader(
        "Upload Second File",
        key="compare_file_2"
    )

    if file1 is not None and file2 is not None:

        if st.button("Compare Files"):

            hash1 = hashlib.sha256(
                file1.getvalue()
            ).hexdigest()

            hash2 = hashlib.sha256(
                file2.getvalue()
            ).hexdigest()

            st.subheader("File Hashes")

            col1, col2 = st.columns(2)

            with col1:
                st.write("**First File**")
                st.code(hash1)

            with col2:
                st.write("**Second File**")
                st.code(hash2)

            if hash1 == hash2:
                st.success(
                    "✅ Files are identical."
                )
            else:
                st.error(
                    "❌ Files are different."
                )


# ============================================================
# 5. DNS LOOKUP
# ============================================================

elif tool == "🌐 DNS Lookup":

    st.header("🌐 DNS Lookup")

    domain = st.text_input(
        "Enter Domain",
        placeholder="example.com"
    )

    if st.button("Lookup DNS"):

        if not domain:
            st.warning("Please enter a domain.")

        else:

            try:

                ip = dns_lookup.lookup(domain)
                hostname = dns_lookup.get_hostname()

                st.subheader("DNS Information")

                col1, col2 = st.columns(2)

                with col1:
                    st.write("**Computer Hostname**")
                    st.code(hostname)

                with col2:
                    st.write("**Domain IP Address**")
                    st.code(ip)

            except Exception as error:

                st.error(
                    f"DNS lookup failed: {error}"
                )


# ============================================================
# 6. PORT SCANNER
# ============================================================

elif tool == "🔎 Port Scanner":

    st.header("🔎 Port Scanner")

    st.warning(
        "Only scan systems you own or have explicit "
        "permission to test."
    )

    host = st.text_input(
        "Enter Host",
        placeholder="example.com"
    )

    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        443: "HTTPS"
    }

    selected_ports = st.multiselect(
        "Select Ports",
        list(common_ports.keys()),
        default=[22, 80, 443]
    )

    if st.button("Scan Ports"):

        if not host:
            st.warning("Please enter a host.")

        elif not selected_ports:
            st.warning("Select at least one port.")

        else:

            results = []

            with st.spinner("Scanning..."):

                for port in selected_ports:

                    status = port_scanner.scan_port(
                        host,
                        port
                    )

                    results.append(
                        {
                            "Port": port,
                            "Service": common_ports[port],
                            "Status": status
                        }
                    )

            st.subheader("Scan Results")

            st.dataframe(
                results,
                use_container_width=True
            )


# ============================================================
# 7. LOG ANALYZER
# ============================================================

elif tool == "📋 Log Analyzer":

    st.header("📋 Log Analyzer")

    uploaded_log = st.file_uploader(
        "Upload a log file",
        type=["txt", "log"]
    )

    if uploaded_log is not None:

        if st.button("Analyze Log"):

            text = uploaded_log.getvalue().decode(
                "utf-8",
                errors="ignore"
            )

            info = 0
            warning = 0
            error = 0

            for line in text.splitlines():

                if "INFO" in line:
                    info += 1

                elif "WARNING" in line:
                    warning += 1

                elif "ERROR" in line:
                    error += 1

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("INFO", info)

            with col2:
                st.metric("WARNING", warning)

            with col3:
                st.metric("ERROR", error)

            st.subheader("Log Preview")

            st.text_area(
                "Content",
                text,
                height=250
            )


# ============================================================
# 8. WEBSITE SECURITY SCANNER
# ============================================================

elif tool == "🌍 Website Security Scanner":

    st.header("🌍 Website Security Scanner")

    st.warning(
        "Scan only websites you own or have permission to test."
    )

    url = st.text_input(
        "Website URL",
        placeholder="https://example.com"
    )

    if st.button("Scan Website"):

        if not url:
            st.warning("Please enter a website URL.")

        else:

            with st.spinner("Scanning website..."):

                result = website_scanner.scan_website(
                    url
                )

            if isinstance(result, dict):

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Status Code",
                        result["Status Code"]
                    )

                    st.write(
                        "**Server:**",
                        result["Server"]
                    )

                with col2:

                    st.write(
                        "**Content Type:**",
                        result["Content Type"]
                    )

                st.subheader("Security Headers")

                headers = result[
                    "Security Headers"
                ]

                for header, status in headers.items():

                    if status == "Present":
                        st.success(
                            f"✅ {header}: Present"
                        )

                    else:
                        st.warning(
                            f"⚠️ {header}: Missing"
                        )

            else:

                st.error(result)


# ============================================================
# 9. PACKET SNIFFER
# ============================================================

elif tool == "📡 Packet Sniffer":

    st.header("📡 Packet Sniffer")

    st.warning(
        "Packet capture requires appropriate permissions "
        "and network access. This feature is intended for "
        "authorized/local testing."
    )

    st.info(
        "The original packet sniffer uses Scapy and captures "
        "packets from the machine where it is running."
    )

    st.code(
        "packet_sniffer.start_sniffer()",
        language="python"
    )

    st.write(
        "For security reasons and cloud compatibility, "
        "run the original packet sniffer locally from "
        "the CLI version using:"
    )

    st.code(
        "python main.py",
        language="bash"
    )


# ============================================================
# 10. PASSWORD MANAGER
# ============================================================

elif tool == "🔒 Password Manager":

    st.header("🔒 Password Manager")

    st.warning(
        "This demonstration stores encrypted passwords "
        "using your existing Fernet-based password manager."
    )

    manager_action = st.selectbox(
        "Select Action",
        [
            "Add Password",
            "View Passwords",
            "Search Password",
            "Delete Password"
        ]
    )

    # ---------------- ADD PASSWORD ----------------

    if manager_action == "Add Password":

        website = st.text_input(
            "Website",
            placeholder="example.com"
        )

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Save Password"):

            if not website or not username or not password:

                st.warning(
                    "Please fill all fields."
                )

            else:

                try:

                    password_manager.generate_key()

                    password_manager.save_password(
                        website,
                        username,
                        password
                    )

                    st.success(
                        "Password saved successfully."
                    )

                except Exception as error:

                    st.error(
                        f"Unable to save password: {error}"
                    )

    # ---------------- VIEW PASSWORDS ----------------

    elif manager_action == "View Passwords":

        st.info(
            "For security, passwords are not displayed "
            "in the web interface."
        )

        st.write(
            "Use the original CLI Password Manager "
            "for local password viewing."
        )

    # ---------------- SEARCH PASSWORD ----------------

    elif manager_action == "Search Password":

        website = st.text_input(
            "Website to Search"
        )

        if st.button("Search"):

            if not website:

                st.warning(
                    "Enter a website."
                )

            else:

                st.info(
                    "Use the local CLI password manager "
                    "to retrieve stored credentials."
                )

    # ---------------- DELETE PASSWORD ----------------

    elif manager_action == "Delete Password":

        website = st.text_input(
            "Website to Delete"
        )

        if st.button("Delete Password"):

            if not website:

                st.warning(
                    "Enter a website."
                )

            else:

                try:

                    password_manager.delete_password(
                        website
                    )

                    st.success(
                        "Delete operation completed."
                    )

                except Exception as error:

                    st.error(
                        f"Unable to delete password: {error}"
                    )


# ============================================================
# 11. VULNERABILITY SCANNER
# ============================================================

elif tool == "🛡️ Vulnerability Scanner":

    st.header("🛡️ Vulnerability Scanner")

    st.warning(
        "Only scan systems you own or have explicit "
        "authorization to test."
    )

    host = st.text_input(
        "Enter Host",
        placeholder="example.com"
    )

    col1, col2 = st.columns(2)

    with col1:

        start_port = st.number_input(
            "Start Port",
            min_value=1,
            max_value=65535,
            value=20
        )

    with col2:

        end_port = st.number_input(
            "End Port",
            min_value=1,
            max_value=65535,
            value=100
        )

    if st.button("Start Vulnerability Scan"):

        if not host:

            st.warning(
                "Please enter a host."
            )

        elif start_port > end_port:

            st.error(
                "Start port must be less than or equal "
                "to end port."
            )

        else:

            with st.spinner(
                "Scanning authorized target..."
            ):

                try:

                    open_ports = (
                        vulnerability_scanner.scan_host(
                            host,
                            int(start_port),
                            int(end_port)
                        )
                    )

                    if open_ports:

                        st.subheader(
                            "Open Ports Found"
                        )

                        results = []

                        for port, service in open_ports:

                            results.append(
                                {
                                    "Port": port,
                                    "Service": service,
                                    "Status": "Open"
                                }
                            )

                        st.dataframe(
                            results,
                            use_container_width=True
                        )

                        st.success(
                            f"{len(open_ports)} open port(s) found."
                        )

                    else:

                        st.info(
                            "No open ports found."
                        )

                except Exception as error:

                    st.error(
                        f"Scan failed: {error}"
                    )


# ============================================================
# 12. FILE ENCRYPTION TOOL
# ============================================================

elif tool == "🔐 File Encryption Tool":

    st.header("🔐 File Encryption Tool")

    st.info(
        "Files are encrypted using Fernet symmetric encryption."
    )

    encryption_action = st.radio(
        "Select Action",
        [
            "Encrypt File",
            "Decrypt File"
        ]
    )

    # ---------------- ENCRYPT ----------------

    if encryption_action == "Encrypt File":

        uploaded_file = st.file_uploader(
            "Choose a file to encrypt",
            key="encrypt_file"
        )

        if uploaded_file is not None:

            if st.button("Encrypt File"):

                try:

                    file_encryption.generate_key()

                    key = file_encryption.load_key()

                    from cryptography.fernet import Fernet

                    cipher = Fernet(key)

                    original_data = (
                        uploaded_file.getvalue()
                    )

                    encrypted_data = cipher.encrypt(
                        original_data
                    )

                    encrypted_filename = (
                        uploaded_file.name + ".enc"
                    )

                    st.success(
                        "File encrypted successfully."
                    )

                    st.download_button(
                        label="⬇️ Download Encrypted File",
                        data=encrypted_data,
                        file_name=encrypted_filename,
                        mime="application/octet-stream"
                    )

                except Exception as error:

                    st.error(
                        f"Encryption failed: {error}"
                    )

    # ---------------- DECRYPT ----------------

    else:

        uploaded_file = st.file_uploader(
            "Choose an encrypted .enc file",
            type=["enc"],
            key="decrypt_file"
        )

        if uploaded_file is not None:

            if st.button("Decrypt File"):

                try:

                    file_encryption.generate_key()

                    key = file_encryption.load_key()

                    from cryptography.fernet import Fernet

                    cipher = Fernet(key)

                    encrypted_data = (
                        uploaded_file.getvalue()
                    )

                    decrypted_data = cipher.decrypt(
                        encrypted_data
                    )

                    filename = uploaded_file.name

                    if filename.endswith(".enc"):
                        filename = filename[:-4]

                    st.success(
                        "File decrypted successfully."
                    )

                    st.download_button(
                        label="⬇️ Download Decrypted File",
                        data=decrypted_data,
                        file_name=filename,
                        mime="application/octet-stream"
                    )

                except Exception as error:

                    st.error(
                        "Decryption failed. Make sure "
                        "the file was encrypted with the "
                        "same encryption key."
                    )