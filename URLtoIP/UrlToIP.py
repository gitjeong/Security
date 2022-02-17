# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 13:33:30 2021

@author: user
"""

import socket

def getIpAddr(url):
    try:
        results = str(socket.getaddrinfo(url,0,0,0,0))
        if results.find("('") > -1 :
            results = results[results.find("('")+2:-7]
            return results
        else:
            return "-"
    except:
        return "-"

urlfile = open("urls.txt", 'r')
ipfile = open("ip.txt", 'w')
ips = ''
urls = urlfile.readlines()
for url in urls:
    url = url.replace('\n','')
    ips = ips + getIpAddr(url) + '\n'
ipfile.write(ips)
urlfile.close()
ipfile.close()
