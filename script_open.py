import socket as sck
import logging
# Fast Script to iterate ports

for port in range(1, 1024):  # Define port range
    try:
        logging.info('Initializating port scanning ')
        s = sck.socket(sck.AF_INET, sck.SOCK_STREAM) # Define connection parameter
        s.settimeout(1000)  # Define time limit
        s.connect((  # Define connection parameters
            '127.0.0.1',
            port
        ))
        logging.info('%d:OPEN' % port)
        s.close()
    except:
        logging.error('Cannot connect to port: %d' % port)
        continue

logging.info('Ended scan')
