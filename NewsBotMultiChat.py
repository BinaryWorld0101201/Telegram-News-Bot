import json
import requests
import time
import datetime
TOKEN = "672919339:AAFzwtKcZc6DEMuDop1quOHb928-w8-HZeQ"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content
def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js
def get_update():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js
def get_chat_id_and_text(updates):
    now = datetime.datetime.now()
    chat_list = []
    for i in updates['result']:
        if i['message']['chat']['id'] not in chat_list:
            chat_list.append(i['message']['chat']['id'])
            
    for i in chat_list:
        print("chat ids: ",i)
    print()
    url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=ce41de8a4d04411c90aeb120aa060d5a')
    news = requests.get(url).json()
    article= news['articles']
    news_list = [u'\u2705 News Headlines',now.strftime("%Y-%m-%d"),now.strftime("%H:%M")] #\u23EC
    for i in article:
        news_list.append(i['title']+"\n")
    #for i in range(int(len(news_list)/4)):
    #   print(i+1,news_list[i])
    text = u"\n\u23E9 "
    text = text.join(news_list)
    return (text, chat_list)
def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    
def main():
    while True:
        text, chat_list = get_chat_id_and_text(get_update())
        for chat_i in chat_list:
            send_message(text, chat_i)
        
        time.sleep(3600)


if __name__ == '__main__':
    main()

#https://api.telegram.org/bot672919339:AAFzwtKcZc6DEMuDop1quOHb928-w8-HZeQ/getUpdates
#https://api.telegram.org/bot<YourBOTToken>/getUpdates
#https://www.rapidtables.com/code/text/unicode-characters.html          (emoji link)
