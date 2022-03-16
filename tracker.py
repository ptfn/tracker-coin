import sys
import time
import requests

def pers(last, new):
    return round((new - last) / last * 100, 2)

def main():
    try:
        coin = sys.argv[1]
        wallet = sys.argv[2]
        money = sys.argv[3]
        limit = sys.argv[4]
    except:
        print("Error!")
        exit(0)

    while True:
        try:
            r = requests.get("https://api.bitfinex.com/v1/pubticker/"+ coin + wallet)
            data = r.json()
            price = data["ask"]
            persent = pers(float(money), float(price))
            print("{}\t{} %".format(price, persent))
            if persent >= float(limit) :
                print("---LIMIT PRICE!---")
        except:
            print("Error request!")
        finally:
            time.sleep(10)

if __name__ == "__main__":
    main()