
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 18:36:01 2018

@author: 31043
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
import pandas as pd


output_folder = "D:\\output\\"
chrome_path = "D:\\chromedriver.exe"

def url_creator():
    first_page = "http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&f=S&l=50&d=PTXT&RS=PN&Refine=Refine+Search&Query=P"
    list_links = []
    page_num = range(1357, 46327)
    for each_page in page_num:
        if each_page == 1:
            list_links.append(first_page)
        else:
            next_pages = "http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&f=S&l=50&d=PTXT&p=" + str(each_page) + "&S1=P&Page=Next&OS=P&RS=P"
            list_links.append(next_pages)
    return list_links


list_of_links = url_creator()

def get_page_table(chrome_driver, url, file_number):
    list_records = []
    wait = WebDriverWait(chrome_driver, 20)
    chrome_driver.get(url)
    result_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/table')))
    soup = BeautifulSoup(result_element.get_attribute('innerHTML'), 'lxml')
    table_records = soup.find_all('tr')
    for each_record in table_records[1:]:
        each_record_map = dict()
        data_points = each_record.find_all('td')
        each_record_map['Serial Number'] = data_points[0].text.strip()
        each_record_map['Patent Number'] = data_points[1].text.strip()
        each_record_map['Patent Title'] = data_points[3].text.strip()
        link = data_points[3].find('a').get('href')
        link = "http://patft.uspto.gov" + link
        each_record_map['Patent URL'] = link
        list_records.append(each_record_map)
    file_to_write = output_folder + str(file_number) + '.csv'
    data = pd.DataFrame(list_records)
    data.to_csv(file_to_write, index = False)

driver = webdriver.Chrome(executable_path=chrome_path)
i = 1357
for each_link in list_of_links:
    while(True):
        try:
            get_page_table(driver, each_link, i)
            break
        except TimeoutException:
            driver.quit()
            driver = webdriver.Chrome(executable_path=chrome_path)
            continue
        except NoSuchElementException:
            driver.quit()
            driver = webdriver.Chrome(executable_path=chrome_path)
            continue
        except WebDriverException:
            driver.quit()
            driver = webdriver.Chrome(executable_path=chrome_path)
            continue
    i = i + 1

driver.quit()

