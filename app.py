"""
Cyber Security Toolkit - Streamlit Web Interface

Author:
    Macharla Harshith Goud

Description:
    A web-based cybersecurity toolkit containing:
    1. Password Strength Checker
    2. Text SHA-256 Generator
    3. File SHA-256 Generator
    4. Compare Two Files
    5. DNS Lookup
    6. Port Scanner
    7. Log Analyzer
    8. Website Security Scanner
    9. Packet Sniffer
    10. Password Manager
    11. Vulnerability Scanner
    12. File Encryption Tool
"""

import os
import tempfile
import streamlit as st

# Local modules
import password_checker
import hash_generator
import dns_lookup
import port_scanner
import log_analyzer
import website_scanner
import packet_sniffer
import password_manager
import vulnerability_scanner
import file_encryption


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Cyber Security Toolkit",
    page_icon="🔐",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #0e1117;
    }

    .tool-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #30363d;
        margin-bottom: 15px;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #9ca3af;
        margin-bottom: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🔐 Cyber Security Toolkit")

st.sidebar.markdown("---")

tool = st.sidebar.radio(
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
        "🔐 File Encryption Tool"
    ]
)


# ============================================================
# DASHBOARD
# ============================================================

if tool == "🏠 Dashboard":

    st.markdown(
        '<div class="title">🔐 Cyber Security Toolkit</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'A modular Python-based cybersecurity toolkit'
        '</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Select a cybersecurity tool from the sidebar to get started."
    )

    st.markdown("## 🛠️ Available Tools")

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
        ("🔐", "File Encryption Tool")
    ]

    columns = st.columns(3)

    for index, (icon, name) in enumerate(tools):

        with columns[index % 3]:

            st.markdown(
                f"""
                <div class="tool-card">
                    <h3>{icon} {name}</h3>
                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# 1. PASSWORD STRENGTH CHECKER
# ============================================================

elif tool == "🔐 Password Strength Checker":

    st.title("🔐 Password Strength Checker")

    password = st.text_input(
        "Enter Password",
        type="password"
    )

    if st.button("Check Password"):

        if password:

            strength = password_checker.check_password(password)

            if strength == "Strong":
                st.success(f"Password Strength: {strength}")

            elif strength == "Medium":
                st.warning(f"Password Strength: {strength}")

            else:
                st.error(f"Password Strength: {strength}")

            if password_checker.common_password(password):

                st.error(
                    "⚠️ Warning: Common password detected!"
                )

            suggestions = password_checker.password_suggestion(
                password
            )

            if suggestions:

                st.subheader("Suggestions")

                for suggestion in suggestions:
                    st.write("•", suggestion)

        else:

            st.warning("Please enter a password.")


# ============================================================
# 2. TEXT SHA-256 GENERATOR
# ============================================================

elif tool == "🔑 Text SHA-256 Generator":

    st.title("🔑 Text SHA-256 Generator")

    text = st.text_area("Enter text")

    if st.button("Generate SHA-256"):

        if text:

            result = hash_generator.generate_hash(text)

            st.subheader("SHA-256 Hash")

            st.code(result)

        else:

            st.warning("Please enter some text.")


# ============================================================
# 3. FILE SHA-256 GENERATOR
# ============================================================

elif tool == "📁 File SHA-256 Generator":

    st.title("📁 File SHA-256 Generator")

    uploaded_file = st.file_uploader(
        "Upload a file",
        type=None
    )

    if uploaded_file is not None:

        if st.button("Generate File Hash"):

            try:

                with tempfile.NamedTemporaryFile(
                    delete=False
                ) as temp_file:

                    temp_file.write(
                        uploaded_file.getbuffer()
                    )

                    temp_filename = temp_file.name

                result = hash_generator.generate_file_hash(
                    temp_filename
                )

                os.remove(temp_filename)

                st.subheader("SHA-256 Hash")

                st.code(result)

            except Exception as error:

                st.error(f"Error: {error}")


# ============================================================
# 4. COMPARE TWO FILES
# ============================================================

elif tool == "📊 Compare Two Files":

    st.title("📊 Compare Two Files")

    file1 = st.file_uploader(
        "Upload First File",
        type=None,
        key="file1"
    )

    file2 = st.file_uploader(
        "Upload Second File",
        type=None,
        key="file2"
    )

    if file1 is not None and file2 is not None:

        if st.button("Compare Files"):

            try:

                temp1 = tempfile.NamedTemporaryFile(
                    delete=False
                )

                temp1.write(file1.getbuffer())
                temp1.close()

                temp2 = tempfile.NamedTemporaryFile(
                    delete=False
                )

                temp2.write(file2.getbuffer())
                temp2.close()

                result = hash_generator.common_hash(
                    temp1.name,
                    temp2.name
                )

                os.remove(temp1.name)
                os.remove(temp2.name)

                if "Identical" in result:

                    st.success(result)

                else:

                    st.warning(result)

            except Exception as error:

                st.error(f"Error: {error}")


# ============================================================
# 5. DNS LOOKUP
# ============================================================

elif tool == "🌐 DNS Lookup":

    st.title("🌐 DNS Lookup")

    domain = st.text_input(
        "Enter Domain Name",
        placeholder="example.com"
    )

    if st.button("Lookup"):

        if domain:

            hostname = dns_lookup.get_hostname()

            ip = dns_lookup.lookup(domain)

            st.write(
                "**Computer Hostname:**",
                hostname
            )

            st.write(
                "**Domain:**",
                domain
            )

            st.write(
                "**IP Address:**",
                ip
            )

        else:

            st.warning("Please enter a domain.")


# ============================================================
# 6. PORT SCANNER
# ============================================================

elif tool == "🔎 Port Scanner":

    st.title("🔎 Port Scanner")

    host = st.text_input(
        "Enter Host",
        placeholder="127.0.0.1"
    )

    if st.button("Scan Ports"):

        if host:

            services = {
                21: "FTP",
                22: "SSH",
                23: "Telnet",
                25: "SMTP",
                53: "DNS",
                80: "HTTP",
                443: "HTTPS"
            }

            ports = [
                21,
                22,
                23,
                25,
                53,
                80,
                443
            ]

            st.write("### Scan Results")

            for port in ports:

                result = port_scanner.scan_port(
                    host,
                    port
                )

                st.write(
                    f"**{port} - "
                    f"{services.get(port, 'Unknown')}** : "
                    f"{result}"
                )

        else:

            st.warning("Please enter a host.")


# ============================================================
# 7. LOG ANALYZER
# ============================================================

elif tool == "📋 Log Analyzer":

    st.title("📋 Log Analyzer")

    uploaded_log = st.file_uploader(
        "Upload Log File",
        type=["txt", "log"]
    )

    if uploaded_log is not None:

        if st.button("Analyze Log"):

            try:

                with tempfile.NamedTemporaryFile(
                    mode="wb",
                    delete=False
                ) as temp_file:

                    temp_file.write(
                        uploaded_log.getbuffer()
                    )

                    temp_filename = temp_file.name

                info, warning, error = (
                    log_analyzer.analyze_log(
                        temp_filename
                    )
                )

                os.remove(temp_filename)

                st.subheader("Log Analysis Report")

                col1, col2, col3 = st.columns(3)

                col1.metric("INFO", info)
                col2.metric("WARNING", warning)
                col3.metric("ERROR", error)

            except Exception as error_message:

                st.error(
                    f"Error: {error_message}"
                )


# ============================================================
# 8. WEBSITE SECURITY SCANNER
# ============================================================

elif tool == "🌍 Website Security Scanner":

    st.title("🌍 Website Security Scanner")

    url = st.text_input(
        "Enter Website URL",
        placeholder="https://example.com"
    )

    if st.button("Scan Website"):

        if url:

            result = website_scanner.scan_website(url)

            if isinstance(result, dict):

                st.subheader("Website Scan Report")

                st.write(
                    "**Status Code:**",
                    result["Status Code"]
                )

                st.write(
                    "**Server:**",
                    result["Server"]
                )

                st.write(
                    "**Content Type:**",
                    result["Content Type"]
                )

                st.subheader("Security Headers")

                for header, status in (
                    result["Security Headers"].items()
                ):

                    if status == "Present":

                        st.success(
                            f"{header}: {status}"
                        )

                    else:

                        st.warning(
                            f"{header}: {status}"
                        )

            else:

                st.error(result)

        else:

            st.warning("Please enter a website URL.")


# ============================================================
# 9. PACKET SNIFFER
# ============================================================

elif tool == "📡 Packet Sniffer":

    st.title("📡 Packet Sniffer")

    st.warning(
        "Packet sniffing may require administrator/root "
        "permissions and may not work on cloud hosting."
    )

    packet_count = st.number_input(
        "Number of packets",
        min_value=1,
        max_value=20,
        value=5
    )

    if st.button("Start Packet Capture"):

        st.info(
            f"Capturing {packet_count} packets..."
        )

        try:

            packet_sniffer.sniff(
                prn=packet_sniffer.packet_callback,
                count=packet_count,
                store=False
            )

            st.success(
                "Packet capture completed."
            )

        except Exception as error:

            st.error(
                f"Packet capture failed: {error}"
            )


# ============================================================
# 10. PASSWORD MANAGER
# ============================================================

elif tool == "🔒 Password Manager":

    st.title("🔒 Password Manager")

    st.warning(
        "For a public deployment, use dummy credentials only. "
        "Do not store real passwords on a shared demo server."
    )

    manager_option = st.selectbox(
        "Select Operation",
        [
            "Add Password",
            "View Passwords",
            "Search Password",
            "Delete Password"
        ]
    )

    if manager_option == "Add Password":

        website = st.text_input("Website")
        username = st.text_input("Username")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Save Password"):

            if website and username and password:

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
                        f"Error: {error}"
                    )

            else:

                st.warning(
                    "Please fill all fields."
                )

    elif manager_option == "View Passwords":

        if st.button("View Saved Passwords"):

            try:

                password_manager.generate_key()

                if not os.path.exists(
                    password_manager.PASSWORD_FILE
                ):

                    st.info(
                        "No passwords saved."
                    )

                else:

                    with open(
                        password_manager.PASSWORD_FILE,
                        "r"
                    ) as file:

                        import json

                        data = json.load(file)

                    if not data:

                        st.info(
                            "No passwords saved."
                        )

                    else:

                        for account in data:

                            st.write(
                                "**Website:**",
                                account["website"]
                            )

                            st.write(
                                "**Username:**",
                                account["username"]
                            )

                            decrypted = (
                                password_manager.decrypt_password(
                                    account["password"]
                                )
                            )

                            st.write(
                                "**Password:**",
                                decrypted
                            )

                            st.markdown("---")

            except Exception as error:

                st.error(
                    f"Error: {error}"
                )

    elif manager_option == "Search Password":

        website = st.text_input(
            "Enter Website"
        )

        if st.button("Search"):

            if website:

                try:

                    password_manager.generate_key()

                    found = False

                    if os.path.exists(
                        password_manager.PASSWORD_FILE
                    ):

                        import json

                        with open(
                            password_manager.PASSWORD_FILE,
                            "r"
                        ) as file:

                            data = json.load(file)

                        for account in data:

                            if (
                                account["website"].lower()
                                == website.lower()
                            ):

                                st.success(
                                    "Password Found"
                                )

                                st.write(
                                    "**Website:**",
                                    account["website"]
                                )

                                st.write(
                                    "**Username:**",
                                    account["username"]
                                )

                                st.write(
                                    "**Password:**",
                                    password_manager.decrypt_password(
                                        account["password"]
                                    )
                                )

                                found = True
                                break

                    if not found:

                        st.warning(
                            "Website not found."
                        )

                except Exception as error:

                    st.error(
                        f"Error: {error}"
                    )

    elif manager_option == "Delete Password":

        website = st.text_input(
            "Website to Delete"
        )

        if st.button("Delete Password"):

            if website:

                try:

                    password_manager.delete_password(
                        website
                    )

                    st.success(
                        "Delete operation completed."
                    )

                except Exception as error:

                    st.error(
                        f"Error: {error}"
                    )


# ============================================================
# 11. VULNERABILITY SCANNER
# ============================================================

elif tool == "🛡️ Vulnerability Scanner":

    st.title("🛡️ Vulnerability Scanner")

    st.warning(
        "Only scan systems that you own or have "
        "explicit permission to test."
    )

    host = st.text_input(
        "Target Host",
        placeholder="127.0.0.1"
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
                "Please enter a target host."
            )

        elif start_port > end_port:

            st.error(
                "Start port must be less than "
                "or equal to end port."
            )

        else:

            try:

                ports = vulnerability_scanner.scan_host(
                    host,
                    int(start_port),
                    int(end_port)
                )

                st.subheader("Scan Results")

                if ports:

                    for port, service in ports:

                        st.success(
                            f"Port {port} - "
                            f"{service} - OPEN"
                        )

                    st.write(
                        f"Total Open Ports: {len(ports)}"
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

    st.title("🔐 File Encryption Tool")

    st.write(
        "Encrypt and decrypt files using "
        "Fernet symmetric encryption."
    )

    operation = st.selectbox(
        "Select Operation",
        [
            "Generate Encryption Key",
            "Encrypt File",
            "Decrypt File"
        ]
    )


    # --------------------------------------------------------
    # GENERATE KEY
    # --------------------------------------------------------

    if operation == "Generate Encryption Key":

        if st.button("Generate Key"):

            try:

                file_encryption.create_folders()

                file_encryption.generate_key()

                st.success(
                    "Encryption key generated successfully."
                )

            except Exception as error:

                st.error(
                    f"Error: {error}"
                )


    # --------------------------------------------------------
    # ENCRYPT FILE
    # --------------------------------------------------------

    elif operation == "Encrypt File":

        uploaded_file = st.file_uploader(
            "Upload file to encrypt",
            type=None,
            key="encrypt_upload"
        )

        if uploaded_file is not None:

            if st.button("Encrypt File"):

                try:

                    file_encryption.create_folders()

                    file_encryption.generate_key()

                    input_path = os.path.join(
                        "files",
                        uploaded_file.name
                    )

                    with open(
                        input_path,
                        "wb"
                    ) as file:

                        file.write(
                            uploaded_file.getbuffer()
                        )

                    key = file_encryption.load_key()

                    if key is None:

                        st.error(
                            "Encryption key not found."
                        )

                    else:

                        from cryptography.fernet import Fernet

                        cipher = Fernet(key)

                        with open(
                            input_path,
                            "rb"
                        ) as file:

                            data = file.read()

                        encrypted_data = cipher.encrypt(
                            data
                        )

                        output_path = os.path.join(
                            "encrypted",
                            uploaded_file.name
                            + ".encrypted"
                        )

                        with open(
                            output_path,
                            "wb"
                        ) as file:

                            file.write(
                                encrypted_data
                            )

                        st.success(
                            "File encrypted successfully!"
                        )

                        st.download_button(
                            label="⬇️ Download Encrypted File",
                            data=encrypted_data,
                            file_name=(
                                uploaded_file.name
                                + ".encrypted"
                            ),
                            mime="application/octet-stream"
                        )

                except Exception as error:

                    st.error(
                        f"Encryption failed: {error}"
                    )


    # --------------------------------------------------------
    # DECRYPT FILE
    # --------------------------------------------------------

    elif operation == "Decrypt File":

        encrypted_file = st.file_uploader(
            "Upload encrypted file",
            type=None,
            key="decrypt_upload"
        )

        if encrypted_file is not None:

            if st.button("Decrypt File"):

                try:

                    file_encryption.create_folders()

                    key = file_encryption.load_key()

                    if key is None:

                        st.error(
                            "Encryption key not found."
                        )

                    else:

                        from cryptography.fernet import Fernet

                        cipher = Fernet(key)

                        encrypted_data = (
                            encrypted_file.getbuffer()
                        )

                        decrypted_data = cipher.decrypt(
                            encrypted_data
                        )

                        original_filename = (
                            encrypted_file.name
                            .replace(
                                ".encrypted",
                                ""
                            )
                        )

                        output_path = os.path.join(
                            "decrypted",
                            original_filename
                        )

                        with open(
                            output_path,
                            "wb"
                        ) as file:

                            file.write(
                                decrypted_data
                            )

                        st.success(
                            "File decrypted successfully!"
                        )

                        st.download_button(
                            label="⬇️ Download Decrypted File",
                            data=decrypted_data,
                            file_name=original_filename,
                            mime="application/octet-stream"
                        )

                except Exception as error:

                    st.error(
                        "Decryption failed. "
                        "Make sure the file was encrypted "
                        "using the same encryption key."
                    )