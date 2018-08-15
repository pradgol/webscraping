
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
import pandas as pd


data = pd.read_csv('D:\\output13.csv', low_memory = False)
url_list = list(data['Patent URL'])

chrome_path = "D:\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_path)
wait = WebDriverWait(driver, 15)

list_maps = []
for each_link in url_list:
    each_map = dict()
    while True:
        try:
            print(each_link)
            driver.get(each_link)
            abstract_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/p[1]')))
            abstract_text = abstract_element.text.strip()
            each_map['link'] = each_link
            each_map['Abstract'] = abstract_text
            list_maps.append(each_map)
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
           
final_data = pd.DataFrame(list_maps)
final_data.to_csv('D:\\Final_data.csv', index = False)

