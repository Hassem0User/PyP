import socket
import sys


def check_port_open(port):
    try:
        socket.socket().connect(('localhost', port))
        print(f"The port {port} is opened.")
        return True
    except ConnectionRefusedError:
        return False


def open_port(port):
    try:
        print(f"Opening port {port}")
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Linking socket to port {port}")
        server_socket.bind(('0.0.0.0', port))
        print(f"Listening connections to port {port}")
        server_socket.listen(5)
        print(f"Waiting connections to port {port}")
        return server_socket
    except PermissionError:
        sys.exit("You need admin permissions.")


port = 8080

if check_port_open(port):
    print(f"The port {port} is already open.")
else:
    print(f"The port {port} is closed.")
    server_socket = open_port(port)
    print(f"The port {port} has been open succesfully.")
    client_socket = None
    client_address = None

    try:
        server_socket.settimeout(60)  # Max wait time

        client_socket, client_address = server_socket.accept()
        print(f"Connected from {client_address}")

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")
            client_socket.send(data)

    except socket.timeout:
        print("Timeout expired. No connection has been received.")
    except KeyboardInterrupt:
        print("User interruption. Closing the server")
    finally:
        if client_socket:
            client_socket.close()
        server_socket.close()
        print("Server Closed.")
