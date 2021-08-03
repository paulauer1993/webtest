import time

from robot.api import logger
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("./chrome_driver/chromedriver.exe")
driver.maximize_window()


def click_button(name):
    driver.find_element_by_class_name(name).click()
    time.sleep(1)


def write_to_text_box(textbox, text_to_write):
    input_box = driver.find_element_by_id(textbox)
    input_box.click()
    input_box.send_keys(text_to_write)
    time.sleep(1)


def submit(button_name):
    driver.find_element_by_name(button_name).click()
    time.sleep(1)


def click_radio_button(value):
    time.sleep(2)
    driver.find_element_by_css_selector(f"input#{value}").click()
    time.sleep(1)


def drop_box_navigate(dropbox, value):
    box = Select(driver.find_element_by_id(dropbox))
    box.select_by_value(value)
    time.sleep(1)


def click_span(span):
    driver.find_element_by_xpath(span).click()
    time.sleep(5)


def get_div_table_text(xpath):
    table = driver.find_element_by_xpath(xpath)
    all_li = table.find_elements_by_tag_name("li")
    return_list = []
    for li in all_li:
        text = li.text
        return_list.append(text)
    return return_list

