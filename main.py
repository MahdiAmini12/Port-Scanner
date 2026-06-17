import argparse
import socket
from time import sleep

parser = argparse.ArgumentParser(description="Simple Port Scanner")

parser.add_argument("target", help="Enter target hostname")
parser.add_argument("port", type=int, nargs='+', help="Enter one or more Ports")

args = parser.parse_args()

try:
    hostbyname = socket.gethostbyname(args.target)
except socket.gaierror:
    print("[!] Could not resolve hostname")
    exit()

print(f"Target : {args.target}")
print(f"IP     : {hostbyname}")

for port in args.port:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((hostbyname, port))

        if result == 0:
            print(f"[+] Port {port} : OPEN")
        else:
            print(f"[-] Port {port} : CLOSED")

    except socket.error as e:
        print(f"[!] Error scanning port {port}: {e}")

    
    