from selenium import webdriver
import time
import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # start Chrome in desktop mode
chrome_options.add_argument("--incognito")  # start Chrome in incognito mode

# Setup webdriver
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=chrome_options)

# Define the URL of the main page (change to the actual search page)
url = "https://www.kayak.com/flights/DTW-LAX/2023-08-09/1adults?sort=bestflight_a&fs=airlines=MULT,DL"

# Open the URL
driver.get(url)

# Set up the wait
wait = WebDriverWait(driver, 10)
time.sleep(12)

# Open/create a file to append data
csvFile = open('data/flight_data.csv', 'a', newline='')

#Use csv Writer
csvWriter = csv.writer(csvFile)

# Try to click the "Show more results" button until it's no longer available
while True:
    try:
        show_more_button = driver.find_element(By.CSS_SELECTOR, '.ULvh-button.show-more-button')
        show_more_button.click()
        # Wait for the new results to load
        time.sleep(5) # adding sleep time to make sure DOM is fully loaded after clicking
    except NoSuchElementException:
        # If the "Show more results" button is not found, break the loop
        break

# write headers
csvWriter.writerow(["Departure - Arrival Time", "Airline Name", "Number of stops", "Flight Duration", "Main Cabin Price", "Comfort Plus Price"])

# After all results are loaded, find all flight elements
flights = driver.find_elements(By.CSS_SELECTOR, '.nrc6')

# Now you can interact with the results
for flight in flights:
    flight_details = flight.text.split('\n')

    print(flight_details)

    # Initialize variables to hold the flight details
    departure_arrival_time, airline_name, number_of_stops, flight_duration = "", "", "", ""
    main_cabin_price, comfort_plus_price = "", ""  # Initialize these variables as empty strings

    # Loop over the flight details to parse the information
    for index, detail in enumerate(flight_details):
        if "–" in detail and ":" in detail:  # The departure-arrival time detail contains a dash and colon
            departure_arrival_time = detail
        elif any(airline.lower() in detail.lower() for airline in ["Delta", "American", "United"]):  # Replace with the actual airline names
            airline_name = detail
        elif "stop" in detail:  # Just check if "stop" is in the detail
            number_of_stops = detail
        elif "h" in detail and "m" in detail and "–" not in detail:  # The flight duration detail contains "h" and "m", but not dash
            flight_duration = detail
        elif "$" in detail:  # If the detail contains a "$", it's the price info
            try:
                if flight_details[index + 1] == "Main Cabin":  # Check if the next detail is "Main Cabin"
                    main_cabin_price = detail
                elif flight_details[index + 1] == "Comfort +":  # Check if the next detail is "Comfort Plus"
                    comfort_plus_price = detail
            except IndexError:
                continue  # If the "$" detail is the last item in the list, just continue

    # Write the details to the CSV file
    csvWriter.writerow([departure_arrival_time, airline_name, number_of_stops, flight_duration, main_cabin_price, comfort_plus_price])

print('Done Writing to CSV')

# Close the browser
driver.quit()

# Close the CSV file
csvFile.close()
