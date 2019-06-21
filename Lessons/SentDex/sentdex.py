import urllib.request
import urllib.parse

# urlopen() opens a link like we do in a browser (a get request)
# Returns .html data sent from the website
# x = urllib.request.urlopen('https://www.google.com')
# Prints the .html data to console:
# print(x.read())

'''
url = 'http://pythonprogramming.net'
values = {
    's': 'basic',
    'submit': 'search'
}

# Adds the submit request to the site url:
data = urllib.parse.urlencode(values)
# Encodes it to 8-bit format:
data = data.encode('utf-8')
# Request we send to the website:
req = urllib.request.Request(url, data)
# Response from website:
resp = urllib.request.urlopen(req)
# Data from response:
respData = resp.read()
print(respData)
'''

try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())
except Exception as e:
    print(str(e), '\nForbidden for bots/programs such as me! :( ')


try:
    url = 'https://www.google.com/search?q=test'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11, Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    }

    # Calling header argument in Request() func and setting our custom header to fool bot detection:
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req, "lxml")
    respData = resp.read()

    # Saving the data received into a text file:
    saveFile = open('with_headers.txt', 'w')
    saveFile.write(str(respData))
    print('\nSecond test successful!\nCheck project directory for .txt file')
except Exception as e:
    print(str(e))
