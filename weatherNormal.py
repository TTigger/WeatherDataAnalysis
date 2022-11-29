import requests
import json
import time
import csv
import math

def writeCSV():
    with open('weather.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['縣市', '12小時降雨機率', '天氣現象', '體感溫度', '溫度', '相對濕度', '舒適度指數', '天氣預報綜合描述', '6小時降雨機率', '風速', '風向', '露點溫度'])
        data = getData()
        for location in data["records"]["locations"][0]["location"]:
            city = location["locationName"]
            for weatherElement in location["weatherElement"]:
                if weatherElement["elementName"] == "PoP12h":
                    count = 0
                    PoP12h = list()
                    for time in weatherElement["time"]:
                        PoP12h.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "Wx":
                    count = 0
                    Wx = list()
                    for time in weatherElement["time"]:
                        Wx.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "AT":
                    count = 0
                    AT = list()
                    for time in weatherElement["time"]:
                        AT.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "T":
                    count = 0
                    T = list()
                    for time in weatherElement["time"]:
                        T.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "RH":
                    count = 0
                    RH = list()
                    for time in weatherElement["time"]:
                        RH.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "CI":
                    count = 0
                    CI = list()
                    for time in weatherElement["time"]:
                        CI.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "WeatherDescription":
                    count = 0
                    WeatherDescription = list()
                    for time in weatherElement["time"]:
                        WeatherDescription.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "PoP6h":
                    count = 0
                    PoP6h = list()
                    for time in weatherElement["time"]:
                        PoP6h.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "WS":
                    count = 0
                    WS = list()
                    for time in weatherElement["time"]:
                        WS.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "WD":
                    count = 0
                    WD = list()
                    for time in weatherElement["time"]:
                        WD.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "Td":
                    count = 0
                    Td = list()
                    for time in weatherElement["time"]:
                        Td.append(time["elementValue"][0]["value"])
                        count += 1
            for i in range(count):
                writer.writerow([city, PoP12h[math.floor(i / 6)], Wx[i], AT[i], T[i], RH[i], CI[i], WeatherDescription[i],  PoP6h[math.floor(i / 3)], WS[i], WD[i], Td[i]])

            


# 一般天氣預報
def getData():

    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-089?Authorization=CWB-A4CB2B13-29D3-4814-A575-3FBE669C55C6"
    params = {
        "Authorization": "CWB-5B0A45C1-7A1B-4557-A797-7F031B4822A2",
        # "locationName": locationName,
    }

    response = requests.get(url, params=params)
    return response.json()



if __name__ == "__main__":
    writeCSV()