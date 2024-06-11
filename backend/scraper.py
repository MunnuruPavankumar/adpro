# backend/scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_amazon(query):
    url = f"https://www.amazon.in/s?k={query.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    results = []
    for item in soup.select(".s-result-item"):
        title = item.select_one("h2 .a-text-normal")
        price = item.select_one(".a-price .a-offscreen")
        rating = item.select_one(".a-icon-alt")
        availability = item.select_one(".a-size-small .a-color-success")

        if title and price and rating:
            results.append({
                "productName": title.text.strip(),
                "price": price.text.strip() if price else "N/A",
                "rating": rating.text.strip(),
                "availability": availability.text.strip() if availability else "N/A"
            })
    return results

def scrape_flipkart(query):
    url = f"https://www.flipkart.com/search?q={query.replace(' ', '%20')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    results = []
    for item in soup.select("._1AtVbE"):
        title = item.select_one("._4rR01T")
        price = item.select_one("._30jeq3")
        rating = item.select_one("._3LWZlK")
        availability = item.select_one("._2-RaEL")

        if title and price and rating:
            results.append({
                "productName": title.text.strip(),
                "price": price.text.strip() if price else "N/A",
                "rating": rating.text.strip(),
                "availability": availability.text.strip() if availability else "N/A"
            })
    return results
