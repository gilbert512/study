import requests
import json

url = 'http://apis.data.go.kr/1360000/VilageFcstMsgService/getWthrSituation'
params ={'serviceKey' : 'XPoQxBGjDcCkUe+SzRwRhJfW7ZxRpYcJudlTEzxQvSaqn7y4u/wKnYZInMpCQJ11jw9iGPq+ZSwmLLsHt8WhHg==', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'JSON', 'stnId' : '146' }

response = requests.get(url, params=params)

print(response.content)

jsonObj = json.loads(response.content)

print(json.dumps(jsonObj, indent=4, ensure_ascii=False))

content = jsonObj['response']['body']['items']['item']

print(json.dumps(content, indent=4, ensure_ascii=False))