import platform
import psutil
import os

def display_system_info():
    print("System Information")
    print("=" * 40)
    
    # OS information
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Platform: {platform.platform()}")
    print(f"Processor: {platform.processor()}")
    
    # Memory information
    mem = psutil.virtual_memory()
    print(f"Total Memory: {mem.total / (1024 ** 3):.2f} GB")
    print(f"Available Memory: {mem.available / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {mem.used / (1024 ** 3):.2f} GB")
    
    # CPU information
    print(f"CPU Count: {psutil.cpu_count(logical=True)} cores")
    print(f"CPU Frequency: {psutil.cpu_freq().current} MHz")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    
    # Disk information
    disk = psutil.disk_usage('/')
    print(f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB")
    print(f"Used Disk Space: {disk.used / (1024 ** 3):.2f} GB")
    print(f"Free Disk Space: {disk.free / (1024 ** 3):.2f} GB")
    
    # Network information
    net = psutil.net_if_addrs()
    print(f"Network Interfaces: {', '.join(net.keys())}")


display_system_info()
input()
exit()
