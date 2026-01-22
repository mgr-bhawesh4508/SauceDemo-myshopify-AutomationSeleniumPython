# # Import the selenium webdriver module - this allows us to control web browsers
# import os
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Import the By module - this helps us find elements on web pages
# from selenium.webdriver.common.by import By
#
# # Import the Service class - this manages the driver executable
# from selenium.webdriver.chrome.service import Service
#
# # Import the Options class - this allows us to customize browser settings
# from selenium.webdriver.chrome.options import Options
#
# # Import the time module - this lets us add delays between actions
# import time
#
# # Import allure for generating detailed test reports
# # Allure provides beautiful reports with steps, attachments, and test status
# import allure
#
# # Create Chrome options object to customize browser behavior
# chrome_options = Options()
#
# # Add argument to start the browser maximized (full screen)
# chrome_options.add_argument("--start-maximized")
#
# #for headless and jenkins
# chrome_options.add_argument("--headless=new")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
#
#
#
# # Create a service object pointing to the ChromeDriver executable
# # This is the file that connects our script to the Chrome browser
# service = Service(r"C:\Users\97155\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
#
# # Create a webdriver instance using Chrome with our options and service
# # This opens a new Chrome browser window for automation
# driver = webdriver.Chrome(service=service, options=chrome_options)
#
# # Navigate to the Sauce Demo website - this is our test website
# driver.get('https://sauce-demo.myshopify.com')
#
# # Define a function to click on elements using their XPATH
# # XPATH is a way to locate elements on a webpage
# # Allure step annotation provides reporting for this action
#
# # BaseClass
# @allure.step("Click on element with xpath: {xpath}")
# def test_click_element(driver, xpath):
#     # Find the element on the page using its XPATH
#     element = driver.find_element(By.XPATH, xpath)
#     # Assert that the element is present
#     assert element.is_displayed(), f"Element with xpath {xpath} is not displayed"
#     # Click on the found element
#     element.click()
#     print(f"Successfully clicked on element: {xpath}")
#
# # Define a function to enter text into input fields
# # Allure step annotation provides reporting for this action
# @allure.step("Send keys '{keys}' to element with xpath: {xpath}")
# def test_send_keys_to_element(driver, xpath, keys):
#     # Find the element on the page using its XPATH
#     element = driver.find_element(By.XPATH, xpath)
#     # Assert that the element is present and enabled
#     assert element.is_enabled(), f"Element with xpath {xpath} is not enabled"
#     # Clear any existing text in the field
#     element.clear()
#     # Enter the new text into the field
#     element.send_keys(keys)
#     test_take_screenshot()
#     print(f"Successfully sent keys '{keys}' to element: {xpath}")
#
# # Define a function to assert that an element exists
# # Allure step annotation provides reporting for this assertion
# @allure.step("Assert element exists with xpath: {xpath}")
# def test_assert_element_exists(driver, xpath, timeout=10):
#     try:
#         WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
#         element = driver.find_element(By.XPATH, xpath)
#         assert element.is_displayed(), f"Element with xpath {xpath} is not visible"
#         print(f"Assertion passed: Element {xpath} exists and is visible")
#         return True
#     except:
#         print(f"Assertion failed: Element {xpath} does not exist or is not visible")
#         return False
#
# # # Navigate to the registration page
# # SignUp = "//a[contains(text(),'Sign up')]"
# # click_element(driver, SignUp)
# # print("Clicked on Sign Up link")
# #
# # # wait for navigate to registration
# # time.sleep(2)
# #
# # # Verify registration page opens properly by checking the URL
# # if "register" in driver.current_url:
# #     print("Registration form loaded successfully")
# # else:
# #     print("Warning: Registration form may not have loaded properly - current URL:",driver.current_url)
# #
# # FirstName = "//input[@id='first_name']"
# # send_keys_to_element(driver, FirstName, "Bhawesh")
# # print("First name entered")
# #
# # LastName = "//input[@id='last_name']"
# # send_keys_to_element(driver,LastName, "Magar")
# # print("Last name entered")
# #
# # Email= "//input[@id='email']"
# # unique_email = f"testuser_{int(time.time())}@gmail.com"
# # send_keys_to_element(driver, Email, unique_email)
# # print("Email entered")
# #
# # Password = "//input[@id='password']"
# # send_keys_to_element(driver, Password, "Mgr@bhawesh4508")
# # print("Password Entered")
# #
# # CreateButton = "//input[@type='submit' and @value='Create']"
# # click_element(driver, CreateButton)
# # print("Clicked on Create button")
# #
# # # Assert that registration was successful by checking the URL first,then for the presence of the Log out element
# # time.sleep(30)
# #
# # # Check if redirected to account page first (primary indicatroot redirected,check for the presence of the Log out element as secondary indicator
# # logout_element = driver.find_element(By.XPATH,"//div[@class='seven columns offset-by-one desktop']//a[@id='customer_logout_link']")
# # if logout_element:
# #     print("Registration successful - Log Out element found")
# # else:
# #     print("Registration is not successful - No redirect and Log Out element not found")
#
# login_search_data = [
# {
#
#     "email": "nepal@gmail.com",
#     "password": "ABCDE@12345",
#     "search_term": "grey jacket"
# }
# # {
# #     "email" : "testuser45@gmail.com",
# #     "password" : "Password@45",
# #     "search_term": "jacket"
# # },
# # {
# #     "email": "testtest45@gmail.com",
# #     "password": "Hunnybunny@45",
# #     "search_term": "jeans"
# # }
# ]
#
# for i,user_data in enumerate(login_search_data):
#     # login_link = "//a[@id='customer_login_link']"
#     # click_element(driver, login_link)
#     # print("Clicked on Log In link")
#     #
#     # email_input= "//input[@id='customer_email']"
#     # send_keys_to_element(driver,email_input,user_data["email"])
#     # print(f"Email entered: {user_data['email']}")
#     #
#     # passwrod_input= "//input[@id='customer_password']"
#     # send_keys_to_element(driver,passwrod_input,user_data["password"])
#     # print("Password entered")
#     #
#     # sign_in_button= "//input[@value='Sign In']"
#     # click_element(driver,sign_in_button)
#     # print("Clicked on Sign In button")
#     #
#     # time.sleep(500)
#
#     search_input= "//input[@id='search-field']"
#     test_send_keys_to_element(driver,search_input,user_data["search_term"])
#     print(f"Product Searched:{user_data['search_term']}")
#     time.sleep(3)
#
#     search_button= "//input[@id='search-submit']"
#     test_click_element(driver,search_button)
#     print("Product is Searched")
#     time.sleep(3)
#
#     search_product= "//div[@class='four columns alpha']"
#     test_click_element(driver,search_product)
#     print("Product is clicked")
#
#     add_to_cart_button= "//input[@id='add']"
#     test_click_element(driver,add_to_cart_button)
#     print("Added to cart")
#     time.sleep(2)
#
#     checkout_link= "//a[normalize-space()='Check Out']"
#     test_click_element(driver,checkout_link)
#     print("Checkout button is clicked")
#     time.sleep(3)
#
#     checkout_button= "//input[@id='checkout']"
#     test_click_element(driver,checkout_button)
#     print("Product is checked out")
#     time.sleep(3)
#
#     # SignIn_link= "//a[normalize-space()='Sign in']"
#     # click_element(driver,SignIn_link)
#     # print("Signin link is clicked")
#     # time.sleep(3)
#     #
#     # Email_input= "//input[@id='customer_email']"
#     # send_keys_to_element(driver,Email_input,"nepal@gmail.com")
#     # print("Email is entered")
#     #
#     # Password_input="//input[@id='customer_password']"
#     # send_keys_to_element(driver,Password_input,"ABCDE@12345")
#     # print("Password is entered")
#     #
#     # SignIn_button= "//input[@value='Sign In']"
#     # click_element(driver,SignIn_button)
#     # print("Sign In button is clicked")
#
#
#
# # wait for page to load
# time.sleep(60)
# # implicit wait
# with allure.step("Taking screenshot"):
#     def test_take_screenshot(self: object, name: object = "screenshot", timestamp: object = True) -> None:
#         screenshots_dir = "screenshots"
#         if not os.path.exists(screenshots_dir):
#             os.makedirs(screenshots_dir)
#
#         if timestamp:
#             timestamp_str = int(time.time())
#             filename = f"{screenshots_dir}/{name}_{timestamp_str}.png"
#         else:
#             filename = f"{screenshots_dir}/{name}.png"
#
#         self.driver.save_screenshot(filename)
#
#         allure.attach.file(
#             filename,
#             name= name,
#             attachment_type=allure.attachment_type.PNG,
#     )
# # print(f"Screenshot taken: {filename}")
#
# # close browser
# driver.quit()