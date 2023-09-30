'''
extract a dataset from URL
'''
import requests
url = "https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Air%20Quality/real_2016_air.csv"
filepath = "./data/real_2016_air.csv"
def extract_dataSource(url = "https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Air%20Quality/real_2016_air.csv",
                       filepath = "./data/real_2016_air.csv"):
    ''' extract data from url to a filepath '''
    with requests.get(url) as r:
        with open(filepath, 'wb') as f:
            f.write(r.connect)
    return filepath

