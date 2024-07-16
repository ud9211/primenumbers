from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


service = Service('./chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://hprera.nic.in/PublicDashboard')

driver.implicitly_wait(20)

n = 6  # Replace this with the desired range

data = []
def extract_table_data():
    try:
        table = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//table[@class="table table-borderless table-sm table-responsive-lg table-striped font-sm"]'))
        )
        rows = table.find_elements(By.XPATH, './/tr')
        row_data = {}
        for row in rows:
            columns = row.find_elements(By.XPATH, './/td')
            if len(columns) == 2:
                key = columns[0].text.strip()
                value = columns[1].text.strip()
                row_data[key] = value
        data.append(row_data)
    except Exception as e:
        print(f"An error occurred: {e}")

try:
    anchor_elements = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, '//a[@title="View Application"]'))
    )

    for i in range(min(n+1, len(anchor_elements))):
        anchor_elements[i].click()
        extract_table_data()
        
        close_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="close" and @data-dismiss="modal"]'))
        )
        close_button.click()
        
        driver.implicitly_wait(20)

        anchor_elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[@title="View Application"]'))
        )
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()

# i have created a dataframe for better arrangement of the data and cleaning the data too
df = pd.DataFrame(data)
df['GSTIN No.'] = df['GSTIN No.'].str.split().str[0]
df['PAN No.'] = df['PAN No.'].str.split().str[0]

extracted_data = df[['Name', 'GSTIN No.', 'PAN No.', 'Permanent Address']]
print(extracted_data)