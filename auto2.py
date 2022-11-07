import requests 
import json 
import os
import sys
import urllib.request
from bs4 import BeautifulSoup
import random
from datetime import datetime

client_id = 'kIV9tc6fOFFiNRTT8Voj'
client_secret ='vQCwley762'

# 크롤링할 사이트 
url = 'https://arxiv.org/list/cs.CV/recent'

url_post = "https://www.tistory.com/apis/post/write" 
access_token = '7d13a517677238efc2b674a367736d23_9e310677c4e36c1c8db304f82203de2c'
blog_name = "https://yeobing.tistory.com/"

def get_url_of_the_day():
    papers = []
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a', href=True):
        if a['href'].startswith('/abs/'):
            papers.append('https://arxiv.org{}'.format(a['href']))
    return random.choices(papers, k=3)

# 각 페이퍼 주소에서 그 페이퍼의 제목, 초록, 초록의 한국어 번역본 반환 
def extract_content(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.select_one('#abs > h1').text.replace('Title:', '')
    abstract = soup.select_one('#abs > blockquote').text.replace('Abstract: ', '')
    translation = translate(abstract)
    return title, abstract, translation
    
# 영어 텍스트 한국어로 번역하기 (파파고 API 사용 )
def translate(eng_abs):
    try:
        text = urllib.parse.quote(eng_abs)
        data = "source=en&target=ko&text=" + text
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            res = response_body.decode('utf-8')
            res = json.loads(res)
            result = res['message']['result']['translatedText']
            return result
    except:
        return ''

# 글 쓰기 
def write_post():
    
    post = ''
    titles = []
    abstracts = []
    translations = []

    urls = get_url_of_the_day()
    for url in urls:
        title, abstract, translation = extract_content(url)
        titles.append(title)
        abstracts.append(abstract)
        translations.append(translation)
    
    
    for ti, ab, tr in zip(titles, abstracts, translations):
        post += "<h3 data-ke-size='size23'><b><span style='font-family: 'Noto Sans Demilight', 'Noto Sans KR';'>{}</span></b><span style='font-family: 'Noto Sans Demilight', 'Noto Sans KR';'></span></h3>".format(ti)
        post += "<p data-ke-size='size18'>&nbsp;</p>"
        post += "<p data-ke-size='size18'><span style='font-family: 'Noto Sans Demilight', 'Noto Sans KR';'>{}</span></p>".format(ab)
        post += "<p data-ke-size='size18'>&nbsp;</p>"
        post += "<p data-ke-size='size18'><span style='font-family: 'Noto Sans Demilight', 'Noto Sans KR';'>{}&nbsp;</span></p>".format(tr)
        post += "<p data-ke-size='size18'>&nbsp;</p>"
        post += "<p data-ke-size='size18'>&nbsp;</p>"
    
    html_file = open('./post.html', 'w+')
    html_file.write(post)
    html_file.close()


if __name__ == '__main__':
	
    # 글 제목 
    title = '[{}] 오늘의 영상처리'.format(datetime.today().strftime('%Y-%m-%d')) 

    write_post()
    f = open('./post.html', 'r')
    # 글 내용 
    content = f.read()

    visibility = 3 #(0: 비공개 - 기본값, 1: 보호, 3: 발행) 
    category = 973726 # 글을 올리고 싶은 카테고리 번호 
    publish_time = '' 
    slogan = '' 
    tag = '논문,CV,컴퓨터비전,영상딥러닝,object_detection,classfication,objectdetection,computervision,computer_vision,computer vision' # 글 태그 
    acceptComment = 1 # 댓글허용 
    password = '' # 보호글 비밀번호 

    headers = {'Content-Type': 'application/json; charset=utf-8'} 
    params = { 'access_token': access_token, 'output': 'json', 'blogName': blog_name, 'title': title, 'content': content, 'visibility': visibility, 'category': category, 'published': publish_time, 'slogan': slogan, 'tag': tag, 'acceptComment': acceptComment, 'password': password } 
    data = json.dumps(params) 
    rw = requests.post(url_post, headers=headers, data=data) 

    if rw.status_code == 200: 
        print('ok') 
    else: 
        print('fail')