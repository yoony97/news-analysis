from gdeltdoc import GdeltDoc, Filters
from datetime import datetime, timedelta


def get_articles(keyword, domains, num_records=10):
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    # Format dates as strings in 'YYYY-MM-DD' format
    end_date_str = end_date.strftime('%Y-%m-%d')
    start_date_str = start_date.strftime('%Y-%m-%d')
    f = Filters(
        start_date=start_date_str,
        end_date=end_date_str,
        keyword=keyword,
        domain=domains,
        country=["UK", "US"],
        num_records=num_records
    )
    gd = GdeltDoc()
    articles = gd.article_search(f)
    return articles