import psutil


def list_open_ports():
    print("Listing all open ports on the system:")
    try:
        print("PID, Laddr, Status")
        # List all open ports
        for conn in psutil.net_connections(kind='inet'):
            print(f"PID: {conn.pid}, Laddr: {conn.laddr}, Status: {conn.status}")
    except PermissionError:
        print("PermissionError: You may need to run this script with elevated privileges (e.g., as an administrator).")


list_open_ports()
