import time

import requests
import json
import os

class Proxy:
    """
    A class for managing and testing proxy servers.

    current proxy_api Website : https://proxyscrape.com/free-proxy-list
    other proxy website : https://free-proxy-list.net/#   ,  https://geonode.com/free-proxy-list
    """

    def __init__(self):
        """
        Initialize the Proxy object.
        """
        pass

    def fatch_new_proxies(self):

        url = 'https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=json&limit=15'
        # url = 'http://pubproxy.com/api/proxy'
        api_proxies = []
        response = requests.get(url)
        if response.status_code == 200:
            proxies = response.json()
            for i in proxies['proxies']:
                ip = str(i['ip']) + ':' + str(i['port'])
                api_proxies.append(ip)

        # if os.path.exists('new_proxies'):
        #     os.remove('new_proxies')
        with open('new_proxies', 'w') as file:
            file.write(json.dumps(api_proxies))
            # json.dump(api_proxies, open('new_proxies', 'w'))
            print("new proxy saved..")
    def filter_proxy(self):

        # self.fatch_new_proxies()
        proxies = json.load(open('new_proxies', 'r'))
        tested_proxy = []
        count = 0
        for proxy in proxies:
            count+=1
            print(count)
            proxy = proxy.split(':')
            # print(f'Testing proxy: {proxy[0]}:{proxy[1]}')

            proxy_url = {'https': f'https://{proxy[0]}:{proxy[1]}', 'http': f'http://{proxy[0]}:{proxy[1]}'}
            try:
                with requests.Session() as session:
                    session.proxies = proxy_url
                    # print(session.proxies)
                    response = session.get('http://ip-api.com/json')
                    # print(json.dumps(response.json(), indent=2))
                    if response.status_code == 200:
                        print(f'Proxy {proxy_url} is working')
                        print(json.dumps(response.json(), indent=2))
                        tested_proxy.append(proxy_url)
                    else:
                        continue
            except:
                continue


        # if os.path.exists('final_proxies'):
        #     os.remove('final_proxies')
        with open('final_proxies', 'w') as file:
            file.write(json.dumps(tested_proxy))
            # json.dump(tested_proxy, open('final_proxies', 'w'))
            print("Saved Working Proxies")

    def proxy(self):
        proxies = json.load(open('final_proxies', 'r'))
        print(proxies)
        # tested_proxy = []
        for proxy in proxies:
            proxy = proxy.split(':')
            proxy_url = {'https': f'https://{proxy[0]}:{proxy[1]}', 'http': f'http://{proxy[0]}:{proxy[1]}'}
            with requests.Session() as session:
                session.proxies = proxy_url
                # print(session.proxies)
                try:
                    response = session.get('https://www.angelone.in/', timeout=5)
                    # print(json.dumps(response.json(), indent=2))

                    if response.status_code == 200:
                        # print(f'Proxy {proxy_url} is connected')
                        # print(json.dumps(response.json(), indent=2))
                        # tested_proxy.append(proxy_url)

                        break
                    else:
                        continue
                except:
                    continue
        print('working proxy is ready')
    def main(self):
        print("file is called")
        self.fatch_new_proxies()
        self.filter_proxy()
        return self.proxy()

if __name__ == '__main__':
    now = time.time()
    proxy = Proxy()
    proxy.main()
    end = time.time() - now
    print(end)