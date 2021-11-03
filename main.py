import requests

def search_request(name):
    url = "https://superheroapi.com/api/2619421814940190/search/"+name
    response = requests.get(url)
    temp = response.json()
    return int(temp['results'][0]['powerstats']['intelligence'])

Hulk=search_request('Hulk')
CaptainAmerica=search_request('Captain America')
Thanos=search_request('Thanos')
if Hulk > CaptainAmerica and Hulk > Thanos:
    print('Самый умный - Halk')
elif CaptainAmerica > Thanos:
    print('Самый умный - Captain America')
else:
    print('Самый умный - Thanos')







