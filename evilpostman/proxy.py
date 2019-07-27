from colorama import Fore, Back, Style
import socks, random

s = socks.socksocket()

def ConnectToProxy(ProxysList):
    with open(ProxysList) as file:
        for lines in file:
            ProxyList = []
            ProxyList.append(lines)
            Proxy = random.choice(ProxyList)

    try:
       s.set_proxy(socks.SOCKS5, Proxy)
       s.connect(Proxy)
       print(Fore.GREEN + '[+] You connected to proxy. Proxy IP is: ' + Proxy)
    except:
       print(Fore.RED + '[-] Cannot connect to proxy. Delete this IP from proxylist')
       ProxyList.remove(Proxy)
       
    
    
