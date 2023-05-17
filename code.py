import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_careers_page():
    # Set up WebDriver
    driver = webdriver.Chrome()  # Update with the appropriate WebDriver for your browser

    # Step 1: Visit Insider homepage
    driver.get("https://useinsider.com/")
    assert "Insider" in driver.title, "Insider homepage not opened"

    # Step 2: Open Careers page and check blocks
    more_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "More")))
    more_menu.click()
    careers_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Careers")))
    careers_link.click()
    assert "Careers" in driver.title, "Careers page not opened"
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "locations"))), "Locations block not opened"
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "teams"))), "Teams block not opened"
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "lifeatinsider"))), "Life at Insider block not opened"

    # Step 3: Filter and check QA jobs
    see_all_teams = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "See All Teams")))
    see_all_teams.click()
    quality_assurance = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Quality Assurance")))
    quality_assurance.click()
    see_all_qa_jobs = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "See all QA jobs")))
    see_all_qa_jobs.click()
    assert "Istanbul, Turkey" in driver.page_source, "Jobs list not filtered by location"
    assert "Quality Assurance" in driver.page_source, "Jobs list not filtered by department"

    # Step 4: Check job details
    job_positions = driver.find_elements(By.CSS_SELECTOR, ".job-position")
    for position in job_positions:
        assert "Quality Assurance" in position.text, "Position does not contain 'Quality Assurance'"
    job_departments = driver.find_elements(By.CSS_SELECTOR, ".job-department")
    for department in job_departments:
        assert "Quality Assurance" in department.text, "Department does not contain 'Quality Assurance'"
    job_locations = driver.find_elements(By.CSS_SELECTOR, ".job-location")
    for location in job_locations:
        assert "Istanbul, Turkey" in location.text, "Location does not contain 'Istanbul, Turkey'"
    apply_buttons = driver.find_elements(By.CSS_SELECTOR, ".job-apply-button")
    for apply_button in apply_buttons:
        assert apply_button.is_enabled(), "Apply Now button is not enabled"

    # Step 5: Click Apply Now and check Lever Application form
    apply_buttons[0].click()
    time.sleep(3)  # Wait for the page to load
    assert "Lever" in driver.title, "Lever Application form page not opened"

    # Quit the WebDriver
    driver.quit()


# Run the test
test_careers_page()