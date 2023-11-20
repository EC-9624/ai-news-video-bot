from GoogleNews import GoogleNews
from newspaper import Article


googlenews = GoogleNews(lang='ja', encode='utf-8')
googlenews.get_news('openai')
result = googlenews.results()
links = googlenews.get_links()
print(result)
article_link = result[0]['link']

if not article_link.startswith("https://"):
    article_link = "https://" + article_link


article = Article(article_link)
article.download()
article.parse()


# Print the article's title and summary
print("Title:", article.title)
print("\Text:")
print(article.text)
