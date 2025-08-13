import socket
import time

# Map of common ports to services
common_ports = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

def scan_port(ip, port):
    """Try to connect to a port and return if it's open."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # half a second timeout
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:  # port is open
            service = common_ports.get(port, "Unknown Service")
            print(f"[+] Port {port} ({service}) is OPEN")
        sock.close()
    except socket.error:
        pass

def main():
    target = input("Enter target IP or domain: ").strip()
    
    # Resolve domain to IP if needed
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid target.")
        return

    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")
    start_time = time.time()

    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

    end_time = time.time()
    print(f"\nScan completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()
