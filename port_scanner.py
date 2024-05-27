#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 00:30:19 2024

@author: pavelkim
"""


import socket

def port_scanner(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    ip = input("Enter IP address to scan: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    open_ports = port_scanner(ip, start_port, end_port)
    print(f"Open ports on {ip}: {open_ports}")
