import random
import os
import sys
import subprocess
import time
import datetime
import requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException

webhook_url = "https://discord.com/api/webhooks/1272446000434249748/1LqSPp1x8OBckK96COA8dEZgtNMDK-QYXtUTMzNBD8mp877fGbaYu4GJFyaJ7dHOCD-g"

# driving.py

def close_chrome():
    """Close all running instances of Google Chrome."""
    try:
        if os.name == 'posix':  # For macOS and Linux
            subprocess.call(['pkill', 'Google Chrome'])
            subprocess.call(['pkill', 'chrome'])
        elif os.name == 'nt':  # For Windows
            subprocess.call(['taskkill', '/F', '/IM', 'chrome.exe'])
    except Exception as e:
        print(f"Error while trying to close Chrome: {e}")

# Close Chrome before starting the script
#close_chrome()

# Set up Chrome options
options = uc.ChromeOptions()
profile_path = os.getenv('CHROME_PROFILE_PATH', "/Users/salimmohamud/Library/Application Support/Google/Chrome")
options.add_argument(f"user-data-dir={profile_path}")

# Disable automation flags
#options.add_argument('--incognito')

options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize undetected Chrome WebDriver with the specified options
driver = uc.Chrome(options=options)
driver.implicitly_wait(10)  # Increase implicit wait time

# Parameterize the URL
url = os.getenv('TICKETING_URL', "https://www.gov.uk/change-driving-test")
driver.get(url)

time.sleep(2.5)

def click_start_button():
    """Waits for the start button to be present, refreshing the page if needed."""
    max_attempts = 360  # Number of times to attempt before giving up
    attempt = 0
    while attempt < max_attempts:
        try:
            print("Waiting for start button to be present...")
            start_button_element = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/div/div[2]/div/div/section[1]/p/a"))
            )
            start_button_element.click()
            print("Clicked start button")
            return
        except TimeoutException:
            print("Timed out waiting for start button to be present. Refreshing the page...")
            driver.refresh()  # Refresh the page if the button is not found
            time.sleep(1)  # Wait for 1 second before retrying
        except NoSuchElementException:
            print("Start button not found. Refreshing the page...")
            driver.refresh()  # Refresh the page if the button is not found
            time.sleep(1)  # Wait for 1 second before retrying
        attempt += 1
    print("Failed to find the start button after several attempts.")

# Call the function to click the start button
click_start_button()

time.sleep(2.5)

def enter_licence_number():
    """Waits for the driving licence input field to be present, refreshing the page every second if needed."""
    max_attempts = 360  # Number of times to attempt before giving up
    attempt = 0
    while attempt < max_attempts:
        try:
            print("Waiting for driving licence input field to be present...")
            licence_input_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#driving-licence-number"))
            )
            licence_input_element.clear()  # Clear the input field if necessary (optional)
            licence_input_element.send_keys("MOHAM053105ZI9TP")
            print("Entered licence number")
            return
        except TimeoutException:
            print("Timed out waiting for driving licence input field to be present. Refreshing the page...")
            driver.refresh()  # Refresh the page if the element is not found
            time.sleep(1)  # Wait for 1 second before retrying
        except NoSuchElementException:
            print("Driving licence input field not found. Refreshing the page...")
            driver.refresh()  # Refresh the page if the element is not found
            time.sleep(1)  # Wait for 1 second before retrying
        attempt += 1
    print("Failed to find the driving licence input field after several attempts.")

enter_licence_number()

time.sleep(2.5)

def enter_test_number():
    """Waits for the driving licence input field to be present, refreshing the page every second if needed."""
    max_attempts = 360  # Number of times to attempt before giving up
    attempt = 0
    while attempt < max_attempts:
        try:
            print("Waiting for driving licence input field to be present...")
            licence_input_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#application-reference-number"))
            )
            licence_input_element.clear()  # Clear the input field if necessary (optional)
            licence_input_element.send_keys("63125260")
            print("Entered licence number")
            return
        except TimeoutException:
            print("Timed out waiting for driving licence input field to be present. Refreshing the page...")
            driver.refresh()  # Refresh the page if the element is not found
            time.sleep(1)  # Wait for 1 second before retrying
        except NoSuchElementException:
            print("Driving licence input field not found. Refreshing the page...")
            driver.refresh()  # Refresh the page if the element is not found
            time.sleep(1)  # Wait for 1 second before retrying
        attempt += 1
    print("Failed to find the driving licence input field after several attempts.")

enter_test_number()

time.sleep(2.5)

