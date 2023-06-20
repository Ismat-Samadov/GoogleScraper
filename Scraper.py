import csv
from googlesearch import search

def scrape_google_search_results(query):
    links = []
    for result in search(query, num_results=10):  # Set the desired number of results
        links.append(result)
    return links

def save_to_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Search Results"])
        writer.writerows([[link] for link in data])

query = "web scraping"
search_results = scrape_google_search_results(query)
save_to_csv(search_results, "search_results.csv")
