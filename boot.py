from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

cancion = input ("Ingrese la cancion que desea")

#Opciones de navegacion

options=webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path='C:\chromedriver-win64.exe'
driver=webdriver.Chrome()

#Inicializar el navegador
driver.get("https://www.youtube.com")
WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#search')))\
    .send_keys(cancion)

WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button#search-icon-legacy')))\
    .click()
WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'yt-formatted-string.style-scope.ytd-video-renderer')))\
    .click()
WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div')))\
    .click()
WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-unified-share-panel-renderer/div[2]/yt-third-party-network-section-renderer/div[2]/yt-copy-link-renderer/div/yt-button-renderer/yt-button-shape')))\
    .click()
##Desicion del usuario
desea= input ("Desea descargarlo en mp3 o mp4")
if desea=="mp3":(
driver.get("https://www.y2mate.com/es736/youtube-mp3"),

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       'input#txt-url'))) \
    .send_keys(Keys.CONTROL + "v"),
WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[4]/div[1]/div[2]/div/div/div[2]/button')))\
    .click(),
WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div/a')))\
    .click())
elif desea=="mp4":(
    driver.get("https://greenconvert.net/en6/youtube-to-mp4"),
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/main/section[1]/div/div[1]/input'))) \
        .send_keys(Keys.CONTROL + "v"),
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/main/section[1]/div/div[1]/div/button'))) \
        .click(),
    
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/main/section[1]/div/div[5]/div[2]/div/div[2]/div/div[1]/select'))) \
        .click(),
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/main/section[1]/div/div[5]/div[2]/div/div[2]/div/div[1]/select/optgroup[1]/option[1]'))) \
        .click(),
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/main/section[1]/div/div[5]/div[2]/div/div[2]/div/a'))) \
        .click(),
)
else :(
    print("Dato ingresado invalido")
)
time.sleep(120)
