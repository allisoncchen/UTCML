from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType

from selenium.webdriver.chrome.service import Service as ChromeService



import time
import random

import pandas as pd
import re

#  webdriver setup

PORT = '10001'
HOSTNAME = 'us.smartproxy.com'


def configureProxy(): # 6
    p = Proxy() # 7
    p.proxy_type = ProxyType.MANUAL
    p.http_proxy = '{hostname}:{port}'.format(hostname = 
                      HOSTNAME, port = PORT)
    p.ssl_proxy = '{hostname}:{port}'.format(hostname = 
                      HOSTNAME, port = PORT) # 8

    capabilities = webdriver.DesiredCapabilities.CHROME
    p.add_to_capabilities(capabilities) # 9
    return capabilities

options = Options()
options.add_argument('--no-sandbox')
options.add_argument("--headless")
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# service = ChromeService(executable_path='/home/ubuntu/UTCML/chromedriver_linux64')

# driver = webdriver.Chrome(service=service)

# driver = webdriver.Chrome()

# path = '/home/ubuntu/UTCML/chrome-linux64'

# chrome_options = webdriver.ChromeOptions()

# driver = webdriver.Chrome(executable_path = path, options = chrome_options)
# driver = webdriver.Chrome('/home/ubuntu/UTCML/chrome-linux64')

df= pd.read_csv("toFind.csv" )

# run from 149 to 250 in batcßhes and also save these batches in seperate csv. If the terminal prints "Please show you're not a robot" or "Our systems have detected unusual traffic from your computer network. This page checks to see if it's really you sending the requests, and not a robot. Why did this happen?" you have to stop for a while or change your network

start = 55
stop = 84

df = df[start:stop]
# print(f"df {df}")

outputFile = f"{start}-{stop}"
print(f"output file name: {outputFile}")

# quit()
#open the webpage
for i, row in df.iterrows():
    k = row['Title']
    # k="A message from Addiction's new Editor‐in‐Chief, Professor John Marsden."
    query = re.sub(r"[^a-zA-Z0-9]+", ' ', k)
    print(f"ARTICLE #: {i}")
    print(query)
    # ("HERE)")
    # query = "A message from Addiction s new Editor in Chief Professor John Marsden"
    url = "https://scholar.google.com/scholar?hl=en&q="+query
    print(url)
    driver.get(url)
    
    # driver.get("https://www.geeksforgeeks.org/competitive-programming-a-complete-guide/")
    # print(driver.find_element(By.XPATH, "/html/body").text)
    x = driver.find_element(By.XPATH, "/html/body").text
    print(f"X = {x}")

    # quit()
  
    # print("sk")

    time.sleep(5)
    elements = [f for f in driver.find_elements(By.XPATH, "//*[contains(@class, 'gs_fl') or @class = 'gs_fl']")]
    if len(elements) > 2:
        df.at[i,"Citation"] = 0
        print("putting a -")
        continue;

    # quit()

    # wait for the page to load and extract the number of citations
    time.sleep(5)

    try:
        cited_by = driver.find_element(By.XPATH, "//a[contains(text(),'Cited by ')]")

    except:
        df.at[i,"Citation"]=0
        # print(row['Citation'])
        print(f"putting a 0 \n")
        df.to_csv(f"{outputFile}.csv")
        # quit()
        continue;

    else:
        print(cited_by)
        # quit()
        num_citations = cited_by.text.split(" ")[-1]
        print(f"The paper has {num_citations} citations. \n")
        df.at[i,"Citation"]=num_citations
        # print(row['Citation'])
        df.to_csv(f"{outputFile}.csv")
        # quit()

df.to_csv(f"{outputFile}.csv")
# close the webdriver
# driver.quit()
driver.close()