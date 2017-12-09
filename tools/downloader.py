import requests

startId = 5
endId = 6
url = 'http://www.japaneselawtranslation.go.jp/law/detail_download/'
ff = '01' # Japanese XML
#ff = '06' # English XML

for x in range(startId, endId):
    params = { 'ff': ff, 'id': x }
    filename = "id_" + str(x) + ".xml"
    response = requests.get(url, allow_redirects=True, params=params)
    with open(filename, 'wb') as fd:
        for chunk in response.iter_content(chunk_size=128):
            fd.write(chunk)
