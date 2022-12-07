import requests
import csv
import math
import pandas as pd
import matplotlib.pyplot as plt
import getRelation

def writeCSV():
    with open('weather.csv', 'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['區', '時間', '12小時降雨機率', '平均溫度', '平均相對濕度', '最小舒適度指數', '最大風速', '最高體感溫度', '天氣現象', '最大舒適度指數', '最低溫度', '紫外線指數', '天氣預報綜合描述', '最低體感溫度', '最高溫度', '風向', '平均露點溫度'])
        data = getData()
        for location in data["records"]["locations"][0]["location"]:
            aria = location["locationName"]
            for weatherElement in location["weatherElement"]:
                if weatherElement["elementName"] == "PoP12h":
                    count = 0
                    PoP12h = list()
                    for time in weatherElement["time"]:
                        PoP12h.append(time["elementValue"][0]["value"])
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
                elif weatherElement["elementName"] == "MinCI":
                    count = 0
                    MinCI = list()
                    for time in weatherElement["time"]:
                        MinCI.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "WS":
                    count = 0
                    WS = list()
                    for time in weatherElement["time"]:
                        WS.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "MaxAT":
                    count = 0
                    MaxAT = list()
                    for time in weatherElement["time"]:
                        MaxAT.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "Wx":
                    count = 0
                    Wx = list()
                    for time in weatherElement["time"]:
                        Wx.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "MaxCI":
                    count = 0
                    MaxCI = list()
                    for time in weatherElement["time"]:
                        MaxCI.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "MinT":
                    count = 0
                    MinT = list()
                    for time in weatherElement["time"]:
                        MinT.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "UVI":
                    count = 0
                    UVI = list()
                    for time in weatherElement["time"]:
                        UVI.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "WeatherDescription":
                    count = 0
                    WeatherDescription = list()
                    for time in weatherElement["time"]:
                        WeatherDescription.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "MinAT":
                    count = 0
                    MinAT = list()
                    for time in weatherElement["time"]:
                        MinAT.append(time["elementValue"][0]["value"])
                        count += 1
                elif weatherElement["elementName"] == "MaxT":
                    count = 0
                    MaxT = list()
                    for time in weatherElement["time"]:
                        MaxT.append(time["elementValue"][0]["value"])
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
            j = 0
            for i in range(count):
                if i % 2 == 1:
                    writer.writerow([aria, "早上", PoP12h[i], T[i], RH[i], MinCI[i], WS[i], MaxAT[i], Wx[i], MaxCI[i], MinT[i], UVI[j], WeatherDescription[i], MinAT[i], MaxT[i], WD[i], Td[i]])
                    j += 1
                else:
                    writer.writerow([aria, "夜晚", PoP12h[i], T[i], RH[i], MinCI[i], WS[i], MaxAT[i], Wx[i], MaxCI[i], MinT[i], "", WeatherDescription[i], MinAT[i], MaxT[i], WD[i], Td[i]])


# 一般天氣預報
def getData():

    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-075?Authorization=CWB-5B0A45C1-7A1B-4557-A797-7F031B4822A2"
    params = {
        "Authorization": "CWB-5B0A45C1-7A1B-4557-A797-7F031B4822A2",
    }

    response = requests.get(url, params=params)

    # print(response.text)
    return response.json()



if __name__ == "__main__":
    writeCSV()

    # 平均溫度與平均相對濕度的關係
    getRelation.get_temperature_and_relativeHumidity()

    # 體感溫度與平均相對溼度的關係
    getRelation.get_bodyTemperature_and_relativeHumidity()

    # 舒適度指數與平均相對濕度的關係
    getRelation.get_ComfortIndex_and_relativeHumidity()

    # 天氣現象與平均溫度的關係
    getRelation.get_weatherPhenomenon_and_Temperature()

    # 12小時降雨機率與平均相對濕度的關係
    getRelation.get_chanceOfRain_and_relativeHumidity()

    # 風向與平均溫度的關係
    # getRelation.get_windDirection_and_Temperature()

    # 風向與平均相對濕度的關係
    # getRelation.get_windDirection_and_relativeHumidity()



    
    