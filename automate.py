import os
import time
from play import click, run
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.EdgeOptions()
options.add_experimental_option('detach', True)


os.environ['PATH'] += r'../driver'
driver = webdriver.Edge(options=options)

driver.get('https://www.gamesgames.com/game/magic-piano-tiles')
driver.maximize_window()

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
)
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

# Wait for the iframe to be present
iframe = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src*='html5.gamedistribution.com']"))
)
# Switch to the iframe
driver.switch_to.frame(iframe)

# Now wait for the play button to be clickable
play_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "pluto-splash-button")))
play_button.click()


# Bypass ads
time.sleep(15)
click(1198, 814)
# Click the start button
time.sleep(10)
click(677, 516)

# Let the beethoven play
run()

