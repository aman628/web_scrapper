import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def extract_article_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        article_text = soup.find('body').get_text()
        return article_text.strip()
    else:
        return None

def main():
    url = "http://www.shwetalodha.in/2023/03/create-chatbot-based-using-gpt-index.html"
    article_text = extract_article_text(url)
    if article_text is not None:
        file_name = "39.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(article_text)

if __name__ == "__main__":
    main()
