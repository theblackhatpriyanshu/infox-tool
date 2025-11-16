import os
import platform
import requests

def banner():
    print("""
===================================
        INFOX - TOOL V1.0
===================================
    """)

def ip_info():
    ip = input("Enter IP Address: ")
    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url)
        data = response.json()

        print("\n--- IP PUBLIC INFO ---")
        for key, value in data.items():
            print(f"{key}: {value}")

    except:
        print("Error: Unable to fetch IP info.")

def device_info():
    print("\n--- DEVICE INFO ---")
    print("System:", platform.system())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())
    print("Platform:", platform.platform())

def network_info():
    print("\n--- NETWORK INFO ---")
    os.system("ifconfig || ip a")

def main():
    banner()
    print("1. IP Info")
    print("2. Device Info")
    print("3. Network Info")

    choice = input("Enter your choice: ")

    if choice == "1":
        ip_info()
    elif choice == "2":
        device_info()
    elif choice == "3":
        network_info()
    else:
        print("Invalid Option!")

if __name__ == "__main__":
    main()
