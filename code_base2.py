Version 6:
from selenium import webdriver from selenium.webdriver.common.by import By from selenium.webdriver.support.ui import WebDriverWait from selenium.webdriver.support import expected_conditions as EC from selenium.webdriver.common.action_chains import ActionChains

class DaisiBot: # Previous methods...

def navigate_to_page(self, page_name):
    # Replace 'page_name' with the actual XPath or other locator strategy of the page link
    page_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{page_name}']")))
    page_link.click()
    print(f"Navigated to {page_name} page.")

def enter_data(self, student_data):
    for data_field, value in student_data.items():
        # Replace 'data_field' with the actual name or id or XPath of the HTML input fields
        input_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, data_field)))
        input_field.clear()
        input_field.send_keys(value)
        print(f"Entered {value} into {data_field} field.")
    submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    submit_button.click()
    print("Data submitted successfully.")

# Remaining methods...

def run(self, username, password, year):
    self.read_voucher()
    self.validate_data()
    self.setup_webdriver()
    self.login(username, password)
    self.select_year(year)
    self.navigate_to_page("Class Page")
    for student_data in self.voucher_data:
        self.navigate_to_page("Attendance Page")
        self.enter_data(student_data)
        self.navigate_to_page("Roster Page")
        self.enter_data(student_data)
    # Remaining sequence...
bot = DaisiBot("path/to/your/voucher.xlsx") bot.run("username", "password", "2023")


Version 7:
from selenium import webdriver from selenium.webdriver.chrome.service import Service from selenium.webdriver.common.by import By from selenium.webdriver.chrome.options import Options from selenium.webdriver.support.ui import WebDriverWait from selenium.webdriver.support import expected_conditions as EC from webdriver_manager.chrome import ChromeDriverManager

Setup chrome options for Selenium
chrome_options = Options() chrome_options.add_argument("--headless") # Ensure GUI is off chrome_options.add_argument("--no-sandbox") chrome_options.add_argument("--disable-dev-shm-usage")

Set path to chromedriver as per your configuration
webdriver_service = Service(ChromeDriverManager().install())

def login_to_daisi(username, password): driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Navigate to the Daisi login page
driver.get("https://your-daisi-website-url.com")

# Fill in username
username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'userName')))
username_field.send_keys(username)

# Fill in password
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'password')))
password_field.send_keys(password)

# Click login button
login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'login')))
login_button.click()

# Click on Daisi-Acess-V2
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "V2 DAISI")]'))).click()

return driver
Execute login
driver = login_to_daisi('your_username', 'your_password')


Version 8:
from selenium.webdriver.common.action_chains import ActionChains

Add the following functions to your existing script
def select_year(driver, year): # Click dropdown dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-dropdown-trigger-icon'))) dropdown.click()

# Select year from dropdown
year_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//li[@aria-label="{year}"]')))
year_option.click()
def enter_student_search(driver, student_name): # Enter student name in search search_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Enter Class/Section No to Search"]'))) search_field.send_keys(student_name)

def navigate_to_students(driver): # Click on the "Students" header dropdown students_header = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Students"]'))) students_header.click()

def navigate_to_classes(driver): # Click on the "Classes" header dropdown classes_header = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Classes"]'))) classes_header.click()

Execute functions
select_year(driver, 2023) enter_student_search(driver, 'student_name') # replace with actual student name navigate_to_students(driver) navigate_to_classes(driver)

This code builds upon the previous script by adding several new functions to interact with the site after logging in.

The select_year function clicks on the year dropdown and then selects the specified year from the dropdown.

The enter_student_search function finds the student search field (by placeholder text) and enters the specified student name into it.

The navigate_to_students and navigate_to_classes functions click on the "Students" and "Classes" header dropdowns, respectively.


Version 9:
Selecting "Add New" under the "Students" dropdown. Clicking on "List/Search" under the "Classes" dropdown. Selecting "List Current FY" from the Classes menu. Here is how you can add these actions to your Selenium script: def add_new_student(driver): # Click on the "Add New" option under "Students" add_new_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[text()="Add New"]'))) add_new_option.click()

def list_search_classes(driver): # Click on the "List/Search" option under "Classes" list_search_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[text()="List/Search"]'))) list_search_option.click()

def list_current_fy(driver): # Click on the "List Current FY" option under "Classes" list_current_fy_option = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[text()="List Current FY"]'))) list_current_fy_option.click()

Execute functions
add_new_student(driver) list_search_classes(driver) list_current_fy(driver)

Version 10:
 from selenium.webdriver.support.ui import WebDriverWait from selenium.webdriver.support import expected_conditions as EC from selenium.webdriver.common.by import By

def navigate_to_class_page(driver, class_name): # Enter class name into search field class_search_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[pinputtext][size="12"]'))) class_search_field.send_keys(class_name)

# Wait for the table to load and select the first row
table_first_row = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tbody.ui-table-tbody > tr')))
table_first_row.click()

# Wait for the class page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul[role="tablist"]')))
def navigate_to_roster_tab(driver): # Click on the 'Roster' tab roster_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-tabpanel-5-label'))) roster_tab.click()

def search_student_in_roster(driver, last_name, first_name): # Enter student's last name into search field last_name_search_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[pinputtext][size="12"].ng-star-inserted'))) last_name_search_field.send_keys(last_name)

# Enter student's first name into search field
first_name_search_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[pinputtext][size="12"].ng-star-inserted')))
first_name_search_field.send_keys(first_name)

# Apply the global filter
global_filter_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"][size="50"][placeholder="Global Filter"]')))
global_filter_field.send_keys('\n')  # Press enter to apply filter
Here's a usage example: driver = webdriver.Firefox() # or webdriver.Chrome()

Navigate to your application's URL
driver.get('https://your-application-url')

navigate_to_class_page(driver, 'Your ClassName') navigate_to_roster_tab(driver) search_student_in_roster(driver, 'StudentLastName', 'StudentFirstName')

You can also merge these functions into one or split them even further depending on how you intend to use them.

The CSS selectors I used are based on the HTML snippets you provided. If these steps don't work as expected, please check if the selectors are correct.

Please replace 'Your ClassName', 'StudentLastName', and 'StudentFirstName' with actual values.

The line driver.get('https://your-application-url') should be replaced with the actual URL of your application.
