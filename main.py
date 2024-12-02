from scanner.scanner import scan_port 
from scanner.utils import display_banner 
from concurrent.futures import ThreadPoolExecutor

def port_scanner():
    display_banner()
    target = input("Enter the target IP address or hostname: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    print(f"Scanning {target}...\n")
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_single_port, target, port)

def scan_single_port(ip, port):
    if scan_port(ip, port):
        print(f"[+] Port {port} is open")

if __name__ == "__main__":
    port_scanner()
