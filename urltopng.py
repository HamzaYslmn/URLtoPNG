from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import concurrent.futures
import time
import os

def capture_full_page_screenshot(url, output_file):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    service = Service()  # Specify the path to chromedriver if not in PATH
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)  # Adjust based on the expected load time of the page
        
        required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        driver.set_window_size(required_width, required_height)
        time.sleep(2)  # Wait for the resize to take effect

        driver.find_element(By.TAG_NAME, 'body').screenshot(output_file)
    finally:
        driver.quit()

if not os.path.exists('PNG'):
    os.makedirs('PNG')

def process_url(index, url):
    output_file = f'PNG/output_{index}.png'
    capture_full_page_screenshot(url, output_file)
    print(f"Screenshot captured for {url}")

def main():
    with open('a.txt', 'r') as file:
        urls = [url.strip() for url in file.readlines()]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Using enumerate(urls) to keep track of each URL's index
        executor.map(lambda args: process_url(*args), enumerate(urls))

if __name__ == "__main__":
    main()
