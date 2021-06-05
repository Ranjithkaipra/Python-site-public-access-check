#!/usr/bin/python
import requests
import socket
import ssl


#curl -s -o /dev/null -I -w "%{http_code}" http://deployer.wrg-apps.com
#curl -I "http://deployer.wrg-apps.com"

sites = open("domains.txt", "r")
for dev_urls in sites:
    #print(x.rstrip())
    response = requests.get(url=dev_urls.rstrip(), allow_redirects=True)
    #print(response)
    print(response.url, response.status_code)