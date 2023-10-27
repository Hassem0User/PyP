import socket as sck

# Fast Script to iterate ports

for port in range(1, 1024):
    try:
        # Pending to use an INFO logger in this line
        s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
        s.settimeout(1000)
        s.connect((
            '127.0.0.1',
            port
        ))
        print('%d:OPEN' % port)
        s.close()
    except:
        # Pending to use an ERROR logger in this line
        continue
