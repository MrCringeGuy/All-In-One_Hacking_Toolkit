import os
import socket

req = '0'
clear = lambda: os.system('cls')


def import_pkg(req):
    clear()
    try:
        import req
    except ModuleNotFoundError:
        os.system(f'pip install {req}')
    clear()


def port_scan(target_ip, ports):
    for port in range(ports):
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((target_ip, ports))
            print(f'[+] Port {port} Is Open.')
        except:
            print(f'[+] Port {port} Is Closed.')

import_pkg(req)
target_ip = input('[+] Enter Target IP: ')
ports = int(input('[+] Enter Number Of Ports To Scan: '))
port_scan(target_ip, ports)
