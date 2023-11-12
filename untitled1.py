# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 18:36:54 2023

@author: CASPER
"""

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# WebDriver hizmetini başlat (Edge için)
service = Service("C:/Users/Cengiz/Desktop/msedgedriver.exe")

# WebDriver'ı başlat ve hizmeti kullan
edge_options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=edge_options)

# Web sitesini aç
url = "https://www.researchgate.net/search.Search.html?query=&type=publication"
driver.get(url)

# Read names from hocalar.txt
with open("hocalar.txt", "r", encoding="utf-8") as names_file:
    names = names_file.read().splitlines()

# Loop through each name and perform the scraping
for person in names:
    wait = WebDriverWait(driver, 30)

    # İlgili XPath'teki input alanına metni gir
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/form/div[2]/input"))
    )
    
    input_element.clear()
    input_element.send_keys(person)

    # İlgili XPath'teki butona tıkla
    button_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/form/div[2]/button[1]"))
    )
    button_element.click()

    link_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[1]/div/a[2]"))
    )
    link_element.click()

    xpath = "/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[1]/div/a"
    link_element1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    link_element1.click()

    element = driver.find_element(By.XPATH, "/html/body/div/main/section[3]/div[1]/div[1]/div").text
    
   
    with open("veriler.txt", "a", encoding="utf-8") as txt_file:
        txt_file.write("\n\n")
        txt_file.write(person + "\n")
        txt_file.write(element + "\n")
        txt_file.write("\n\n")
        print(f"Veriler metin dosyasına eklenmiştir ({person}).")
        driver.back()
        


# Close the WebDriver
driver.quit()