def click_continue_button():
    """Waits for the continue button to be clickable, refreshing the page every second if needed."""
    max_attempts = 360  # Number of times to attempt before giving up
    attempt = 0
    while attempt < max_attempts:
        try:
            print("Waiting for continue button to be clickable...")
            continue_button_element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#booking-login"))
            )
            continue_button_element.click()
            print("Clicked continue button")
            return
        except TimeoutException:
            print("Timed out waiting for continue button to be clickable. Refreshing the page...")
            driver.refresh()  # Refresh the page if the element is not found
            time.sleep(1)  # Wait for 1 second before retrying
        except NoSuchElementException:
            print("Continue button not found. Refreshing the page...")
            driver.refresh()  # Refresh the page if the element is not found
            time.sleep(1)  # Wait for 1 second before retrying
        attempt += 1
    print("Failed to find the continue button after several attempts.")

click_continue_button()

time.sleep(1.5)

def click_change_button():
    """Waits for the continue button to be clickable, refreshing the page every second if needed."""
    max_attempts = 360  # Number of times to attempt before giving up
    attempt = 0
    while attempt < max_attempts:
        try:
            print("Waiting for continue button to be clickable...")
            continue_button_element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#date-time-change"))
            )
            continue_button_element.click()
            print("Clicked continue button")
            return
        except TimeoutException:
            print("Timed out waiting for continue button to be clickable. Refreshing the page...")
            driver.refresh()  # Refresh the page if the element is not found
            time.sleep(1)  # Wait for 1 second before retrying
        except NoSuchElementException:
            print("Continue button not found. Refreshing the page...")
            driver.refresh()  # Refresh the page if the element is not found
            time.sleep(1)  # Wait for 1 second before retrying
        attempt += 1
    print("Failed to find the continue button after several attempts.")

click_change_button()

time.sleep(1.5)

def click_asap_button():
    """Waits for the ASAP radio button to be clickable, refreshing the page every second if needed."""
    max_attempts = 360  # Number of times to attempt before giving up
    attempt = 0
    while attempt < max_attempts:
        try:
            print("Waiting for ASAP radio button to be clickable...")
            asap_button_element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#test-choice-earliest"))
            )
            asap_button_element.click()
            print("Clicked ASAP radio button")
            return
        except TimeoutException:
            print("Timed out waiting for ASAP radio button to be clickable. Refreshing the page...")
            driver.refresh()  # Refresh the page if the element is not found
            time.sleep(1)  # Wait for 1 second before retrying
        except NoSuchElementException:
            print("ASAP radio button not found. Refreshing the page...")
            driver.refresh()  # Refresh the page if the element is not found
            time.sleep(1)  # Wait for 1 second before retrying
        attempt += 1
    print("Failed to find the ASAP radio button after several attempts.")

# Call the function to click the ASAP radio button
click_asap_button()

time.sleep(1.5)

def click_continue_test_button():
    """Waits for the continue button to be clickable, refreshing the page every second if needed."""
    max_attempts = 360  # Number of times to attempt before giving up
    attempt = 0
    while attempt < max_attempts:
        try:
            print("Waiting for continue button to be clickable...")
            continue_button_element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#driving-licence-submit"))
            )
            continue_button_element.click()
            print("Clicked continue button")
            return
        except TimeoutException:
            print("Timed out waiting for continue button to be clickable. Refreshing the page...")
            driver.refresh()  # Refresh the page if the element is not found
            time.sleep(1)  # Wait for 1 second before retrying
        except NoSuchElementException:
            print("Continue button not found. Refreshing the page...")
            driver.refresh()  # Refresh the page if the element is not found
            time.sleep(1)  # Wait for 1 second before retrying
        attempt += 1
    print("Failed to find the continue button after several attempts.")

click_continue_test_button()

time.sleep(1.5)

def book_first_available_date(driver):
    """
    Searches for the first available booking date and clicks on it.

    Args:
        driver: The Selenium WebDriver instance.

    Returns:
        bool: True if an available date was found and clicked, False otherwise.
    """
    try:
        # Wait for the booking calendar to load and display available dates
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "BookingCalendar-date--bookable"))
        )

        # Re-find the elements in case the page has updated or the reference is stale
        available_dates = driver.find_elements(By.CLASS_NAME, "BookingCalendar-date--bookable")
        
        if available_dates:
            first_available = available_dates[0]
            
            # Attempt a JavaScript click first
            try:
                driver.execute_script("arguments[0].click();", first_available)
                print("Clicked on the first available date using JavaScript.")
            except Exception as e:
                print(f"JavaScript click failed: {e}. Attempting normal click.")
                # Fallback to normal click if JavaScript click fails
                first_available.click()
                print("Clicked on the first available date.")

            return True
        else:
            print("No available dates found.")
            return False
    
    except TimeoutException:
        print("Timed out waiting for available dates to load.")
        return False
    except StaleElementReferenceException:
        print("Stale element reference encountered. Retrying...")
        return book_first_available_date(driver)
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Call the function in different contexts

