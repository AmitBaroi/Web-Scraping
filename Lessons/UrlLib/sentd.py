import urllib.request
import urllib.parse

# Data for Request:
link = "http://pythonprogramming.net"
values = {'s': 'basic',
          'submit': 'search'}

# Turns the values dict to "s=basic&submit=search"
data = urllib.parse.urlencode(values)
# Puts ur data in bytes
data = data.encode('utf-8')
# Turning our link and values into a Request object (stored in req)
req = urllib.request.Request(link, data)
# Response (urlopen is a get request):
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)
