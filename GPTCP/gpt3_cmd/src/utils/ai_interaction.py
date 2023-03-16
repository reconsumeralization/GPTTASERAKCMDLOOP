from typing import List, Tuple
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def interact_with_chat_website(driver, input_message: str) -> str:
    """
    Interacts with the chat.openai.com website using Selenium.
    """
    # Find the input field for the message
    input_field = driver.find_element_by_xpath("//input[@class='composer__input']")

    # Clear the input field and send the input message
    input_field.clear()
    input_field.send_keys(input_message)
    input_field.send_keys(Keys.RETURN)

    # Wait for the response message to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'response')][last()]"))
    )

    # Get the response message text
    response_message = driver.find_element_by_xpath("//div[contains(@class, 'response')][last()]").text

    return response_message
