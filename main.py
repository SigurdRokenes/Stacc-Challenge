import csv
import requests
import pandas as pd
import json

from core.fetchInfo import FetchLeadership
from core.checkPep import PEP

#Default = arbeiderpartiet
default = 971526939
#Just a few exceptions to ensure input is correct format (9 integers)

while True:
    org_id = input("Skriv firma-nummer (brønnøysundregisteret) (default: Arbeiderpartiet): ")
    if org_id == "":
        org_id = default
    try:
        int(org_id)
    except:
        print('Contains non-numbers... Try again')
        continue
    
    if len(str(org_id)) != 9:
        print('Not 9 numbers... Check your info and try again')
        continue
    else:
        break






def main():
    company = FetchLeadership()
    check = PEP()

    names = company.check_company(org_id)['Name'].to_list()
    print("Checking the following names:")
    print(names)
    #print(check.data.columns)
    matches = check.check_name(names)
    print('Matches in PEP database:')
    print(matches[['name', 'birth_date', 'dataset', 'sanctions']])



if __name__ == '__main__':
    try:
        main()
    except SystemExit as e:
        print('Error!', e)
        print('Press enter to exit')
        input()
