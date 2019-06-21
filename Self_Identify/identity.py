import urllib.request
import bs4

# This website shows your User-Agent, IP, Browser info, Screen Size etc
url = "https://www.whoishostingthis.com/tools/user-agent/"
# Headers to send along with the request (Use ONLY ONE! Comment out others!)
headers = {
    #"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0"
}

# Creating a Request object to send to server
req = urllib.request.Request(url, headers=headers)

# Getting a Response back from the server
resp = urllib.request.urlopen(req).read()

# Parsing the response html with BeautifulSoup for easy access of contents
soup = bs4.BeautifulSoup(resp, "html.parser")

# Getting relevant data from the returned html
user_agent = soup.findAll("div", {"class": "info-box user-agent"})[0].text
user_ip = soup.findAll("div", {"class": "info-box ip"})[0].span.text
rows = soup.findAll("tr")
browser_info = []
for row in rows:
    browser_info.append(row.text)

# Displaying info
print("User-Agent:", user_agent)
print("User-IP:", user_ip)
for each in browser_info:
    print(each)

"""
Look up how to access each of the info from the system itself
"""


input("\n!!!Press ENTER to EXIT!!!")

