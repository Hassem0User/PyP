import logging
import socket
import sys


def check_port_open(port):
    try:
        socket.socket().connect(('localhost', port))
        logging.info("The port %(port)s is opened." % {"port": port})
        return True
    except ConnectionRefusedError:
        return False


def open_port(port):
    try:
        logging.info("Opening port %(port)s" % {"port": port})
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.info("Linking socket to port %(port)s" % {"port": port})
        server_socket.bind(('0.0.0.0', port))
        logging.info("Listening connections to port %(port)s" % {"port": port})
        server_socket.listen(5)
        logging.info("Waiting connections to port %(port)s" % {"port": port})
        return server_socket
    except PermissionError:
        sys.exit("You need admin permissions.")


port = 8080

if check_port_open(port):
    logging.info("The port %(port)s is already open." % {"port": port})
else:
    logging.info("The port %(port)s is closed." % {"port": port})
    server_socket = open_port(port)
    logging.info("The port %(port)s has been open succesfully." % {"port": port})
    client_socket = None
    client_address = None

    try:
        server_socket.settimeout(60)  # Max wait time

        client_socket, client_address = server_socket.accept()
        logging.info("Connected from %(client_address)s" % {"client_address": client_address})

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            logging.info("Received: %(data.decode)s('utf-8')" % {"data.decode": data.decode})
            client_socket.send(data)

    except socket.timeout:
        logging.info("Timeout expired. No connection has been received.")
    except KeyboardInterrupt:
        logging.info("User interruption. Closing the server")
    finally:
        if client_socket:
            client_socket.close()
        server_socket.close()
        logging.info("Server Closed.")
