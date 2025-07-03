import time, json, sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


from webdriver_manager.chrome import ChromeDriverManager


# Set up the Chrome options

# debugging = False
# or
debugging = True

chrome_options = Options()
if debugging:
    chrome_options.add_experimental_option("detach", True)
else:
    chrome_options.add_argument("--headless")


def wait_for_element(driver, by, element_identifier, timeout=5):
    element_present = EC.presence_of_element_located((by, element_identifier))
    WebDriverWait(driver, timeout).until(element_present)
    return driver.find_element(by, element_identifier)


# Set up the ChromeDriver service
# Set up the WebDriver
# service = Service("/Users/jc/toy/selenium/chromedriver-mac-x64-3/chromedriver")
# driver = webdriver.Chrome(service=service, options=chrome_options)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


# Step 1: Access the login page
# login_page = 'https://mpo.keiho-u.ac.jp/portfolio/index.jsp'
# login_page_unipa = "https://unipa.keiho-u.ac.jp/uprx/up/pk/pky001/Pky00101.xhtml"
# driver.get(login_page_unipa)

# # Set up ChromeOptions
# options = Options()
# options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)

# # Set up the ChromeDriver service
# service = Service(ChromeDriverManager().install())

# # Initialize the driver with the service and options
# driver = webdriver.Chrome(service=service, options=options)

# Open the URL
url = "https://www.youtube.com/watch?v=kbGu60QBx2o"
driver.get(url)

# Wait for the page to fully load (you may need to adjust the wait time)
driver.implicitly_wait(10)

input()

with open("out_from_sele.py", "w", encoding="utf-8") as f:
    f.write("<!DOCTYPE html>\n")
    f.write('<html lang="ja">\n')
    f.write("<head>\n")
    f.write('<meta charset="UTF-8">\n')  # Specify UTF-8 encoding
    f.write("</head>\n")
    f.write("<body>\n")
    f.write(driver.page_source)
    f.write("</body>\n")
    f.write("</html>\n")


# Print the text content after the page has loaded
# html_content = driver.page_source

# # Save the HTML content to a file
# # with open("output.html", "w", encoding="utf-8") as file:
# with open("output.html", "w") as file:
#     file.write(html_content)

# # Close the browser
driver.quit()
