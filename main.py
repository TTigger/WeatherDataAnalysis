import requests


response = requests.get('https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-089?Authorization=CWB-A4CB2B13-29D3-4814-A575-3FBE669C55C6&format=JSON')
print(response.text)