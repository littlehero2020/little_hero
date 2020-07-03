import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "littlehero_server.settings")
import django
django.setup()

from announcement.models import Post
from _db_utils import push_data
from _db_utils import domain_of_url


def parser_1365() :
    URL = 'https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do'
    SHOW = '?type=show&progrmRegistNo='

    #for headless
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('disable-gpu')

    driver = webdriver.Chrome('./chromedriver', chrome_options=options)
    driver.get(URL)
    driver.implicitly_wait(3)
    select = Select(driver.find_element_by_xpath('//*[@id="searchSrvcStts"]'))
    select.select_by_value("3")
    driver.find_element_by_xpath('//*[@id="btnSearch"]').click()
    ## explicit wait for loading
    ele = WebDriverWait(driver, 30).until(EC.element_to_be_selected(driver.find_element_by_xpath('//*[@id="searchSrvcStts"]/option[1]')))

    xpath_for_page_button = '//*[@id="content"]/div[2]/div[5]/div/div/div/a['
    ## get datas
    while True :
        page_temp = driver.find_elements_by_xpath('//*[@id="content"]/div[2]/div[5]/div/div/div/*')
        pageNum = len(page_temp)-4
        for ind in range(2,pageNum+2) :
            #print(str(ind))
            _get_datas(driver, URL, SHOW)
            
            ## go to next page
            page_temp = driver.find_elements_by_xpath('//*[@id="content"]/div[2]/div[5]/div/div/div/*')
            page_temp[ind+1].click()
            ele = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, xpath_for_page_button + str(ind+1)+']')))

        ## if it's last of all data page
        page_temp = driver.find_elements_by_xpath('//*[@id="content"]/div[2]/div[5]/div/div/div/*')
        if page_temp[ind+1].get_attribute('href').split('=')[1] == page_temp[ind].text :
            break
    
    driver.quit()

    return







def _get_datas(driver, URL, SHOW) :
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.select('#content > div.content_view > div.board_list.board_list2.non_sub > ul > li > input')

    ### 순서 바꿔서 소요되는 시간을 줄여야 함.. 나중에 할 것!
    for li in temp :
        data = {}
        val = li.attrs['value']
        data['regist_no'] = int(val)
        data['site_domain'] = domain_of_url.ILSAM65.value

        ## prevent error of server connection error
        while True :
            try :
                res = requests.get(URL+SHOW+val)
                break
            except :
                time.sleep(5)
                continue
            
        data['url'] = URL+SHOW+val
        res_html = res.text
        res_soup = BeautifulSoup(res_html, 'html.parser')
        tmp = res_soup.select('#content > div.content_view > div > div.board_view.type2')[0]
        
        title = tmp.select('h3 > input[type=hidden]')[0].attrs['value']
        data['title'] = title
        #print(title)
        tmpStatus = tmp.select('h3 > em')[0].text
        if tmpStatus == '(모집중)' :
            recruit_status = True
        else :
            recruit_status = False
        data['recruit_status'] = recruit_status
        do_date = tmp.select('div.board_data.type2 > div:nth-child(1) > dl:nth-child(1) > dd')[0].text
        data['do_date'] = do_date
        do_time = tmp.select('div.board_data.type2 > div:nth-child(1) > dl:nth-child(2) > dd')[0].text
        do_week = tmp.select('div.board_data.type2 > div:nth-child(2) > dl:nth-child(2) > dd')[0].text
        data['do_date_extra'] = do_week + ' ' + do_time
        recruit_member = tmp.select('div.board_data.type2 > div:nth-child(3) > dl:nth-child(1) > dd')[0].text
        data['recruit_member'] = recruit_member
        domain = tmp.select('div.board_data.type2 > div:nth-child(4) > dl:nth-child(1) > dd')[0].text
        data['domain'] = domain
        adult_tmp = tmp.select('div.board_data.type2 > div:nth-child(4) > dl:nth-child(2) > dd')[0].text.strip()
        if adult_tmp == '성인' :
            data['adult_status'] = True
        else :
            data['adult_status'] = False
        company_tmp = tmp.select('div.board_data.type2 > div:nth-child(5) > dl:nth-child(1) > dd')
        if company_tmp[0].find('span') :
            company_tmp2 = company_tmp[0].select('span')[0].text
            if company_tmp2[-4:] == '상세정보' :
                data['recruit_company'] = company_tmp2[:-4]
            else :
                data['recruit_company'] = company_tmp2
        else :
            data['recruit_company'] = company_tmp[0].text.strip()

        data['text'] = tmp.select('div.board_body > div.bb_txt')[0].text
        data['telephone'] = tmp.select('div.board_body > div.incharge_data > dl.tel > dd')[0].text
        address_temp = tmp.select('#dataAdres')[0].text.strip().split(' ')
        data['address_city'] = address_temp[0]
        if len(address_temp)== 1 :
            data['address_gu'] = ''
            data['address_remainder'] = ''
        else :
            data['address_gu'] = address_temp[1]
            data['address_remainder'] = ''
            for j in range(2,len(address_temp)) :
                data['address_remainder'] += address_temp[j]
                if j != len(address_temp)-1 :
                    data['address_remainder'] += ' '

        push_data(data)
    return




if __name__ == '__main__' :
    parser_1365()