# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service
# import time
#
# # Replace with the actual path to your msedgedriver.exe
# edge_driver_path = r"C:\drivers\msedgedriver.exe"  # <-- Update this path
#
# # Set up the Edge driver
# service = Service(executable_path=edge_driver_path)
# driver = webdriver.Edge(service=service)
#
# try:
#     # Open the website
#     driver.get("https://xenqu.com/#login/logout")
#     time.sleep(3)  # Wait for the page to load; adjust the delay as needed
#
# #     # Locate the username field and enter the username
# #     # (Update the locator below if the actual element identifier is different)
# #     username_field = driver.find_element(By.ID, "username")
# #     username_field.clear()
# #     username_field.send_keys("Grayni")
# #
# #     # Locate the password field and enter the password
# #     # (Update the locator below if necessary)
# #     password_field = driver.find_element(By.ID, "password")
# #     password_field.clear()
# #     password_field.send_keys("Nadia@124")
# #
# #     # Locate and click the login button
# #     # (The XPath below assumes the login button is a <button> with type 'submit'. Adjust if needed.)
# #     login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
# #     login_button.click()
# #
# #     # Wait for login to complete; adjust delay if necessary
# #     time.sleep(5)
# #
# #     # You can add further steps here (like validations, further navigation, etc.)
# #
# # finally:
# #     # Close the browser
# #     driver.quit()
# ----------------------------------------
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

# Replace with the actual path to your msedgedriver.exe
edge_driver_path = r"C:\drivers\msedgedriver.exe"

# Set up the Edge driver service
service = Service(executable_path=edge_driver_path)

# Initialize the Edge driver
driver = webdriver.Edge(service=service)

try:
    # Open the website
    driver.get("https://xenqu.com/#login/logout")
    time.sleep(10)  # Wait for 3 seconds so you can see the page


finally:
    # Close the browser
    driver.quit()
