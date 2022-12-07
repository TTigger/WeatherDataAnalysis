import requests
import csv
import math
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


# 解決x-label and y-label中文亂碼問題
# https://pyecontech.com/2020/03/27/python_matplotlib_chinese/


# 平均溫度與平均相對濕度的關係
def get_temperature_and_relativeHumidity():
    df = pd.read_csv('weather.csv',encoding="Big5")

    df.groupby('平均溫度')['平均相對濕度'].mean().plot(marker = 'o')

    plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
    plt.grid(True)
    plt.title('平均溫度與平均相對濕度的關係')
    plt.xlabel('平均溫度')
    plt.ylabel('平均相對濕度')
    plt.savefig('relation_images/平均溫度與平均相對濕度的關係.png')
    plt.show()

# 體感溫度與平均相對溼度的關係
def get_bodyTemperature_and_relativeHumidity():
    df = pd.read_csv('weather.csv',encoding="Big5")

    df.groupby('最高體感溫度')['平均相對濕度'].mean().plot(marker = 'o', color = 'red', label = '最高體感溫度')

    df.groupby('最低體感溫度')['平均相對濕度'].mean().plot(marker = 'o', color = 'blue', label = '最低體感溫度')

    plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
    plt.legend(title = '體感溫度', loc = 'upper right')
    plt.grid(True)
    plt.title('體感溫度與平均相對溼度的關係')
    plt.xlabel('體感溫度')
    plt.ylabel('平均相對濕度')
    plt.savefig('relation_images/體感溫度與平均相對溼度的關係.png')
    plt.show()

# 最大舒適度指數與平均相對濕度的關係
def get_ComfortIndex_and_relativeHumidity():
    df = pd.read_csv('weather.csv',encoding="Big5")

    # for i in range(len(df['最大風速'])):
    #     df['最大風速'][i] = df['最大風速'][i].replace('>= ', '')
    #     # print(df['最大風速'][i])
   
    df.groupby('最大舒適度指數')['平均相對濕度'].mean().plot(marker = 'o', color = 'red', label = '最大舒適度指數')

    df.groupby('最小舒適度指數')['平均相對濕度'].mean().plot(marker = 'o', color = 'blue', label = '最小舒適度指數')

    plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
    plt.legend(title = '舒適度指數', loc = 'upper right')
    plt.grid(True)
    plt.title('舒適度指數與平均相對濕度的關係')
    plt.xlabel('舒適度指數')
    plt.ylabel('平均相對濕度')
    plt.savefig('relation_images/舒適度指數與平均相對濕度的關係.png')
    plt.show()

# 天氣現象與平均溫度的關係
def get_weatherPhenomenon_and_Temperature():
    df = pd.read_csv('weather.csv',encoding="Big5")

    plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

    plt.bar(df['天氣現象'], df['平均溫度'], color = 'black')
    plt.title('天氣現象與平均溫度的關係')
    plt.xlabel('天氣現象')
    plt.ylabel('平均溫度')
    plt.savefig('relation_images/天氣現象與平均溫度的關係.png')
    plt.show()

# 12小時降雨機率與平均相對濕度的關係
def get_chanceOfRain_and_relativeHumidity():
    df = pd.read_csv('weather.csv',encoding="Big5")

    # df.dropna(axis=0, how='any')

    df.groupby('12小時降雨機率')['平均相對濕度'].mean().plot(marker = 'o')

    plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
    plt.grid(True)
    plt.title('12小時降雨機率與平均相對濕度的關係')
    plt.xlabel('12小時降雨機率')
    plt.ylabel('平均相對濕度')
    plt.savefig('relation_images/12小時降雨機率與平均相對濕度的關係.png')
    plt.show()

# 風向與平均溫度的關係
def get_windDirection_and_Temperature():
    df = pd.read_csv('weather.csv',encoding="Big5")

    plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

    plt.bar(df['風向'], df['平均溫度'], color = 'black')
    plt.title('風向與平均溫度的關係')
    plt.xlabel('風向')
    plt.ylabel('平均溫度')
    plt.savefig('relation_images/風向與平均溫度的關係.png')
    plt.show()

# 風向與平均相對濕度的關係
def get_windDirection_and_relativeHumidity():
    df = pd.read_csv('weather.csv',encoding="Big5")

    plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

    plt.bar(df['風向'], df['平均相對濕度'], color = 'black')
    plt.title('風向與平均相對濕度的關係')
    plt.xlabel('風向')
    plt.ylabel('平均相對濕度')
    plt.savefig('relation_images/風向與平均相對濕度的關係.png')
    plt.show()


# if __name__ == '__main__':
#     平均溫度與平均相對濕度的關係
#     get_temperature_and_relativeHumidity()

#     體感溫度與平均相對溼度的關係
#     get_bodyTemperature_and_relativeHumidity()

#     舒適度指數與平均相對濕度的關係
#     get_ComfortIndex_and_relativeHumidity()

#     天氣現象與平均溫度的關係
#     get_weatherPhenomenon_and_Temperature()

#     12小時降雨機率與平均相對濕度的關係
#     get_chanceOfRain_and_relativeHumidity()

#     風向與平均溫度的關係
#     get_windDirection_and_Temperature()

#     風向與平均相對濕度的關係
#     get_windDirection_and_relativeHumidity()

