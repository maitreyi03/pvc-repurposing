import requests
from bs4 import BeautifulSoup

def fetch_news():
    # URL of the news site (example: Google News)
    url = 'https://news.google.com/search?q=recycling+PVC+repurposing+plastic+pollution+microplastics+harms+of+PVC'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    # Find all article links with class "JtKRv"
    for item in soup.find_all('a', class_='JtKRv')[:15]:  # Fetch top 15 articles
        title = item.get_text()
        link = item['href']
        # Construct the full URL
        full_link = f"https://news.google.com{link}"
        articles.append({'title': title, 'url': full_link})

    return articles

def save_to_file(articles):
    with open('news_articles.json', 'w') as file:
        json.dump({'articles': articles}, file, indent=4)

if __name__ == "__main__":
    news_articles = fetch_news()
    save_to_file(news_articles)
