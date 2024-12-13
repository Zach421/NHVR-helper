from selenium import webdriver
from selenium.webdriver.common.by import By
import json

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
