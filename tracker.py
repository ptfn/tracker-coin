import sys
import time
import requests

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

try:
    argument = sys.argv[1]
except:
    print('Error argument!')
    exit(0)

file = open(argument, 'r')
options = file_opt(file)
coin = options[0]
wallet = options[1]
money = options[2]
limit = options[3]

while True:
    try:
        r = requests.get('https://api.bitfinex.com/v1/pubticker/'+ coin + wallet)
        data = r.json()
        price = data['ask']
        persent = pers(float(money), float(price))
        print("{} %".format(persent))
        if persent >= float(limit) :
            print("LIMIT PRICE!")
    except:
        print('Error request!')
    finally:
        time.sleep(10)