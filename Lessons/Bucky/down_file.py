from urllib import request

links = [
    # The .csv is in a .zip file:
    'http://spatialkeydocs.s3.amazonaws.com/FL_insurance_sample.csv.zip',
    # Raw .csv file:
    'https://www.sample-videos.com/csv/Sample-Spreadsheet-100-rows.csv'
]

def download_csv(url):
    response = request.urlopen(url)
    csv = response.read()
    # Parsing file data to string:
    csv_str = str(csv)
    # Using \ before \n to escape character:
    lines = csv_str.split('\\n')
    # Using r = raw string so that we don't have to write \ multiple times when writing directories:
    directory = r'D:\Py\WebCrawler'
    dest_url = r'sample_sheet.csv'
    f = open(dest_url, 'w')
    for line in lines:
        f.write(line + '\n')
    f.close()


download_csv(links[1])

