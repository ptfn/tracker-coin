import sys
import requests
import time


def file_opt(file):
    arr = file.readlines()
    res = []
    for i in range(len(arr)):
        arr[i] = arr[i].replace('\n', '')
    for i in range(len(arr)):
        for k in range(len(arr[i])):
            if arr[i][k] == ":":
                res.append(arr[i][k+1:])
    return res


def pers(last, new):
    return round((new - last) / last * 100, 2)


file = open('option.txt', 'r')
options = file_opt(file)
coin = options[0]
wallet = options[1]
money = options[2]

while True:
    r = requests.get('https://api.bitfinex.com/v1/pubticker/'+ coin + wallet)
    data = r.json()
    price = data['ask']
    print("{} %".format(pers(float(money), float(price))))
    time.sleep(10)