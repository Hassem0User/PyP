import logging

import psutil


def list_open_ports():
    logging.info("Listing all open ports on the system:")
    try:
        logging.info("PID, Laddr, Status")
        # List all open ports
        for conn in psutil.net_connections(kind='inet'):
            logging.info("PID: %(conn.pid)s, Laddr: %(conn.laddr)s, Status: %(conn.status)s"
                         % {"conn.pid": conn.pid, "conn.laddr": conn.laddr, "conn.status": conn.status}
                         )
    except PermissionError:
        logging.info("PermissionError: You may need to run this script with elevated privileges (e.g., as an administrator).")


list_open_ports()