# 1. Initial booking attempt
print("First attempt to book an available date...")
first_attempt_success = book_first_available_date(driver)
print("First booking attempt successful:", first_attempt_success)


def handle_warning_loop(driver):
    """
    Handles warnings by retrying booking from the start until the warning is no longer present.
    
    Args:
        driver: The Selenium WebDriver instance.
    """
    while True:
        try:
            # Check if the warning element is present
            warning_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#main > section.warning-summary.formatting > p"))
            )
            print("Warning message detected. Waiting before retrying...")

            # Wait a random time between 100 and 200 seconds with a live countdown
            wait_time = random.randint(100, 200)
            print(f"Waiting for {wait_time} seconds before retrying...")
            
            # Live countdown
            for i in range(wait_time, 0, -1):
                print(f"Retrying in {i} seconds...", end="\r")
                time.sleep(1)

            print("\nCountdown finished. Retrying process...")
            
            # Click the 'Change Test Centre' button
            change_centre_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "change-test-centre"))
            )
            driver.execute_script("arguments[0].click();", change_centre_button)
            print("Clicked 'Change Test Centre' button.")


            # Click the 'Find test centres' submit button
            test_centres_submit_button = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.ID, "test-centres-submit"))
            )
            driver.execute_script("arguments[0].click();", test_centres_submit_button)
            print("Clicked 'Find test centres' submit button.")


            # Click the first available test centre option
            first_centre_option = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#centre-name-56 > div"))
            )
            driver.execute_script("arguments[0].click();", first_centre_option)
            print("Clicked first available test centre option.")

            # Check again if the warning element is still present
            if WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#main > section.warning-summary.formatting > p"))
            ):
                print("Warning message still present, restarting process...")
                continue
            else:
                print("Warning message no longer present, process completed.")
                break
        
        except TimeoutException:
            print("Warning element not found, process may have succeeded.")
            break
        except NoSuchElementException:
            print("Element not found during the process.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
        

def click_change_test_centre_button(driver):
    """Clicks the 'Change Test Centre' button using JavaScript, then clears the input field and enters 'Chilwell'."""
    try:
        print("Clicking 'Change Test Centre' button...")
        change_centre_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "change-test-centre"))
        )
        
        # Use JavaScript to click the button
        driver.execute_script("arguments[0].click();", change_centre_button)
        print("Clicked 'Change Test Centre' button using JavaScript.")
        #time.sleep(2)
        # Proceed with further actions
        # Clear the input field and enter 'Chilwell'
        test_centre_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "test-centres-input"))
        )
        test_centre_input.clear()  # Clear the input field
        print("Cleared the test centre input field.")
    
        test_centre_input.send_keys("Chesterfield")  # Enter 'Chilwell'
        print("Entered 'Chilwell' in the test centre input field.")
        handle_test_centre_selection(driver)
        
    except TimeoutException:
        print("'Change Test Centre' button or input field not found in time.")
    except NoSuchElementException:
        print("'Change Test Centre' button or input field not found on the page.")
    except Exception as e:
        print(f"An error occurred while interacting with the test centre input: {e}")

def handle_test_centre_selection(driver):
    """Handles the selection of a test centre and checks for warnings."""
    try:
        # Click the 'Find test centres' submit button
        print("Clicking 'Find test centres' submit button...")
        test_centres_submit_button = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#test-centres-submit"))
        )
        driver.execute_script("arguments[0].click();", test_centres_submit_button)
        print("Clicked 'Find test centres' submit button.")

        # Click the first available test centre option
        print("Clicking first available test centre option...")
        first_centre_option = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#centre-name-56 > div"))
        )
        driver.execute_script("arguments[0].click();", first_centre_option)
        print("Clicked first available test centre option.")
        
        # Handle warning messages and retry booking if necessary
        handle_warning_loop(driver)

    except TimeoutException:
        print("Timed out waiting for elements during test centre selection.")
    except NoSuchElementException:
        print("One of the test centre elements was not found on the page.")
    except Exception as e:
        print(f"An error occurred during test centre selection: {e}")

