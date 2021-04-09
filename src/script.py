from models.Crawler import Crawler
from models.Website import Website

crawler = Crawler()

siteData = [
    ['O\'Reilly Media', 'http://oreilly.com',
        'https://ssearch.oreilly.com/?q=','article.product-result',
        'p.title a', True, 'h1', 'section#product-description']
]

sites = []
for row in siteData:
    sites.append(Website(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))


topics = ['python', 'data science']

for topic in topics:
    print("GETTING INFO ABOUT: " + topic) 
    for targetSite in sites:
        crawler.search(topic, targetSite)