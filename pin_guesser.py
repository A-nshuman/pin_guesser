from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

def generate_pin():
    pin = random.randint(1000, 9999)
    return pin

def main():
    driver = webdriver.Edge(executable_path='C:\')

    driver.get("https://www.guessthepin.com/")

    while True:
        pin = generate_pin()
        print(pin)

        input_element = driver.find_element_by_css_selector("#input")

        input_element.send_keys(str(pin))

        input_element.send_keys(Keys.RETURN)

        time.sleep(1)

    driver.quit()

if __name__ == "__main__":
    main()
