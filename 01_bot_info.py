import requests
from config import TOKEN, BASE_URL
from pprint import pprint


def get_bot_info():
    """
    Task 1: Get Bot Information
    - Use getMe method
    - Return bot's name and username
    - Show verification status
    """
    url=BASE_URL+'/getMe'
    r=requests.get(url)
    data=r.json()
    pprint(data)
    result=data['result']
    first_name=result['first_name']
    username=result['username']
    print(first_name,username)
get_bot_info()
