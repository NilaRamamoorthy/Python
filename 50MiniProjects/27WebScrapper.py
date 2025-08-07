import requests
import BeautifulSoup

def scrape(url):
    """Scrape news headlines from the given URL."""
    headlines = {}
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all headline elements (adjust the tag and class as needed)
        headline_elements = soup.find_all('h3', class_='gs-c-promo-heading__title')
        
        for idx, element in enumerate(headline_elements, 1):
            title = element.get_text(strip=True)
            link = element.find_parent('a')['href']
            headlines[f"headline_{idx}"] = {"title": title, "link": link}
    
    except requests.exceptions.RequestException as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return headlines

def headline_generator(url):
    """Generator to yield headlines one by one."""
    headlines = scrape(url)
    for key, value in headlines.items():
        yield value

# Example usage
if __name__ == "__main__":
    url = 'https://www.bbc.com/news'
    print("All Headlines:")
    headlines = scrape(url)
    for key, value in headlines.items():
        print(f"{key}: {value['title']} ({value['link']})")
    
    print("\nHeadlines (Generator):")
    for headline in headline_generator(url):
        print(f"{headline['title']} ({headline['link']})")
