import requests

startId = 1
endId = 7
url = 'http://www.japaneselawtranslation.go.jp/law/detail_download/'
ff = '01' # Japanese XML
#ff = '06' # English XML

for x in range(startId, endId):
    params = { 'ff': ff, 'id': x }
    filename = "id_" + str(x) + ".xml"
    response = requests.get(url, allow_redirects=True, params=params)
    if response.status_code == 404:
        continue

    if response.status_code == 200:
        with open(filename, 'wb') as fd:
            for chunk in response.iter_content(chunk_size=128):
                fd.write(chunk)
    else:
        print('Server responded with {status} for id {id}'.format(
            status=response.status_code,
            id=x
        ))
