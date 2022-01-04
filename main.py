# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 16:30:13 2022

@author: dtrelles
"""

import Scrapper as sc
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import pickle



Wait_time = 5 # necesita esperar entre cada request para que no cierren la cuenta


#Importar Directorio
path = r''
directorio = pd.read_excel(path + r'\links.xlsx', sheet_name = 'directorio', index_col = 0)
directorio.dropna(how='all', axis=1, inplace=True)
directorio = directorio.transpose()
seguidores = pd.DataFrame(index = directorio.index, columns = directorio.columns)



# open browser
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#Scrapping

#Facebook
driver.get("http://www.facebook.com")
cookies = pickle.load(open(path + r"\facebook_cookies.pkl", "rb"))
print('Facebook')
for cookie in cookies:
    driver.add_cookie(cookie)
for compania in directorio.columns:
    seguidores[compania]['Facebook'] = sc.fb_followers_scrapper(directorio[compania]['Facebook'],Wait_time)


#Instagram
driver.get("http://www.instagram.com")
cookies = pickle.load(open(path + r"\instagram_cookies.pkl", "rb"))
print('Instagram')
for cookie in cookies:
    driver.add_cookie(cookie)
for compania in directorio.columns:
    seguidores[compania]['Instagram'] = sc.instagram_followers_scrapper(driver,directorio[compania]['Instagram'],Wait_time)


#Linkedin
driver.get("http://www.linkedin.com")
cookies = pickle.load(open(path + r"\linkedin_cookies.pkl", "rb"))
print('Linkedin')
for cookie in cookies:
    driver.add_cookie(cookie)
for compania in directorio.columns:
    seguidores[compania]['Linkedin'] = sc.linkedin_followers_scrapper(driver,directorio[compania]['Linkedin'],Wait_time)
    

#Youtube
print('youtube')
for compania in directorio.columns:    
    seguidores[compania]['Youtube'] = sc.youtube_followers_scrapper(driver,directorio[compania][ 'Youtube'],Wait_time)
    
    
    
    
    
    
driver.close()