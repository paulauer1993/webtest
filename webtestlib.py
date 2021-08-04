import time

from robot.api import logger
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("./chrome_driver/chromedriver.exe")
driver.maximize_window()


def click_button(name):
    """
    :goal: searches button by class name
    :param name: class name to be searched
    :type name: str
    :return: None
    """
    driver.find_element_by_class_name(name).click()
    time.sleep(1)


def write_to_text_box(textbox, text_to_write):
    """
    :goal: searches textbox by id and writes to them
    :param textbox: textbox to be searched
    :type textbox: str
    :param text_to_write: text to be entered in textbox
    :type text_to_write: str
    :return: None
    """
    input_box = driver.find_element_by_id(textbox)
    input_box.click()
    input_box.send_keys(text_to_write)
    time.sleep(1)


def submit(button_name):
    """
    :goal: searches element by name
    :param button_name: name of the element
    :type: str
    :return: None
    """
    driver.find_element_by_name(button_name).click()
    time.sleep(1)


def click_radio_button(value):
    """
    :goal: finds element by css selector
    :param value: value of the element to be searched
    :type value: str
    :return: None
    """
    time.sleep(3)
    driver.find_element_by_css_selector(f"input#{value}").click()
    time.sleep(1)


def drop_box_navigate(dropbox, value):
    """
    :goal: navigates drop-boxes by id
    :param dropbox: dropbox's id
    :type dropbox: str
    :param value: value to be entered
    :type value: str
    :return: None
    """
    box = Select(driver.find_element_by_id(dropbox))
    box.select_by_value(value)
    time.sleep(1)


def click_span(span):
    """
    :goal: clicks on a span
    :param span: xpath to the span
    :type span: str
    :return: None
    """
    driver.find_element_by_xpath(span).click()
    time.sleep(1)


def get_div_table_text(xpath):
    """
    :goal: lists all the values of a table
    :param xpath: xpath to the table
    :type xpath: str
    :return: all values inside a table
    :rtype: list
    """
    table = driver.find_element_by_xpath(xpath)
    all_li = table.find_elements_by_tag_name("li")
    return_list = []
    for li in all_li:
        return_list.append(li.text)
    return return_list

