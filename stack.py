import requests

def stack_request(name):
    url = 'https://api.stackexchange.com/'+name
    response = requests.get(url)
    temp = response.json()
    return temp

test = stack_request('/2.3/questions?fromdate=1635724800&todate=1635811200&order=desc&sort=activity&tagged=Python&site=stackoverflow')['items']
n = 0
for id in test:
    n += 1
    print(n, id['title'])


