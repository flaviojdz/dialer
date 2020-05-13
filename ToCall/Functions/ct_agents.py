import requests

ACCESS_KEY_ID= ''
ACCESS_KEY_SECRET= ''

def add_agent(firstname,lastname,email):
    url = 'https://my.cloudtalk.io/api/agents/add.json'
    data = {
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "pass": "glovo1234",
        "status_outbound": True,
    }
    r = requests.put(url, auth=(ACCESS_KEY_ID, ACCESS_KEY_SECRET), json=data)
    #return agent cloudtalk id for edit and assignment
    return r.json()['responseData']['data']['id']


def edit_agent(firstname, lastname, email,agent_id):
    url ='https://my.cloudtalk.io/api/agents/edit/'+agent_id+'.json'
    data = {
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "status_outbound": True,
    }
    r = requests.post(url, auth=(ACCESS_KEY_ID, ACCESS_KEY_SECRET), json=data)
    # return agent cloudtalk id for edit and assignment
    return r.json()['responseData']['status']
