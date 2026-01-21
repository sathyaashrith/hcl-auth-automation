import pytest
from automation.src.pages.login_page import LoginPage
from automation.src.utils.read_testdata import read_csv

test_data = read_csv("automation/data/login_testdata.csv")

@pytest.mark.regression
@pytest.mark.parametrize("data", test_data)
def test_login_flow(driver, config, logger, data):
    logger.info("Starting Login Test")

    login_page = LoginPage(driver, timeout=config["explicit_wait"])
    login_page.open_url(config["base_url"] + "/login")

    login_page.login(data["email"], data["password"])
    actual_msg = login_page.get_message()

    logger.info(f"Expected: {data['expected']} | Actual: {actual_msg}")
    assert actual_msg == data["expected"]
