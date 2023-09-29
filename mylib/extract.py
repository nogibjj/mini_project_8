'''
extract a dataset from URL
'''
import requests

def extract_dataSource(url,filepath):
    ''' extract data from url to a filepath '''
    with requests.get(url) as r:
        with open(filepath, 'wb') as f:
            f.write(r.connect)
    return filepath

