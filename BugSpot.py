import os
import subprocess
import time
import sys

def show_banner():
    banner = """
 ____  _   _  ____ ____  ____   ___ _____ 
| __ )| | | |/ ___/ ___||  _ \ / _ \_   _|
|  _ \| | | | |  _\___ \| |_) | | | || |  
| |_) | |_| | |_| |___) |  __/| |_| || |  
|____/ \___/ \____|____/|_|    \___/ |_|  
                                          

    """
    print(banner)

def subdomain_enum(domain):
    print("[+] Running subdomain enumeration...")
    subprocess.run(["subfinder", "-d", domain])

def port_scan(domain):
    print("[+] Running port scan...")
    subprocess.run(["nmap", "-sV", domain])

def directory_bruteforce(domain):
    print("[+] Running directory brute-force...")
    subprocess.run(["ffuf", "-u", f"http://{domain}/FUZZ", "-w", "/usr/share/wordlists/dirb/common.txt"])  

def sql_injection_scan(domain):
    print("[+] Testing for SQL Injection...")
    # Dummy implementation, replace with an actual scanner
    print(f"[*] Scanning {domain} for SQL Injection vulnerabilities...")
    time.sleep(2)
    print("[-] No SQL Injection found (mock result)")

def xss_scan(domain):
    print("[+] Testing for XSS...")
    # Dummy implementation, replace with an actual scanner
    print(f"[*] Scanning {domain} for XSS vulnerabilities...")
    time.sleep(2)
    print("[-] No XSS found (mock result)")

def os_injection_scan(domain):
    print("[+] Testing for OS Command Injection...")
    # Dummy implementation, replace with an actual scanner
    print(f"[*] Scanning {domain} for OS Injection vulnerabilities...")
    time.sleep(2)
    print("[-] No OS Injection found (mock result)")

def main():
    show_banner()
    domain = input("Enter target domain: ")
    
    while True:
        print("\nSelect an option:")
        print("1. Subdomain Enumeration")
        print("2. Port Scanning")
        print("3. Directory Brute-force")
        print("4. SQL Injection Test")
        print("5. XSS Test")
        print("6. OS Command Injection Test")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            subdomain_enum(domain)
        elif choice == "2":
            port_scan(domain)
        elif choice == "3":
            directory_bruteforce(domain)
        elif choice == "4":
            sql_injection_scan(domain)
        elif choice == "5":
            xss_scan(domain)
        elif choice == "6":
            os_injection_scan(domain)
        elif choice == "7":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
