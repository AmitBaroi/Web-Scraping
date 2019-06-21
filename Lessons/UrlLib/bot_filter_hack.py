import urllib.request
import urllib.parse

# This req will be blocked
try:
    req = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(req.read())
except Exception as e:
    print(str(e), "Bots are forbidden!")

# This will work!
try:
    url = 'https://www.google.com/search?q=test'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11, Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    }
    # Note: data vs headers (Request parameters)!!!
    # Making a Request object
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    resp_data = resp.read()

    sav_file = open("got stuff.txt", mode='w')
    sav_file.write(str(resp_data))
    sav_file.close()
    print("\nIt worked!")
except Exception as e:
    print(str(e), "This is not supposed to happen! :O")
