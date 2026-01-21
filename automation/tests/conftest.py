import pytest
import yaml
from automation.src.utils.driver_factory import get_driver
from automation.src.utils.logger import get_logger
from automation.src.utils.flask_server import start_flask_server, stop_flask_server

def load_config():
    with open("automation/config/config.yaml", "r") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def config():
    return load_config()

@pytest.fixture(scope="session")
def logger():
    return get_logger()

@pytest.fixture(scope="session", autouse=True)
def flask_server(logger):
    logger.info("Starting Flask server automatically...")
    process = start_flask_server()
    yield
    logger.info("Stopping Flask server automatically...")
    stop_flask_server(process)

@pytest.fixture(scope="session")
def driver(config, logger):
    logger.info("Launching browser (SESSION)...")

    driver = get_driver(
        browser=config["browser"],
        headless=config["headless"]
    )
    driver.implicitly_wait(3)

    yield driver

    logger.info("Closing browser (SESSION)...")
    driver.quit()
