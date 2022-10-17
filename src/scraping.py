from pygooglenews import GoogleNews
import re
import pandas as pd
import time
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required=True, help="news keyword")
ap.add_argument("-t", "--topic", required=True, help="news topic")
args = vars(ap.parse_args())

print("""
                    ____                       _             
                   / ___|  ___ _ __ __ _ _ __ (_)_ __   __ _ 
                   \___ \ / __| '__/ _` | '_ \| | '_ \ / _` |
                    ___) | (__| | | (_| | |_) | | | | | (_| |
                   |____/ \___|_|  \__,_| .__/|_|_| |_|\__, |
                                        |_|            |___/ 
                                       _ _   _     
                             __      _(_) |_| |__  
                             \ \ /\ / / | __| '_ \ 
                              \ V  V /| | |_| | | |
                               \_/\_/ |_|\__|_| |_|
                                                   
                      ___ _   _ _   _ _____    _    ____  
                     |_ _| \ | | | | | ____|  / \  |  _ \ 
                      | ||  \| | |_| |  _|   / _ \ | | | |
                      | || |\  |  _  | |___ / ___ \| |_| |
                     |___|_| \_|_| |_|_____/_/   \_\____/ 
""")


def search_news_headlines(query, topic=args["topic"].capitalize()) -> None:
    gn = GoogleNews(lang='id', country='id')
    search = gn.search(query)
    news_item = search['entries']
    timestr = time.strftime("%Y%m%d-%H%M%S")
    source_list = []

    print("Total Data Scraped: ", len(news_item))

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
    df['topic'] = topic

    path = 'data/'
    df.to_csv(path + topic + "_" + timestr + '.csv')


if __name__ == "__main__":
    search_news_headlines(args["query"])
