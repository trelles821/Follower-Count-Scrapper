# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 15:13:28 2021

@author: dtrelles
"""
#Funciones para hacer scrapping

import time
import requests
import bs4
import re
from random import uniform






#scrappers
def instagram_followers_scrapper(browser,link,Wait_time):
    if type(link) == str:
        try:
            browser.get('https://instagram.com/'+link)
            time.sleep(Wait_time*uniform(0.8,1.2))
            element = browser.find_element_by_partial_link_text('seguidores').text
            match = re.search('[0-9.km]+ seguidores', element)
            raw_string = match.group().split()[0].replace('.','')
            if 'k' in raw_string:
                seguidores = int(1000 * float(raw_string.replace(',','.').replace('k','')))
            else:
                seguidores = int(raw_string.replace(',','').replace('.',''))
        except:
            print('fallo el instagram de %s.' %link)
            seguidores = 0
    else:
        seguidores = 0
    return seguidores

def youtube_followers_scrapper(browser,link,Wait_time):
    if type(link) == str:
        try:
            browser.get('https://www.youtube.com/'+link)
            time.sleep(Wait_time*uniform(0.8,1.2))
            raw_string = browser.find_element_by_id('subscriber-count')
            seguidores = int(raw_string.text.split()[0].replace(',',''))
        except:
            print('fallo el youtube de %s.' %link)
            seguidores = 0
    else:
        seguidores = 0
    return seguidores

def linkedin_followers_scrapper(browser, link,Wait_time):
    if type(link) == str:
        try:
            browser.get('https://mx.linkedin.com/company/'+ link)
            time.sleep(Wait_time*uniform(0.8,1.2))
            element = browser.find_element_by_partial_link_text('seguidores').text
            match = re.search('[0-9.,]+ seguidores', element)
            #element = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/div[2]')
            #match = element.text.split()[0]
            seguidores = int(match.group().split()[0].replace('.',''))
        except:
            print('fallo el linkedin de %s.' %link)
            seguidores = 0
    else:
        seguidores = 0
    return seguidores

def fb_followers_scrapper(link,Wait_time):
    if type(link) == str:
        try:
            res = requests.get('https://www.facebook.com/'+link)
            time.sleep(Wait_time*uniform(0.8,1.2))
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            match = re.search('[0-9.]+ personas siguen esto', soup.text)
            seguidores = int(match.group().split()[0].replace('.',''))
        except:
            print('fallo el facebook de %s.' %link)
            seguidores = 0
    else:
        seguidores = 0
    return seguidores








    
