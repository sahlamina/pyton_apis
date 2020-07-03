# What is an API
# Application programming interface
# why - used to connect to other programmes
#i n python we have a module called requests with WEB_APIS

# how can we install a python package in pycharm
# pip install requests

import requests
# requests allows us to

# print(response_bbc.status_code) # status_code is a way to make it more human readable, a method from requests
# print(response_bbc.headers) # this checks how they've done the data
# print(type(response_bbc.headers)) # checking the type of data type of the headers
# print(response_bbc.content) # this prints the content of the website
# print(response_bbc.)

# iteration 1
# receive a response and check if 200 - print success

# print(response_bbc.status_code)
# if response_bbc.status_code == "200":
#     print("success")
# #elif code 400 - page not found
# elif response_bbc.status_code == "400":
#     print("Page not found...")
# # elif 404 - oops sorry something went wrong
# elif response_bbc.status_code == "404":
#     print("oops sorry something went wrong")

# iteration 2
# create a function called check_response_code() including all the above

response_bbc = requests.get("https://www.bbc.co.uk/")
def check_response_code():
    if response_bbc.status_code == 200:
        print("success")
    # elif code 400 - page not found
    elif response_bbc.status_code == 400:
        print("Page not found...")
    # elif 404 - oops sorry something went wrong
    elif response_bbc.status_code == 404:
        print("oops sorry something went wrong")
    else:
        pass

check_response_code()

# returns the message with status code

# 3rd iteration OOP

