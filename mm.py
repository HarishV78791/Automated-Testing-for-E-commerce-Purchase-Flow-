import random
import time
import pytest
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    edge_options = Options()
    driver = webdriver.Edge(options=edge_options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_tutorialsninja_purchase(driver):
    driver.get('http://tutorialsninja.com/demo/')
    
    search_box = driver.find_element(By.NAME, 'search')
    search_box.click()
    search_box.send_keys('HP LP3065')
    search_button = driver.find_element(By.XPATH, '//button[@class="btn btn-default btn-lg"]')
    search_button.click()
    time.sleep(2)

    HP = driver.find_element(By.XPATH, '//a[text()="HP LP3065"]')
    HP.click()
    first_pic = driver.find_element(By.XPATH, '//ul[@class="thumbnails"]/li[1]')
    first_pic.click()
    time.sleep(2)

    next_click = driver.find_element(By.XPATH, '//button[@title="Next (Right arrow key)"]')

    for i in range(3): 
        if i > 0:  
            next_click.click()
            time.sleep(2)
        screenshot_path = f'screenshot#{random.randint(0, 101)}.png'
        driver.save_screenshot(screenshot_path)
        print(f'Screenshot saved as {screenshot_path}')

    x_button = driver.find_element(By.XPATH, '//button[@title="Close (Esc)"]')
    x_button.click()
    time.sleep(2)

    add_to_button_2 = driver.find_element(By.XPATH, '//button[@id="button-cart"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", add_to_button_2)
    time.sleep(2)

    calendar = driver.find_element(By.XPATH, '//i[@class="fa fa-calendar"]')
    calendar.click()
    time.sleep(2)

    next_click_calendar = driver.find_element(By.XPATH, '//th[@class="next"]')
    month_year = driver.find_element(By.XPATH, '//th[@class="picker-switch"]')

    while month_year.text != 'December 2024':
        next_click_calendar.click()
        time.sleep(0.1)

    calendar_date = driver.find_element(By.XPATH, '//td[text()="31"]')
    calendar_date.click()
    time.sleep(2)

    add_to_button_2.click()
    time.sleep(2)

    go_to_cart = driver.find_element(By.ID, 'cart-total')
    go_to_cart.click()
    time.sleep(2)

    checkout = driver.find_element(By.XPATH, '//p[@class="text-right"]/a[2]')
    checkout.click()
    time.sleep(1)

    guest = driver.find_element(By.XPATH, '//input[@value="guest"]')
    guest.click()

    continue_1 = driver.find_element(By.ID, 'button-account')
    continue_1.click()
    time.sleep(2)

    driver.execute_script("arguments[0].scrollIntoView(true);", 
    driver.find_element(By.XPATH, '//a[text()="Step 2: Billing Details "]'))
    time.sleep(2)

    first_name = driver.find_element(By.ID, 'input-payment-firstname')
    first_name.send_keys('test_first_name')
    time.sleep(2)

    last_name = driver.find_element(By.ID, 'input-payment-lastname')
    last_name.send_keys('test_last_name')
    time.sleep(2)

    email = driver.find_element(By.ID, 'input-payment-email')
    email.send_keys('test@test.com')
    time.sleep(2)

    telephone = driver.find_element(By.ID, 'input-payment-telephone')
    telephone.send_keys('012345678')
    time.sleep(2)

    address = driver.find_element(By.ID, 'input-payment-address-1')
    address.send_keys('teststreet 187')
    time.sleep(2)

    city = driver.find_element(By.ID, 'input-payment-city')
    city.send_keys('Bangalore')
    time.sleep(2)

    postcode = driver.find_element(By.ID, 'input-payment-postcode')
    postcode.send_keys('560066')
    time.sleep(2)

    country = driver.find_element(By.ID, 'input-payment-country')
    dropdown_1 = Select(country)
    dropdown_1.select_by_index(106)  
    time.sleep(2)

    region = driver.find_element(By.ID, 'input-payment-zone')
    dropdown_2 = Select(region)
    dropdown_2.select_by_visible_text('Karnataka')
    time.sleep(2)

    continue_2 = driver.find_element(By.ID, 'button-guest')
    continue_2.click()
    time.sleep(2)

    continue_3 = driver.find_element(By.ID, 'button-shipping-method')
    continue_3.click()
    time.sleep(2)

    t_e = driver.find_element(By.NAME, 'agree')
    t_e.click()
    time.sleep(2)

    continue_4 = driver.find_element(By.ID, 'button-payment-method')
    continue_4.click()
    time.sleep(3)

    final_price = driver.find_element(By.XPATH, '//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]')
    assert "The final price of both products is " + final_price.text

    confirmation_button = driver.find_element(By.ID, 'button-confirm')
    confirmation_button.click()
    time.sleep(2)

    success_text = driver.find_element(By.XPATH, '//div[@class="col-sm-12"]/h1')
    assert success_text.text == 'Your order has been placed!'
    time.sleep(2)
