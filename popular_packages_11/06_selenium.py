from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

# Open Github site
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.implicitly_wait(10)
browser.get('https://github.com')

# Click on Sign In option
link = browser.find_element(By.LINK_TEXT, 'Sign in')
link.click()

# Fill credentials and sign up
user_input = browser.find_element(By.ID, 'login_field')
pwd_input = browser.find_element(By.ID, 'password')
user_input.send_keys('ljloaizap')
pwd_input.send_keys(os.getenv('GITHUB_PWD'))

# login
pwd_input.send_keys(Keys.RETURN)

# get logged-in user
profile = browser.find_element(
    By.CLASS_NAME,
    'css-truncate-target'
)
label = profile.get_attribute('innerHTML')

# assert 'ljloaizap' in label  # didn't work .-.
