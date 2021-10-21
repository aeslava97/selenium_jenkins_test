from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def init_driver():
    driver = webdriver.Chrome("C:\\Users\\amilk\\Documents\\studying\\QA\\chromedriver.exe")
    return driver

def get_website(driver):
    driver.get("https://qainterview.pythonanywhere.com/")

def form_submit(driver):
    login_form = driver.find_element_by_id('number')
    login_form.send_keys('5')

    button_calc = driver.find_element_by_id('getFactorial')
    actions = ActionChains(driver)
    actions.click(button_calc).perform()

def get_ans_form():
    driver = init_driver()
    get_website(driver)
    form_submit(driver)

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "resultDiv"), ":")
    )
    button_calc = driver.find_element_by_id('resultDiv')
    a = int(button_calc.text.split(":")[1])
    driver.close()
    return a

