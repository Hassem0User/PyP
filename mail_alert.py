import logging

from scapy.all import ARP, Ether, srp
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def scan_local_network(ip_range):

    while True:
        # Create an ARP request packet to discover local devices
        arp = ARP(pdst=ip_range)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast Ethernet frame

        packet = ether / arp

        # Send the packet and capture responses
        result = srp(packet, timeout=3, verbose=0)[0]
        devices = []


        for sent, received in result:
            # Check if the device is already in the list
            if not any(device['ip'] == received.psrc and device['mac'] == received.hwsrc for device in devices):
                # Add the new device to the list
                devices.append({'ip': received.psrc, 'mac': received.hwsrc})
                body = "New device entered your network{'ip': %(received.psrc)s, 'mac': %(received.hwsrc)s}" \
                       % {"received.psrc": received.psrc, "received.hwsrc": received.hwsrc}

                # Mail
                def send_email(body):
                    sender_email = "mail"
                    receiver_email = "mail"
                    password = "password"
                    subject = "[ALERT] New device In your network"
                    message = MIMEMultipart()
                    message["From"] = sender_email
                    message["To"] = receiver_email
                    message["Subject"] = subject
                    message.attach((MIMEText(body, "plain")))

                    server = smtplib.SMTP("smtp.X.com", 587)  # Replace X with the mail extension
                    server.starttls()
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message.as_string())
                    server.quit()
                    logging.info("New device entered your network")

                send_email(body)


        logging.info("Active devices:")
        for device in devices:
            logging.info("IP Address: %(device['ip'])s, MAC Address: %(device['mac'])s"
                         % {"device['ip']": device['ip'], "device['mac']": device['mac']})
        # Wait for a while before the next scan
        time.sleep(10)

ip_range = "192.168.1.0/24"  # Define subnet interface

scan_local_network(ip_range)
