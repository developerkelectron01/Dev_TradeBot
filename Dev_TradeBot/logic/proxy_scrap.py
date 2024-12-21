# import requests
# from bs4 import BeautifulSoup
#
# # The URL you want to scrape
# url = "https://spys.one/en/https-ssl-proxy/"
#
# # Send a GET request to the website
# response = requests.get(url)
#
# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the page content using BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # Print the page title (for example)
#     print("Title of the page:", soup.title.string)
#
#     # You can also find specific elements by their tags or class names
#     # Example: Extracting the proxy list (assuming it's in a table with id 'proxylist')
#     proxy_list = soup.find_all('tr')  # Find all table rows
#     for proxy in proxy_list:
#         print(proxy.text.strip())  # Print the text inside each row
#
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")
