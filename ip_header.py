from socket import *
import os
import struct

def parsing(host):
    if os.name == "nt":
        sock_protocol = IPPROTO_IP
    else:
        sock_protocol = IPPROTO_ICMP
    sock = socket(AF_INET, SOCK_RAW, sock_protocol)
    sock.bind((host, 0))

    #debug
    print("socket binded")

    # socket option
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

    # promiscuous mode on
    if os.name == "nt":
        sock.ioctl(SIO_RCVALL, RCVALL_ON)

    packet_number = 0

    #debug
    print("packet_number: 1")

    try:
        while True:
            packet_number += 1
            data = sock.recvfrom(65535)
            
            #debug
            print("data received")

            ip_headers, ip_payloads = parse_ip_header(data[0])
            print(f"{packet_number} th packet\n")
            print("version: ", ip_headers[0]>>4)
            print("Header length: ", ip_headers[0]&0x0F)
    except KeyboardInterrupt:
        if os.name == "nt":
            sock.ioctl(SIO_RCVALL, RCVALL_OFF)
            sock.close()

def parse_ip_header(ip_header):
    ip_headers = struct.unpack("!BBHHHBBH4s4s", ip_header[:20])
    ip_payloads = ip_header[20:]
    return ip_headers, ip_payloads

if __name__ == "__main__":
    host = "127.0.0.1"
    print(f"Listening at [{host}]")
    parsing(host)
