from PIL import Image, ImageDraw, ImageFont
import textwrap
import requests
import webbrowser
from datetime import datetime
import os
from pandas import DataFrame
import time
import json

requests_headers = {}

def get_category(self):
    url = f'https://www.tistory.com/apis/category/list?access_token=7d13a517677238efc2b674a367736d23_9e310677c4e36c1c8db304f82203de2c&output=json&blogName=https://yeobing.tistory.com/'
    r = requests.get(url, headers=requests_headers)
    r = r.json()['tistory']['item']['categories']
    for i in r:
        print(f'{i["name"]} ({i["id"]})')
    return r
print(get_category(''))