import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json

# Automatically install ChromeDriver
chromedriver_autoinstaller.install()

# Setup WebDriver options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Setup WebDriver
driver = webdriver.Chrome()

# URL of the page with the dropdown
url = "https://example.com"  # Replace with the actual URL

# Open the URL
driver.get(url)

# Locate the dropdown menu
dropdown = driver.find_element(By.ID, "dropdown_id")  # Replace with actual ID

# Initialize the WebDriver
driver = webdriver.Chrome()

# Load the NHVR National Network Map page
driver.get("https://maps.nhvr.gov.au/?networkLayerContext=NATIONAL_MAP&view=Category")

# Function to extract options from a dropdown
def extract_dropdown_options(dropdown_id):
    dropdown = driver.find_element(By.ID, dropdown_id)
    options = dropdown.find_elements(By.TAG_NAME, 'option')
    return [option.text for option in options]

# Extract data from dropdown menus
data = {
    "VehicleCategories": extract_dropdown_options("vehicleCategoriesDropdownId"),
    "StateTerritories": extract_dropdown_options("stateTerritoriesDropdownId"),
    "RouteAccess": extract_dropdown_options("routeAccessDropdownId"),
    "MapLayers": extract_dropdown_options("mapLayersDropdownId"),
    "NoticesPermits": extract_dropdown_options("noticesPermitsDropdownId")
}

# Save the structured data to a JSON file
with open('dropdown_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

# Close the WebDriver
driver.quit()
