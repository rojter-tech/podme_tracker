from __future__ import unicode_literals
import os, re, sys, json, codecs
from seleniumwire import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from time import sleep

PODME_URL=r'https://podme.com/'

LOGIN_PAGE=r'/html/body/div/div/div[1]/nav/button'
EMAIL=r'//*[@id="logonIdentifier"]'
PASSWORD=r'//*[@id="password"]'
LOGIN=r'//*[@id="next"]'
MY_PODCASTS=r'/html/body/div/div/nav/div[2]/a[2]'
FOOTER=r'/html/body/div/div/footer'


def store_dict_as_json(dictionary, filepath):
    path = os.path.dirname(filepath)
    if not os.path.exists(path):
        os.mkdir(path)
    with codecs.open(filepath, 'w', "utf-8") as f:
        json_string = json.dumps(dictionary, sort_keys=True, indent=4, ensure_ascii=False)
        f.write(json_string)

def wait_for_access(driver, XPATH, timer=20):
    element = WebDriverWait(driver, timer).until(
    EC.element_to_be_clickable((By.XPATH, XPATH)))
    return element


def establish_connection():
    driver = webdriver.Firefox(seleniumwire_options={'verify_ssl': False})
    driver.get(PODME_URL)

    wait_for_access(driver, LOGIN_PAGE, timer=20).click()
    wait_for_access(driver, EMAIL, timer=20).send_keys('kixalak392@nuevomail.com')
    wait_for_access(driver, PASSWORD, timer=20).send_keys('DownloadPodme123')
    wait_for_access(driver, LOGIN, timer=20).click()
    wait_for_access(driver, MY_PODCASTS, timer=20)

    return driver