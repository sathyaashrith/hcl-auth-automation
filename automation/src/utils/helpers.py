import os
from datetime import datetime

def take_screenshot(driver, test_name):
    os.makedirs("automation/screenshots/failed_tests", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"automation/screenshots/failed_tests/{test_name}_{timestamp}.png"
    driver.save_screenshot(file_path)
    return file_path
