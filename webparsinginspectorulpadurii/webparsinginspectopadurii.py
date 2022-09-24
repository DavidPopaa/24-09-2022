# import json
# import os
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import requests

# # os.environ['PATH'] += r"C:\Users\popac\Downloads\chromedriver_win32"

# # driver = webdriver.Chrome()

# # driver.get("https://inspectorulpadurii.ro/#/")


# # time.sleep(0.5)
# nr_auto = input("Nr.Auto: ")
# print("loading...")
# response = requests.get(f"https://inspectorulpadurii.ro/api/aviz/locations?nr={nr_auto}&cod=&nrApv=&tip=")




# data = json.loads(response.text)
# # ca sa convertesc din string in ditcionary
# print(data)
# print(type(data))


# array_de_data = []
# for item in data:
#     array_de_data.append(data[item])
# # iau datele din dictionar si le mut in array, facand un array de array-uri


# codul_avizului = array_de_data[1][0]

# array_de_exportat_metri_cubi = []
# for item in array_de_data[1]:
#     time.sleep(1)
#     responseee = requests.get(f"https://inspectorulpadurii.ro/api/aviz/{item}")
#     decoded_responsee = responseee.json()
#     del decoded_responsee['poze']
#     print("=================")
#     print(decoded_responsee['marfa']['total'])
#     array_de_exportat_metri_cubi.append(decoded_responsee['marfa']['total'])


# print("array de exportat:")
# print(array_de_exportat_metri_cubi)