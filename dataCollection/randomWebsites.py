import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse

# Specify the path to the text file containing the list of websites
website_list_file = "random_websites_list.txt"

# Read the website list from the text file
with open(website_list_file, "r") as file:
    websites = file.readlines()

# Remove any leading/trailing whitespace from website names
websites = [website.strip() for website in websites]

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (without GUI)

# Set up the Chrome web driver
driver_path = "path/to/chromedriver"  # Specify the path to your Chrome driver executable
service = Service(driver_path)

for website in websites:
    # Add "http://" prefix if it is not present in the URL
    parsed_url = urlparse(website)
    if parsed_url.scheme == "":
        website = "http://" + website

    try:
        # Initialize the Chrome driver
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open the website in Chrome
        driver.get(website)

        # Wait for the website to fully load (you can adjust the duration if needed)
        time.sleep(5)

        # Close the browser window
        driver.quit()

        # Wait for a brief interval before opening the next website
        time.sleep(1)
    
    except Exception as e:
        print(f"Error occurred while opening {website}: {str(e)}")
        print("Skipping to the next website...")
