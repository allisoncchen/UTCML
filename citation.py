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

# Get most updated web driver from the internet
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Main file of 2055 with all the article information 
fileToRead = "toRerun.csv"
df= pd.read_csv(fileToRead)

# Start and stop indexes for each iteration
start = 60
stop = 90

# Start = inclusive / Stop = exclusive
df = df[start:stop]
# print(f"df {df}")

outputFile = f"{start}-{stop}"
print(f"output file name: {outputFile}")


# Iterating throughout the entire CSV
for i, row in df.iterrows():

    # Grabbing title and formatting to get rid of weird punctuation
    k = row['Title']
    query = re.sub(r"[^a-zA-Z0-9]+", ' ', k)

    # For testing purposes
    print(f"ARTICLE #: {i}")
    print(query)
    
    # Appending article title to google scholar link to find page
    url = "https://scholar.google.com/scholar?hl=en&q="+query
    print(url)
    driver.get(url)
    
    
    x = driver.find_element(By.XPATH, "/html/body").text
    print(f"X = {x}")

    # 5 second pause before getting webdriver gets Google Scholar data
    time.sleep(5)
    elements = [f for f in driver.find_elements(By.XPATH, "//*[contains(@class, 'gs_fl') or @class = 'gs_fl']")]

    # If more than 2 elements, script will automatically put a 0 
    if len(elements) > 2:
        df.at[i,"Citation"] = "-"
        print("putting a -")
        continue;

    # Wait for the page to load and extract the number of citations
    time.sleep(5)

    try:
        cited_by = driver.find_element(By.XPATH, "//a[contains(text(),'Cited by ')]")

    except:
        df.at[i,"Citation"] = 0
        # print(row['Citation'])
        print(f"putting a 0 \n")
        df.to_csv(f"{outputFile}.csv")
        # quit()
        continue;

    else:
        print(cited_by)
        
        num_citations = cited_by.text.split(" ")[-1]
        print(f"The paper has {num_citations} citations. \n")
        df.at[i,"Citation"]=num_citations
        
        df.to_csv(f"{outputFile}.csv")
        

# Writing data to output file
df.to_csv(f"{outputFile}.csv")


# Close the webdriver
driver.close()
