import urllib.request
import urllib.parse
import re
import bs4


def get_web_data():
    """
    Gets html data from a website
    """
    url = "http://pythonprogramming.net"
    values = {
        "s": "basics",
        "submit": "search"
    }
    data = urllib.parse.urlencode(values)
    data = data.encode("utf-8")
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    resp_data = resp.read()
    return resp_data


resp_dat = get_web_data()

# Will return all content between <p> tags
# We specify what to return within the () between the tags
# . = any char except for \n
# * = 0 or more reps
# ? = match 0 or 1 reps
paras = re.findall(r"<p>(.*?)<p>", str(resp_dat))

bs = bs4.BeautifulSoup(resp_dat, "lxml")
ps = bs.findAll("<p>")
print(paras)
print(ps)
