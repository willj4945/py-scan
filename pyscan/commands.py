import click
import sys
import socket
from datetime import datetime

@click.command(help='Perform scan(s) on a target.')
@click.option('-s','--scan', help='Perform a scan on a target IP')
# @click.argument("target", required=False)
def scan(scan):
    """Simple function that scans an IP to check for open ports."""
    target = scan
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror as e:
        print(f"DNS resolution failed: {e}")
        sys.exit(1)
    except socket.error as e:
        print(f"Error occurred while resolving hostname: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
    else:
        print(f"Successfully resolved {target} to {target_ip}")

    # Add Banner
    print("-" * 50)
    print("Scanning Target: " + target)
    print("Scanning started at:" + str(datetime.now()))
    print("-" * 50)

    try:

        # will scan ports between 1 to 65,535
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # returns an error indicator
            result = s.connect_ex((target_ip,port))
            if result ==0:
                print("Port {} is open".format(port))
            s.close()

    except KeyboardInterrupt:
            print("\n Exiting Program !!!!")
            sys.exit()
    except socket.gaierror:
            print("\n Hostname Could Not Be Resolved !!!!")
            sys.exit()
    except socket.error:
            print("\n Server not responding !!!!")
            sys.exit()
