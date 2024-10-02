# main.py
from gdelt_api import get_articles
from article_crawler import crawl_articles
from sentiment_analysis import analyze_sentiment
from database import get_database, save_to_mongodb


def process_keyword(keyword, domains):
    articles_df = get_articles(keyword, domains, num_records=5)
    if articles_df.empty:
        print(f"No articles found for keyword: {keyword}")
        return

    urls = articles_df['url']
    titles = articles_df['title']
    seendates = articles_df['seendate']
    texts = crawl_articles(urls)

    db = get_database()

    for idx, text in enumerate(texts):
        sentiments = analyze_sentiment(text)
        if sentiments:
            data = {
                "title": titles.iloc[idx],
                "url": urls.iloc[idx],
                "seendate": seendates.iloc[idx],
                "text": text,
                "sentiments": sentiments
            }
            insert_id = save_to_mongodb(db, data)
            print(f"Data inserted with ID: {insert_id}")
        else:
            print("No sentiments extracted.")

def main():
    with open('company.txt', 'r') as rf:
        keywords = rf.readlines()
        
    
    with open('domains.txt', 'r') as rf:
        domains = rf.readlines()

    domains = [domain.strip() for domain in domains]
    keywords = [keyword.strip() for keyword in keywords]
    for k in keywords:
        print(f"Processing keyword: {k}")
        process_keyword(k, domains)

if __name__ == "__main__":
    main()
