# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 09:38:59 2021

@author: dtrelles
"""
#Este script se usa para guardar cuentas de instagram, linkedin, y fb para que use el Scrapper.
#Se debe iniciar sesion y guardarla en cada una de estas paginas antes de correr este codigo
#Se debe cambiar la direccion por la direccion en la que se guarda la info de tu google chrome

import pickle
import selenium.webdriver 

original_data_path = r''
path = r''
options = selenium.webdriver.ChromeOptions()
options.add_argument(original_data_path)
driver = selenium.webdriver.Chrome(options = options)
driver.get("http://www.instagram.com")
pickle.dump( driver.get_cookies() , open(path + r"\instagram_cookies.pkl","wb"))

driver.get("http://www.linkedin.com")
pickle.dump( driver.get_cookies() , open(path + r"\linkedin_cookies.pkl","wb"))

driver.get("http://www.facebook.com")
pickle.dump( driver.get_cookies() , open(path + r"\facebook_cookies.pkl","wb"))


