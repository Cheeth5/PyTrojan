# PyTrojan
Overview

Google Login Simulator is an educational tool designed to demonstrate the potential dangers of internet security threats, such as Trojans. This application mimics a Google login interface, capturing user credentials and IP addresses to illustrate how easily sensitive information can be exploited.
Key Features

    Realistic UI: The interface mimics the Google login page, providing a familiar look and feel.
    Credential Capture: Users input their email and password, simulating a login process.
    IP Address Logging: The application captures the user's local IP address.
    Data Transmission: Captured data (credentials and IP address) is sent to a specified Discord server using a webhook for educational purposes.
    Educational Purpose: The application is designed to educate users about the importance of internet security and the risks of sharing personal information online.

Installation

    Clone the Repository:
    git clone https://github.com/yourusername/google-login-simulator.git
    cd google-login-simulator

Set Up a Virtual Environment:

    python3 -m venv myenv
    source myenv/bin/activate

Install Dependencies:



    pip install -r requirements.txt

Usage

Run the Application:


    python main.py

Enter Credentials:

    Input your email or phone and password in the respective fields.
    Click the "Next" button to submit the information.

View Status:

    The status label will indicate whether the information was sent successfully or if there was an error.

Educational Purpose

This application is intended solely for educational purposes. It aims to raise awareness about how easily sensitive information can be captured and transmitted without the user’s knowledge. Always be cautious about where and how personal information is shared online.
Disclaimer

Important: This application is for educational use only. Unauthorized use of this software for malicious purposes is strictly prohibited and may be illegal. Use this tool responsibly and with appropriate permissions.
Technical Details

    Language: Python
    Libraries: Tkinter, Requests, Pillow, Socket
    Platform: Linux

Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.
License

This project is licensed under the MIT License - see the LICENSE file for details.
