import requests
from config import TOKEN, BASE_URL
from pprint import pprint


def reply_to_last_user():
    """
    Task 3: Auto-Reply System
    - Get most recent update
    - Extract chat_id
    - Send response message
    """
    url=BASE_URL+'/getUpdates'
    r=requests.get(url)
    data=r.json()
    result=data['result']
    message=result[-1]['message']
    chat=message['chat']
    pprint(chat)
reply_to_last_user()