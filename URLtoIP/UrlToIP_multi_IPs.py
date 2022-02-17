# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 17:08:06 2021

@author: Minsoo Chung
"""

import socket

def getIpAddr(url):
    try:
        results = str(socket.getaddrinfo(url,0,0,0,0))
        indexes=[]
        index=-1
        target='\''
        while True:
                index = results.find(target, index+1)
                if index == -1:
                    break
                indexes.append(index)
        #print(indexes)
        i=0
        while True:
            if i >= len(indexes):
                break
            elif indexes[i+1] == indexes[i] + 1:
                indexes.remove(indexes[i+1])
                indexes.remove(indexes[i])
            else:
                i = i+2
        #print(indexes)
        #print(len(indexes))
        return_val = []
        for j in range(0,len(indexes)-1,2):
            return_val.append(results[indexes[j]+1:indexes[j+1]] + '\n')
        return return_val
    except:
        return ["-\n"]

urlfile = open("urls.txt", 'r')
ipfile = open("ip.txt", 'w')

urls = urlfile.readlines()
for url in urls:
    url = url = url.replace('\n','')
    #ips = ips.append(getIpAddr(url))
    ipaddr = getIpAddr(url)
    for ip in ipaddr:
        ipfile.write(ip)
#ipfile.write(ips)
urlfile.close()
ipfile.close()

"""
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

"""