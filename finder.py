# https://www.proxy-list.download/api/v1/get?type=http
# https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all

import requests
import urllib.request , socket
import threading
import discord
import time

client = discord.Client()

def normal():
    while True:
        proxyList = []

        proxyListCOM = requests.get("https://www.proxy-list.download/api/v1/get?type=http").text
        proxyScrape = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all").text

        linesProxyListCOM = proxyListCOM.split("\n")
        nonEmptyLinesProxyListCOM = [line for line in linesProxyListCOM if line.strip() != "" or line.strip() != "\n"]

        linesproxyScrape = proxyScrape.split("\n")
        nonEmptyLinesproxyScrape = [line for line in linesproxyScrape if line.strip() != "" or line.strip() != "\n"]

        for proxy in nonEmptyLinesProxyListCOM:
            proxyList.append(proxy)

        for proxy in nonEmptyLinesproxyScrape:
            proxyList.append(proxy)

        def is_bad_proxy(pip):    
            try:        
                proxy_handler = urllib.request.ProxyHandler({'http': pip})        
                opener = urllib.request.build_opener(proxy_handler)
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                urllib.request.install_opener(opener)        
                sock=urllib.request.urlopen('http://www.google.com')  
            except urllib.error.HTTPError as e:        
                return e.code
            except Exception as detail:
                return 1
            return 0

        for item in proxyList:
            bad = threading.Thread(target=is_bad_proxy, args=[item]).start()
            if bad:
                print ("Bad Proxy", item)
            else:
                f = open("proxies.txt", "a")
                f.write(item)
                f.close()
                print (item, "is working")
        time.sleep(300)
        filea = open("proxies.txt","r+")
        filea.truncate(0)
        filea.close()

def roblox():
    while True:
        proxyList = []

        proxyListCOM = requests.get("https://www.proxy-list.download/api/v1/get?type=http").text
        proxyScrape = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all").text

        linesProxyListCOM = proxyListCOM.split("\n")
        nonEmptyLinesProxyListCOM = [line for line in linesProxyListCOM if line.strip() != "" or line.strip() != "\n"]

        linesproxyScrape = proxyScrape.split("\n")
        nonEmptyLinesproxyScrape = [line for line in linesproxyScrape if line.strip() != "" or line.strip() != "\n"]

        for proxy in nonEmptyLinesProxyListCOM:
            proxyList.append(proxy)

        for proxy in nonEmptyLinesproxyScrape:
            proxyList.append(proxy)

        def is_bad_proxy(pip):    
            try:        
                proxy_handler = urllib.request.ProxyHandler({'http': pip})        
                opener = urllib.request.build_opener(proxy_handler)
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                urllib.request.install_opener(opener)        
                sock=urllib.request.urlopen('http://www.roblox.com')  
            except urllib.error.HTTPError as e:        
                return e.code
            except Exception as detail:
                return 1
            return 0

        for item in proxyList:
            bad = threading.Thread(target=is_bad_proxy, args=[item]).start()
            if bad:
                print ("Bad Proxy", item)
            else:
                f = open("roproxies.txt", "a")
                f.write(item)
                f.close()
                print (item, "is working")
        time.sleep(300)
        filea = open("roproxies.txt","r+")
        filea.truncate(0)
        filea.close()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="for new proxies"))
    threading.Thread(target=normal).start()
    threading.Thread(target=roblox).start()
    while True:
        await upload()
        await uploadRoblox()
        time.sleep(300)
        print("relooping")

async def upload():
    channel = client.get_channel(ID)
    await channel.send('Updated Proxies! [Download for proper format]', file=discord.File("proxies.txt"))

async def uploadRoblox():
    channel = client.get_channel(ID)
    await channel.send('Updated Proxies! [Download for proper format]', file=discord.File("roproxies.txt"))

client.run('token')
