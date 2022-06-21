import requests
import json

url = 'http://203.247.66.28/url/url_apiout.php?authKey=edb8dd556c1cb8d877d0b7255eadc74d265228a70affcd10b1b3cbc1aef77f6b6180879e3da3f92902b166eda1c8238f21a9efdc4d8cfb6774d0069a618fdda7'
params ={'serviceKey' : 'XPoQxBGjDcCkUe+SzRwRhJfW7ZxRpYcJudlTEzxQvSaqn7y4u/wKnYZInMpCQJ11jw9iGPq+ZSwmLLsHt8WhHg==', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'JSON', 'stnId' : '146' }

response = requests.get(url, params=params)

print(response.content)

jsonObj = json.loads(response.content)

print(json.dumps(jsonObj, indent=4, ensure_ascii=False))

content = jsonObj['response']['body']['items']['item']

print(json.dumps(content, indent=4, ensure_ascii=False))