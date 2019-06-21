import urllib.parse
import urllib.request
import json

"""
This Google API is NO LONGER AVAILABLE!
We get responseStatus: 403 (Forbidden)
Google detects bots even with User-Agent header

Our link: 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='
"""

# What we want to search Google for
example_search = 'geographic sentiment analysis'
# Replaces spaces with %20s and other web-encoding:
encoded = urllib.parse.quote(example_search)

# Url and Headers that we will send with request
url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='+encoded
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
# The request to be sent
req = urllib.request.Request(url, headers=headers)
# The response from the server
resp = urllib.request.urlopen(req).read()
# Converting to json format
json_data = json.loads(resp)

# Printing . . .
print(json_data)
