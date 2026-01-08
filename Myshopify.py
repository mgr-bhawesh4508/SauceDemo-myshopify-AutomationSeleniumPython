from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

service = Service(r"C:\Users\97155\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver= webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://sauce-demo.myshopify.com")
time.sleep(5)

def click_element(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    element.click()

def send_keys_to_element(driver, xpath, keys):
    element = driver.find_element(By.XPATH, xpath)
    element.clear()
    element.send_keys(keys)

# # Navigate to the registration page
# SignUp = "//a[contains(text(),'Sign up')]"
# click_element(driver, SignUp)
# print("Clicked on Sign Up link")
#
# # wait for navigate to registration
# time.sleep(2)
#
# # Verify registration page opens properly by checking the URL
# if "register" in driver.current_url:
#     print("Registration form loaded successfully")
# else:
#     print("Warning: Registration form may not have loaded properly - current URL:",driver.current_url)
#
# FirstName = "//input[@id='first_name']"
# send_keys_to_element(driver, FirstName, "Bhawesh")
# print("First name entered")
#
# LastName = "//input[@id='last_name']"
# send_keys_to_element(driver,LastName, "Magar")
# print("Last name entered")
#
# Email= "//input[@id='email']"
# unique_email = f"testuser_{int(time.time())}@gmail.com"
# send_keys_to_element(driver, Email, unique_email)
# print("Email entered")
#
# Password = "//input[@id='password']"
# send_keys_to_element(driver, Password, "Mgr@bhawesh4508")
# print("Password Entered")
#
# CreateButton = "//input[@type='submit' and @value='Create']"
# click_element(driver, CreateButton)
# print("Clicked on Create button")
#
# # Assert that registration was successful by checking the URL first,then for the presence of the Log out element
# time.sleep(30)
#
# # Check if redirected to account page first (primary indicatroot redirected,check for the presence of the Log out element as secondary indicator
# logout_element = driver.find_element(By.XPATH,"//div[@class='seven columns offset-by-one desktop']//a[@id='customer_logout_link']")
# if logout_element:
#     print("Registration successful - Log Out element found")
# else:
#     print("Registration is not successful - No redirect and Log Out element not found")

login_search_data = [
{

    "email": "nepal@gmail.com",
    "password": "ABCDE@12345",
    "search_term": "grey jacket"
}
# {
#     "email" : "testuser45@gmail.com",
#     "password" : "Password@45",
#     "search_term": "jacket"
# },
# {
#     "email": "testtest45@gmail.com",
#     "password": "Hunnybunny@45",
#     "search_term": "jeans"
# }
]

for i,user_data in enumerate(login_search_data):
    # login_link = "//a[@id='customer_login_link']"
    # click_element(driver, login_link)
    # print("Clicked on Log In link")
    #
    # email_input= "//input[@id='customer_email']"
    # send_keys_to_element(driver,email_input,user_data["email"])
    # print(f"Email entere: {user_data['email']}")
    #
    # passwrod_input= "//input[@id='customer_password']"
    # send_keys_to_element(driver,passwrod_input,user_data["password"])
    # print("Password entered")
    #
    # sign_in_button= "//input[@value='Sign In']"
    # click_element(driver,sign_in_button)
    # print("Clicked on Sign In button")
    #
    # time.sleep(500)

    search_input= "//input[@id='search-field']"
    send_keys_to_element(driver,search_input,user_data["search_term"])
    print(f"Product Searched:{user_data['search_term']}")
    time.sleep(3)

    search_button= "//input[@id='search-submit']"
    click_element(driver,search_button)
    print("Product is Searched")
    time.sleep(10)

    search_product= "//div[@class='four columns alpha']"
    click_element(driver,search_product)
    print("Product is clicked")

    add_to_cart_button= "//input[@id='add']"
    click_element(driver,add_to_cart_button)
    print("Added to cart")
    time.sleep(2)

    checkout_link= "//a[normalize-space()='Check Out']"
    click_element(driver,checkout_link)
    print("Checkout button is clicked")
    time.sleep(3)

    checkout_button= "//input[@id='checkout']"
    click_element(driver,checkout_button)
    print("Product is checked out")
    time.sleep(3)

    SignIn_link= "//a[normalize-space()='Sign in']"
    click_element(driver,SignIn_link)
    print("Signin link is clicked")
    time.sleep(3)

    Email_input= "//input[@id='customer_email']"
    send_keys_to_element(driver,Email_input,"nepal@gmail.com")
    print("Email is entered")

    Password_input="//input[@id='customer_password']"
    send_keys_to_element(driver,Password_input,"ABCDE@12345")
    print("Password is entered")

    SignIn_button= "//input[@value='Sign In']"
    click_element(driver,SignIn_button)
    print("Sign In button is clicked")



# wait for page to load
time.sleep(600)
# implicit wait

# close browser
driver.quit()