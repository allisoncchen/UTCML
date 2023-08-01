import csv
import random
from scholarly import scholarly
from scholarly import ProxyGenerator
import re 
import pandas as pd

def scrape_google_scholar(url):
    pg = ProxyGenerator()
    pg = pg.FreeProxies()
    scholarly.use_proxy(pg)
    search_query = scholarly.search_pubs(url)
    # scholarly.pprint(next(search_query))
    # article = scholarly.pprint(next(search_query))
    # article = scholarly.fill(scholarly.search_pubs(url))
    article = next(search_query)
    # print(article)
    # you can use data = list(search_query) to get the entire search back
    # df = pd.json_normalize(article)
    # print("HERE: {df}")
    # print("article: " + str(article['num_citations']))
    return article['num_citations']

def main():
    # CSV file paths
    input_csv = 'cleanedFile.csv'
    output_csv = 'output.csv'

    # Read URLs from CSV file
    urls = []
    actualURL = ""

    start_row = 447

    with open(input_csv, 'r') as file:
        reader = csv.reader(file)
        gs = "https://scholar.google.com/scholar?hl=en&q="
        
        for i in range(start_row):
            next(reader)

        for row in reader: 
            # print(gs + row[3])
            url = row[3]
            actualURL = url
            query = re.sub(r"[^a-zA-Z0-9]+", ' ', url)
            urls.append(query)

        # Scrape Google Scholar for citations
        with open(output_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['URL', 'Citations'])

            # for url in urls: #for each row 
            try:
                print(url) # printing out the url
                citations = scrape_google_scholar(url)
                # print("CITATIONS: " + str(citations))
                writer.writerow([url, citations])    
                # print(f"URL: {url} | Citations: {citations}")
            except Exception as e:
                print(f"Error processing URL: {url} | {e}")

if __name__ == '__main__':
    main()
