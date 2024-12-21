# import threading
# import socket
# import requests
# import queue
#
#
# q = queue.Queue(maxsize=0)
# proxy_list = []
#
# with open('proxy_list.text', 'r') as f:
#     proxies = f.read().split('\n')
#     for p in proxies:
#         q.put(p)
#
# def check_proxy():
#     global q
#     while not q.empty():
#         proxy = q.get()
#         try:
#             response = requests.get('http://ipinfo.io/json', proxies={'http': proxy, 'https': proxy})
#
#         except :
#             continue
#
#         if response.status_code == 200:
#             proxy_list.append(proxy)
#             print(proxy)
#
# for _ in range(10):
#     threading.Thread(target=check_proxy).start()

import requests
import json


def proxy():
    proxies = json.load(open('new_proxies', 'r'))
    # tested_proxy = []
    for proxy in proxies:
        proxy = proxy.split(':')
        proxy_url = {'https': f'https://{proxy[0]}:{proxy[1]}', 'http': f'http://{proxy[0]}:{proxy[1]}'}
        with requests.Session() as session:
            session.proxies = proxy_url
            print(session.proxies)
            response = session.get('https://www.angelone.in/')
            print(json.dumps(response.json(), indent=2))
            if response.status_code == 200:
                print(f'Proxy {proxy_url} is connected')
                # print(json.dumps(response.json(), indent=2))
                # tested_proxy.append(proxy_url)

                break
            else:
                continue