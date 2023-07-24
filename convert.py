import csv
import random
from scholarly import scholarly
from scholarly import ProxyGenerator
import re 
import pandas as pd

def scrape_google_scholar(url):
    pg = ProxyGenerator()
    pg.FreeProxies()
    scholarly.use_proxy(pg)
    #scholarly.launch_tor('usr/bin/tor')
    # scholarly.use_tor(tor_sock_port=9050, tor_control_port=9051, tor_password="scholarly_password")
    search_query = scholarly.search_pubs(url)
    article = next(search_query)
    print(f"NUMBER OF CITATIONS {article['num_citations']}")

    return article['num_citations']

def main():
    df = pd.read_csv("CleanedFile.csv")
    df = df[440:500]

    for i, row in df.iterrows():
        k = row['Title']
        query = re.sub(r"[^a-zA-Z0-9]+", ' ', k)
        print(f"QUERY: {query}")
        print(f"ARTICLE NUMBER: {i}")

        url = "https://scholar.google.com/scholar?hl=en&q="+query
        
        print(f"FULL URL: {url}")

        citations = ""

        try:
            citations = scrape_google_scholar(url)
            # print("CITATIONS: " + str(citations))
            # writer.writerow([url, citations])    
            # print(f"URL: {url} | Citations: {citations}")
        except Exception as e:
            print(f"Error processing URL: {url} | {e}")
            citations = 0
        
        df.at[i, "Citation"] = citations
        df.to_csv("output.csv")
        print("Done")

    df.to_csv("output.csv")




if __name__ == '__main__':
    main()
