import requests
from datetime import datetime
from config import TOKEN, BASE_URL
from pprint import pprint


def check_updates():
    """
    Task 2: Monitor Updates
    - Use getUpdates method
    - Display last 5 messages
    - Show user's name, message content, and timestamp
    """
    url=BASE_URL+'/getUpdates'
    r=requests.get(url)
    data=r.json()
    result=data['result']
    message=result[-1]['message']
    username = message['from']['first_name']
    message_content=message['chat']['type']
    date=message['date']
    text=message['text']
    pprint(username)
    pprint(date)
    pprint(text)
    pprint(message_content)
    
    

check_updates()

