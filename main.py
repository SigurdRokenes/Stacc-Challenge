import csv
import requests
import pandas as pd
import json

PATH = "data/pep_small.csv"
URL = "https://code-challenge.stacc.dev/api/pep?name=Knut Arild Hareide"
class Main:

    def __init__(self):
        self.data = self.read_data(PATH)

    def read_data(self, path):
        """
        Reads csv file data and outputs as pandas dataframe

        Input: (str) path to datafile
        output: (DataFrame)
        """
        return pd.read_csv(path, sep = ",", header='infer')


    def check_name(self, name = str):
        """
        Checks for matching names in PEP registry
        input (str): 
        """

        matching_data = self.data[self.data['name'] == name]

    def check_company(self, id = int):
        matching_data = self.data[self.data[id]]

    def test(self, id):
        params = {
            'orgNr': '{}'.format(id),
        }
        response = requests.get('https://code-challenge.stacc.dev/api/roller', params=params)

        return response.json()[0]

def main():
    reader = Main()
    reader.check_name(name = "Oleg SLIZHEVSKIY")
    test = reader.test(988971375)
    bronnoysund = dict(test.json()[0])
    print(bronnoysund['fornavn'])
    #print(pd.read_json(test.json()))



if __name__ == "__main__":
    main()