def check_slot_picker_details(driver):
    """Extracts and returns the concatenated day title and time from the SlotPicker elements."""
    try:
        # Wait for the SlotPicker-dayTitle element to be present and get its text
        day_title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/section/section[3]/form/div[1]/div[2]/fieldset/ul/li[2]/p"))
        )
        day_title_text = day_title_element.text
        print(f"Day title extracted: '{day_title_text}'")  # Debugging output
        
        # Wait for the SlotPicker-time element to be present and get its text
        time_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/section/section[3]/form/div[1]/div[2]/fieldset/ul/li[2]/label/strong"))
        )
        time_text = time_element.text
        print(f"Time extracted: '{time_text}'")  # Debugging output
        
        # Check if the extracted date and time match your existing booking
        if day_title_text == 'Tuesday 21 January 2025' and time_text == '2:22pm':
            print("Current slot matches your existing booking.")
            click_change_test_centre_button(driver)
        else:
            print("Current slot does not match your existing booking. Proceeding with usual process.")
            # You can call your usual booking functions here if needed

    except TimeoutException:
        print("Timed out waiting for elements to be present.")
    except NoSuchElementException:
        print("One of the SlotPicker elements was not found on the page.")
        return None

# Call the function with the WebDriver instance
check_slot_picker_details(driver)


time.sleep(1.5)

# 2. Second booking attempt
print("Second attempt to book an available date...")
second_attempt_success = book_first_available_date(driver)
print("Second booking attempt successful:", second_attempt_success)


def click_first_available_slot(driver):
    """
    Finds the first available radio input with class 'SlotPicker-slot' and clicks it using JavaScript first.

    Args:
        driver: The Selenium WebDriver instance.

    Returns:
        bool: True if the slot was successfully clicked, False otherwise.
    """
    try:
        # Wait for at least one slot input to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.SlotPicker-slot[type='radio'][name='slotTime']"))
        )

        # Find all radio inputs with the class 'SlotPicker-slot' and name 'slotTime'
        slot_inputs = driver.find_elements(By.CSS_SELECTOR, "input.SlotPicker-slot[type='radio'][name='slotTime']")

        if slot_inputs:
            # Scroll the first slot input into view
            first_slot_input = slot_inputs[0]
            driver.execute_script("arguments[0].scrollIntoView(true);", first_slot_input)
            time.sleep(1)  # Wait for the scroll to finish

            # Use JavaScript to click the input element
            try:
                driver.execute_script("arguments[0].click();", first_slot_input)
                print("Clicked on the first available slot using JavaScript.")
                return True
            except Exception as e:
                print(f"JavaScript click failed: {e}")
                # If JavaScript click fails, try direct click
                try:
                    first_slot_input.click()
                    print("Clicked on the first available slot directly.")
                    return True
                except Exception as e:
                    print(f"Direct click also failed: {e}")
                    return False

        else:
            print("No available slots found.")
            return False

    except TimeoutException:
        print("Timed out waiting for the slot inputs to be present.")
        return False
    except NoSuchElementException:
        print("No input element found with the specified criteria.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage:
slot_click_success = click_first_available_slot(driver)
print("Slot selection successful:", slot_click_success)

time.sleep(1.5)

def print_slot_picker_details(driver):
    """Extracts and returns the concatenated day title and time from the SlotPicker elements."""
    try:
        # Wait for the SlotPicker-dayTitle element to be present and get its text
        day_title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/section/section[3]/form/div[1]/div[2]/fieldset/ul/li[2]/p"))
        )
        day_title_text = day_title_element.text
        print(f"Day title extracted: '{day_title_text}'")  # Debugging output
        
        # Wait for the SlotPicker-time element to be present and get its text
        time_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/main/section/section[3]/form/div[1]/div[2]/fieldset/ul/li[2]/label/strong"))
        )
        time_text = time_element.text
        print(f"Time extracted: '{time_text}'")  # Debugging output
        
        # Concatenate the day title and time
        test_date_time = f"{day_title_text}, {time_text}"
        print(f"Concatenated date and time: '{test_date_time}'")  # Debugging output
        
        return test_date_time

    except TimeoutException:
        print("Timed out waiting for elements to be present.")
    except NoSuchElementException:
        print("One of the SlotPicker elements was not found on the page.")
        return None

# Call the function with the WebDriver instance
test_date_time = print_slot_picker_details(driver)

time.sleep(1.5)


