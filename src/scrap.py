from pygooglenews import GoogleNews
import re
import pandas as pd
import time
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required=True, help="news keyword")
args = vars(ap.parse_args())


def search_news_headlines(query) -> None:
    gn = GoogleNews(lang='id', country='id')
    search = gn.search(query)
    news_item = search['entries']
    timestr = time.strftime("%Y%m%d-%H%M%S")
    source_list = []

    print("Total Data Scraped")
    print(len(news_item))

    for j in news_item:
        source = j['title'].split(" - ", 1)[1]
        source_list.append(source)

    for i in news_item:
        i['title'] = re.sub('-.*', '', i['title'])
        i['title'] = re.sub('[^a-zA-Z0-9 ]', '', i['title'])
        i['title'] = re.sub('com', '', i['title'])
        if len(i['title'].split()) > 5:
            df = pd.DataFrame({
                'title': [i['title'] for i in news_item],
                'link': [i['link'] for i in news_item]
            })

    df['source'] = source_list
    df.to_csv('news_headlines_' + timestr + '.csv')


if __name__ == "__main__":
    search_news_headlines(args["query"])
