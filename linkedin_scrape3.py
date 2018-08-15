from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import xlrd
#import sys
#from imp import reload
#reload(sys)  
#sys.setdefaultencoding('utf8')

import re
import string
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame, Series
from xlrd import *
 
URL_values=[]
Startup_names=[]

wb = open_workbook('/Users/pradeep/One Drive/ISB/ISB_Crowdfunding/Linkedin URLS2.xlsx')
sheet = wb.sheet_by_index(0)
for rownum in range(sheet.nrows):
    URL_values.append(sheet.cell(rownum,1).value)
    Startup_names.append(sheet.cell(rownum,0).value) 

data_all=pd.DataFrame()
issuedata_all=pd.DataFrame()
path="/Users/pradeep/One Drive/ISB/ISB_Crowdfunding/Linkedin.csv"
browser = webdriver.Firefox()
i=-1
for p in URL_values:
    i=i+1
    try:
        
        time.sleep(5.5) 
        
        browser.get(str(p))
        time.sleep(5)
        Startup_name = Startup_names[i]
        URL = p    
        name = browser.find_elements_by_css_selector("#name")
        name_str = "(&) ".join(str(item.text) for item in name)
        print ("Retry1")
        
        Top_Card_Title = browser.find_elements_by_css_selector("#topcard .title")
        Top_Card_Title_str = "(&) ".join(str(item.text) for item in Top_Card_Title)
        print ("Retry2")
        
        Locality =  browser.find_elements_by_css_selector(".locality")
        Locality_str = "(&) ".join(str(item.text) for item in Locality)
        print ("Retry3")
           
        Demographics =  browser.find_elements_by_css_selector("#demographics")
        Demographics_str = "(&) ".join(str(item.text) for item in Demographics)
        print ("Retry4")
        
        Tags =  browser.find_elements_by_css_selector("th")
        Tags_str = "(&) ".join(str(item.text) for item in Tags)
        print ("Retry5")
        
        Profile_Summary =  browser.find_elements_by_css_selector("ol")
        Profile_Summary_str = "(&) ".join(str(item.text) for item in Demographics)
        print ("Retry6")
        
        Profile_Preview =  browser.find_elements_by_css_selector(".profile-overview-content")
        Profile_Preview_str = "(&) ".join(str(item.text) for item in  Profile_Preview)
        print ("Retry7")
        
        Summary =  browser.find_elements_by_css_selector("#summary")
        Summary_str = "(&) ".join(str(item.text) for item in Summary)
        print ("Retry8")
        
        Experience=browser.find_elements_by_css_selector(".position")
        Experience_str = "(&) ".join(str(item.text) for item in Experience)
        print ("Retry9")
        
        Experience_Role_Titles=browser.find_elements_by_css_selector("#experience .item-title")
        Experience_Role_Titles_str = "(&) ".join(str(item.text) for item in Experience_Role_Titles)
        print ("Retry10")
        
        Experience_Company=browser.find_elements_by_css_selector("#experience .item-subtitle")
        Experience_Company_str = "(&) ".join(str(item.text) for item in Experience_Company)
        print ("Retry11")
        
        Connections=browser.find_elements_by_css_selector(".member-connections")
        Connections_str = "(&) ".join(str(item.text) for item in Connections)
        print ("Retry12")
        
        Experience_Dates=browser.find_elements_by_css_selector("#experience .meta")
        Experience_Dates_str = "(&) ".join(str(item.text) for item in Experience_Dates)
        print ("Retry13")
        
        School=browser.find_elements_by_css_selector(".school")
        School_str = "(&) ".join(str(item.text) for item in School)
            
        print ("Retry14")
        
        School_Name = browser.find_elements_by_css_selector("#education .item-title")
        School_Name_str = "(&) ".join(str(item.text) for item in School_Name)
        print ("Retry15")
        
        School_Course = browser.find_elements_by_css_selector("#education .item-subtitle")
        School_Course_str = "(&) ".join(str(item.text) for item in School_Course)
        print ("Retry16")
        
        School_Years =browser.find_elements_by_css_selector("#education .meta")  
        School_Years_str = "(&) ".join(str(item.text) for item in School_Years)
        print ("Retry17")
        
        list=Startup_name+"$%^"+URL+"$%^"+name_str+"$%^"+Top_Card_Title_str+"$%^"+Locality_str+"$%^"+Demographics_str+"$%^"+Tags_str+"$%^"+Profile_Summary_str+"$%^"+Profile_Preview_str+"$%^"+Summary_str+"$%^"+Experience_str+"$%^"+ Experience_Dates_str +"$%^"+ Connections_str +"$%^"+Experience_Company_str +"$%^"+Experience_Role_Titles_str+"$%^"+School_Years_str+"$%^"+School_Course_str+"$%^"+School_Name_str+"$%^"+School_str 
  
        data_split = list.split('$%^')
        df=pd.DataFrame(data_split)
        df_1=df.T
        issuedata_all=issuedata_all.append(df_1)
        
    except Exception:
        print ("Retry")
     

issuedata_all.to_csv(path, index=False, header=False, encoding = 'utf-8', mode='a')     

