import pytest
from automation.src.pages.forgot_password_page import ForgotPasswordPage
from automation.src.utils.read_testdata import read_csv

test_data = read_csv("automation/data/forgot_password_testdata.csv")

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("data", test_data)
def test_forgot_password_flow(driver, config, logger, data):
    logger.info("Starting Forgot Password Test")

    page = ForgotPasswordPage(driver, timeout=config["explicit_wait"])
    page.open_url(config["base_url"] + "/forgot-password")

    page.reset_password(data["email"])

    if data["expected"] == "Password reset link sent successfully!":
        actual_msg = page.get_success_message()
    else:
        actual_msg = page.get_message()

    logger.info(f"Expected: {data['expected']} | Actual: {actual_msg}")
    assert actual_msg == data["expected"]
