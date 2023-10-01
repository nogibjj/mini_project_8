'''
extract a dataset from URL
'''
import requests

def extract(url = "https://raw.githubusercontent.com/MainakRepositor/Datasets/master/Chennai%20rain/chennai_reservoir_rainfall.csv",

            filepath = "./data/rainfall.csv"):
    with requests.get(url) as r:
        with open(filepath,"wb") as f:
            f.write(r.content)
    return filepath

if __name__ == "__main__":
    extract()
