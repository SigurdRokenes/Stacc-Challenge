#import requests
from query import query_company
#from config import * 
#ORG_ID = 988971375
ORG_ID = 871088772
URL = "https://code-challenge.stacc.dev/api/pep?name=Knut Arild Hareide"


class Roles:
    def __init__(self):
        self.org_id = ""
        self.name = ""
        self.birthdate = ""
        self.role = ""
        self.code = ""
    
    def fetch_info(self, query, id):
        try:
            response = query_company(query, id)
            return response
        except:
            print("Query has failed, check your spelling")
        

    def parse_company_leadership(self, json):
        names = []
        for i in range(len(json)):
            #Check if current items contain leadership information
            if json[i]['type']['kode'] == "STYR":

                print("number of people in leadership: ",len(json[i]['roller']))

                #iterate through everyone in leadership
                for styremedlem in json[i]['roller']:

                    person = styremedlem['person']
                    names = person['navn']
                    

            else:
                continue

        return json
    
    def __call__(self, id):
        r = self.fetch_info("roller", id)
        parsed_info = self.parse_company_leadership(r)
        #print(type(parsed_info))


def main():
    test = Roles()
    test(ORG_ID)

if __name__ == '__main__':
    main()

