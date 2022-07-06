#import requests
from core.query import query_company
import pandas as pd



class FetchLeadership:
    def __init__(self):
        self.org_id = ""
        self.leadership = pd.DataFrame()

    
    def fetch_info(self, query, id):
        try:
            response = query_company(query, id)
            return response
        except:
            print("Query has failed, check your spelling")
        

    def parse_company_leadership(self, json):
        
        leadership = []

        for i in range(len(json)):
            #Check if current items contain leadership information
            if json[i]['type']['kode'] == "STYR":

                print("number of people in leadership: ",len(json[i]['roller']))

                #iterate through everyone in leadership
                for styremedlem in json[i]['roller']:
                    
                    person = styremedlem['person']
                    name = ''
                    all_names = list(person['navn'].values())
                    #retrieve name as single string
                    for i in range(len(all_names)):
                        name += all_names[i]
                        #add spaces between names unless last name
                        if i+1  < len(all_names):
                             name += ' '
                    #print(person['fodselsdato'])
                    leadership.append({"Name": name, "dateofbirth": person['fodselsdato']})


            else:
                continue

        return pd.DataFrame.from_dict(leadership)
    
    def check_company(self, org_id):
        r = self.fetch_info("roller", org_id)
        self.leadership = self.parse_company_leadership(r)
        self.org_id = org_id
        return self.leadership



def main():
    test = Roles()
    test(ORG_ID)

if __name__ == '__main__':
    main()

