from selenium import webdriver 
import tistoryReq
 
import time
from selenium.webdriver.common.by import By
 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r'E:\codestates\프로젝트\posting\chromedriver.exe', options=options)

naverNewsUrl = 'https://news.naver.com/'
 
driver.get(naverNewsUrl)
 
# 랭킹 뉴스 XPATH 클릭
driver.find_element(By.XPATH, '/html/body/section/header/div[2]/div/div/div[1]/div/div/ul/li[8]/a/span')

# 뉴스 목록 XPATH 클릭
driver.find_element(By.XPATH, '//*[@id="wrap"]/div[4]/div[2]/div/div[1]/ul')
time.sleep(5)
 

# 썸네일 기사 
hdAtag = hdFlickItem.find_element_by_tag_name('a')
 
# 링크
hdHref = hdAtag.get_attribute('href')
 
# 이미지
hdImgTag = hdAtag.find_element_by_tag_name('img')
hdImgSrc = hdImgTag.get_attribute('src')
 
driver.get(hdHref)
time.sleep(1)
 
# 제목
driver.switch_to.window(driver.window_handles[-1])
thumTitHead = driver.find_element_by_class_name('tts_head')
hdTitle = thumTitHead.text
 
driver.back()
driver.switch_to.window(driver.window_handles[-1])
 
print('썸네일 링크 : ', hdHref) 
print('썸네일 이미지 src : ', hdImgSrc)
print('썸네일 제목 : ', hdTitle)
 
result = []
result.append(hdTitle)
result.append(hdHref)
result.append(hdImgSrc)
 
# li를 감싼 div 검색
tmNews = driver.find_element_by_id('today_main_news')
# div 내에서 li 리스트 검색
tmNewsLis = tmNews.find_elements_by_tag_name('li')
 
# li는 여러개이므로 for문으로 루프
for li in range(len(tmNewsLis)) :
    tmNews = driver.find_element_by_id('today_main_news')
    tmNewsLis = tmNews.find_elements_by_tag_name('li')
 
    aTag = tmNewsLis[li].find_element_by_tag_name('a')
    href = aTag.get_attribute('href')
 
    print('기사 제목 :', aTag.text)
    print('링크 : ', href)
    result.append(aTag.text)
    result.append(href)
 
    driver.get(href)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])
    main = driver.find_element_by_id('articleBody') # main content
    try:
        imgTag = main.find_element_by_tag_name('img')
        imgSrc = imgTag.get_attribute('src')
    except:
        imgSrc = ''
    print('이미지 :', imgSrc)
    result.append(imgSrc)
 
    
    driver.back()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[-1])
    
result = [result[i:i+3] for i in range(0, len(result), 3)]
print(result)
 
tistoryReq.autoWrite(result)
 
driver.quit()