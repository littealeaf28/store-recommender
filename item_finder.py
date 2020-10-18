import math
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


def cost_calculate(store, shopping_list):
    availabilities = []
    costs = []
    for item in shopping_list:
        available_and_cost = item_cost(store, item)
        availabilities.append(available_and_cost[0])
        costs.append(available_and_cost[1])
    return [sum(availabilities)/len(availabilities), sum(costs)]

# The store is a formatted address string
# The item is a string corresponding to the item codes defined below in 'code_to_item'
def item_cost(store, item_code):
    store_address = store.split()
    store_building_no = store_address[0]
    store_zip_code = store_address[len(store_address) - 2][0:(len(store_address) - 1)]
    to_search_through = get_SKUs(item_code)
    availabilities = []
    costs = []
    settings = Options()
    settings.headless = True
    with webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=settings) as driver:
        index = 1
        for sku in to_search_through[0:2]:
            driver.get("https://brickseek.com/walmart-inventory-checker/")
            try:
                WebDriverWait(driver, 2).until(ec.presence_of_element_located(
                    (By.CSS_SELECTOR, "input#inventory-checker-form-sku")
                ))
            except TimeoutException:
                break
            driver.find_element_by_css_selector("input#inventory-checker-form-sku").send_keys(sku)
            if index == 1:
                driver.find_element_by_css_selector("input#inventory-checker-form-zip.location-control__input").send_keys(store_zip_code)
                index = index + 1
            driver.find_element_by_css_selector("button.bs-button").click()
            try:
                WebDriverWait(driver, 2).until(ec.presence_of_element_located(
                    (By.CSS_SELECTOR, "address.address")
                ))
            except TimeoutException:
                continue
            store_addresses = driver.find_elements_by_css_selector("address.address")
            store_availabilities = driver.find_elements_by_css_selector("span.availability-status-indicator__text")
            store_costs = driver.find_elements_by_css_selector("span.price-formatted.price-formatted--style-display")
            counter = 0
            for store in store_addresses:
                address_elements = store.text.split('\n')
                if address_elements[0].split()[0].strip() == store_building_no and address_elements[1].split()[2].strip() == store_zip_code:
                    availabilities.append(text_to_availability(store_availabilities[counter]))
                    costs.append(float(store_costs[counter].text.replace("\n", "")[1:]))
                    break
                counter = counter + 1
    if any(availabilities):
        min_cost = math.inf
        for n in range(len(costs)):
            if availabilities[n]:
                min_cost = min_cost if min_cost < costs[n] else costs[n]
        return [True, min_cost]
    return [False, 0]


# Takes food code input and converts it into a list of product SKUs
def get_SKUs(item_code):
    settings = Options()
    settings.headless = True
    with webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=settings) as driver:
        driver.get("https://brickseek.com/walmart-inventory-checker/")
        try:
            WebDriverWait(driver, 2).until(ec.presence_of_element_located(
                (By.CSS_SELECTOR, "span.inventory-checker-form__launch-sku-finder.js-link")
            ))
        except TimeoutException:
            return []
        driver.find_element_by_css_selector("span.inventory-checker-form__launch-sku-finder.js-link").click()
        driver.find_element_by_id("sku-finder-form-query").send_keys(code_to_item(item_code))

        driver.find_element_by_class_name("sku-finder-form__submit").click()
        WebDriverWait(driver, 2).until(ec.presence_of_element_located(
            (By.CLASS_NAME, "sku-finder-form-results__link")
        ))

        searchables = driver.find_elements_by_class_name("sku-finder-form-results__name")
        skus = []
        for item in searchables:
            skus.append(item.text.split('\n')[1].split()[1])

    return skus


def text_to_availability(availability_test):
    if availability_test.text.strip() == "In Stock":
        return True
    else:
        return False


# Hard coding certain items
def code_to_item(item_code):
    if item_code == "milk":
        return "milk gallon"
    if item_code == "soda":
        return "coca cola"
    if item_code == "cereal":
        return "cereal"
    if item_code == "frozen dinner":
        return "frozen dinner"
    if item_code == "snacks":
        return "cheeto"
    if item_code == "detergent":
        return "detergent"
    if item_code == "eggs":
        return "great value eggs 12 count"
    if item_code == "bread":
        return "great value bread"
    return item_code