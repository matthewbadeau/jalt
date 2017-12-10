import argparse
import requests

parser = argparse.ArgumentParser(
    description="Sequentially collect legal documents from www.japaneselawtranslation.go.jp."
)
parser.add_argument("-s", "--start", help="The ID at which to start.", type=int, default=5)
parser.add_argument("-e", "--end", help="The ID at which to finish.", type=int, default=6)
parser.add_argument(
    "-f",
    "--format",
    help="Format to retreive. See https://github.com/matthewbadeau/jalt/wiki/Notes for details.",
    type=str,
    default='01'
)
parser.add_argument("-v", "--verbose", help="Show more information.", action="store_true")
args = parser.parse_args()
url = 'http://www.japaneselawtranslation.go.jp/law/detail_download/'

for x in range(args.start, args.end):
    params = {'ff': args.format, 'id': x}
    filename = params['ff'] + "_id_" + str(x) + ".xml"
    response = requests.get(url, allow_redirects=True, params=params)

    if response.status_code == 200 and 'content-disposition' in response.headers:
        if args.verbose:
            print("{id} exists. Writing to {filename}.".format(
                id=x,
                filename=filename
            ))
        with open(filename, 'wb') as fd:
            for chunk in response.iter_content(chunk_size=128):
                fd.write(chunk)
    elif response.status_code == 200 and not 'content-disposition' in response.headers:
        if args.verbose:
            print("{id} does not have a valid XML to download.".format(
                id=x
            ))
    elif response.status_code == 404:
        if args.verbose:
            print("{id} does not exist. Continuing.".format(
                id=x
            ))
        continue
    else:
        print('Server responded with {status} for id {id}'.format(
            status=response.status_code,
            id=x
        ))
