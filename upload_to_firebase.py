import json
import requests

with open('open_countries_19_01_2021.json') as json_file:
    data = json.load(json_file)
    
url = "https://firestore.googleapis.com/v1/projects/PROJECT_NAME/databases/(default)/documents/COLLECTION_NAME?documentId="

# Bearer token could be obtained via https://firebase.google.com/docs/firestore/reference/rest/v1beta1/projects.databases.documents/createDocument within Networking tab of Dev Tools
headers = {
  'Authorization': 'Bearer GOOGLETOKEN',
  'Content-Type': 'application/json'
}

for k, v in data.items():
    response = requests.request("POST", url + k, headers=headers, data=json.dumps({'fields':v}))
    print(k, response.status_code)
