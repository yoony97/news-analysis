# article_crawler.py
from newspaper import Article

def crawl_articles(urls):
    texts = []
    for url in urls:
        try:
            article = Article(url)
            article.download()
            article.parse()
            texts.append(article.text)
        except Exception as e:
            print(f"Error crawling {url}: {e}")
            continue
    return texts
