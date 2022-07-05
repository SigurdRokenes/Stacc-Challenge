import requests

def query_company(query = "roller", org_id = 988971375):
    """
    Requests info from bronnoysundregisteret using stacc API

    input:
        query:(str) either "roller" or "enheter"
        org_id: (int or str) organisation id

    output:
        dictionary containing queried information
    """

    params = {
        'orgNr': '{}'.format(str(org_id)),
    }
    
    response = requests.get('https://code-challenge.stacc.dev/api/{}'.format(query), params=params)
    #Convert to json and index redundant list out
    response_dict = response.json()

    return response_dict

