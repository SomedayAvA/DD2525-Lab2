import requests



url = 'http://localhost:3000/upload/users'
headers = {}
session = requests.Session()

with open(r'C:\Users\15318\Desktop\lab2\code\tools\ben.json','rb') as f:
    files = {'upload-users': ('123', f, 'application/json')}
    response = session.post(url, files=files, headers=headers)
print(response.text)
session = requests.Session()

with open(r'C:\Users\15318\Desktop\lab2\code\tools\ben_attack.json','rb') as f:
    files = {'upload-users': ('123', f, 'application/json')}
    response = session.post(url, files=files, headers=headers)
print(response.text)


