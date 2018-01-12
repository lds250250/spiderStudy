import re

from config import CHROMEDRIVER
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Taobao(object):
    def __init__(self):
        self.wait = WebDriverWait(browser, 10)

    def __search(self):
        try:
            browser.get('http://www.taobao.com')
            input = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
            submit = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR,
                     '#J_TSearchForm > div.search-button > button')))
            input.send_keys('美食')
            submit.click()
            total = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR,
                     "#mainsrp-pager > div > div > div > div.total")))
            return total.text
        except TimeoutException:
            return self.__search()

    def go(self):
        total = self.__search()
        total = int(re.compile('(\d+)').search(total).group(1))


if __name__ == '__main__':
    browser = webdriver.Chrome(CHROMEDRIVER)
    taobao = Taobao()
    taobao.go()
