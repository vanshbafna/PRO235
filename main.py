import requests

for i in range(1, 100):
    URL = f'http://ec2-3-13-85-11.us-east-2.compute.amazonaws.com/profile?id={i}'
    r = requests.get(url = URL)
    if r.status_code == 200:
        print(URL)