def click_slot_chosen_submit_button(driver):
    """Waits for the 'slot-chosen-submit' button to be clickable, refreshing the page if needed."""
    max_attempts = 360  # Number of times to attempt before giving up
    attempt = 0
    while attempt < max_attempts:
        try:
            print("Waiting for 'slot-chosen-submit' button to be clickable...")
            submit_button_element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#slot-chosen-submit"))
            )
            # Attempt JavaScript click first
            try:
                driver.execute_script("arguments[0].click();", submit_button_element)
                print("Clicked 'slot-chosen-submit' button using JavaScript.")
            except Exception as js_e:
                print(f"JavaScript click failed: {js_e}")
                # If JavaScript click fails, try direct click
                try:
                    submit_button_element.click()
                    print("Clicked 'slot-chosen-submit' button directly.")
                except Exception as e:
                    print(f"Direct click also failed: {e}")
            return
        except TimeoutException:
            print("Timed out waiting for 'slot-chosen-submit' button to be clickable. Refreshing the page...")
            driver.refresh()  # Refresh the page if the element is not found
            time.sleep(1)  # Wait for 1 second before retrying
        except NoSuchElementException:
            print("'slot-chosen-submit' button not found. Refreshing the page...")
            driver.refresh()  # Refresh the page if the element is not found
            time.sleep(1)  # Wait for 1 second before retrying
        attempt += 1
    print("Failed to find the 'slot-chosen-submit' button after several attempts.")

click_slot_chosen_submit_button(driver)

time.sleep(1.5)

##
def print_test_details(driver):
    """
    Extracts the test details from the #selected-slot-time element and prints them.
    
    Args:
        driver: The Selenium WebDriver instance.
        
    Returns:
        str: The text content of the #selected-slot-time element, or None if not found.
    """
    try:
        # Wait for the element to be present
        selected_slot_time_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#selected-slot-time"))
        )
        
        # Extract the text content of the element
        slot_time_text = selected_slot_time_element.text
        
        # Print the extracted details
        print(f"Selected Test Slot Time: {slot_time_text}")
        
        # Return the extracted details
        return slot_time_text
    
    except TimeoutException:
        print("Timeout: The element #selected-slot-time was not found.")
    except NoSuchElementException:
        print("NoSuchElementException: The element #selected-slot-time was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return None

test_details = print_test_details(driver)

time.sleep(1)


def click_slot_warning_continue_button(driver):
    """Waits for the 'slot-warning-continue' button to be clickable, refreshing the page if needed."""
    max_attempts = 360  # Number of times to attempt before giving up
    attempt = 0
    while attempt < max_attempts:
        try:
            print("Waiting for 'slot-warning-continue' button to be clickable...")
            continue_button_element = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#slot-warning-continue"))
            )
            # Attempt JavaScript click first
            try:
                driver.execute_script("arguments[0].click();", continue_button_element)
                print("Clicked 'slot-warning-continue' button using JavaScript.")
            except Exception as js_e:
                print(f"JavaScript click failed: {js_e}")
                # If JavaScript click fails, try direct click
                try:
                    continue_button_element.click()
                    print("Clicked 'slot-warning-continue' button directly.")
                except Exception as e:
                    print(f"Direct click also failed: {e}")
            return
        except TimeoutException:
            print("Timed out waiting for 'slot-warning-continue' button to be clickable. Refreshing the page...")
            driver.refresh()  # Refresh the page if the element is not found
            time.sleep(1)  # Wait for 1 second before retrying
        except NoSuchElementException:
            print("'slot-warning-continue' button not found. Refreshing the page...")
            driver.refresh()  # Refresh the page if the element is not found
            time.sleep(1)  # Wait for 1 second before retrying
        attempt += 1
    print("Failed to find the 'slot-warning-continue' button after several attempts.")

click_slot_warning_continue_button(driver)

time.sleep(1)

def send_to_discord(slot_time_text, webhook_url):
    """Sends the test date and time to a Discord channel via webhook."""
    data = {
        "content": f"Test date and time found and are in basket: {slot_time_text}"
    }
    
    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()  # Will raise an exception for HTTP error codes
        print("Message sent to Discord successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message to Discord: {e}")
        if response:
            print("Response status code:", response.status_code)
            print("Response text:", response.text)


if test_details:
    send_to_discord(test_details, webhook_url)
else:
    print("No test date and time found to send.")

time.sleep(1.5)

# click this button if its there #i-am-candidate

#then click this button if its there #confirm-changes


time.sleep(5000)  # Optional: Wait for subsequent actions
