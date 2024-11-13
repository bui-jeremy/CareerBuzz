from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_to_indeed(driver):
    """Wait for manual login."""
    driver.get('https://secure.indeed.com/account/login')
    
    # Wait for the username field to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-username")))

    # Prompt for user to manually login and then press Enter to continue
    print("Please log in to Indeed manually in the browser.")
    input("Press Enter once you have logged in...")

def visit_job_links_from_search(search_url):
    """
    Given an Indeed search URL, this function navigates to the search page,
    extracts the job links, and visits each job link.
    """
    # Set up Selenium options (headless mode for background operation)
    options = Options()
    options.add_argument("--start-maximized")
    options.headless = False  # Run the browser in a visible mode for manual login
    driver = webdriver.Chrome(options=options)
    
    try:
        # Login manually (wait for user input after login)
        login_to_indeed(driver)

        # Navigate to the Indeed search URL
        print(f"Navigating to Indeed search URL: {search_url}")
        driver.get(search_url)
        time.sleep(3)  # Allow the search page to load

        # Wait for the job cards to be present on the page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='mosaic-provider-jobcards']"))
        )

        # Extract job links from the search page
        job_links = []
        job_cards = driver.find_elements(By.XPATH, "//a[@data-hide-spinner='true']")
        for job_card in job_cards:
            job_link = job_card.get_attribute('href')
            if job_link:
                job_links.append(job_link)
        
        # Visit each job link
        for job_url in job_links:
            print(f"Visiting job link: {job_url}")
            driver.get(job_url)
            time.sleep(3)  # Allow job page to load
            
            # Wait for the job details to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'jobsearch-JobComponent')]"))
            )

            # You can extract additional job details here if needed (e.g., description, salary, etc.)
            print(f"Job details loaded for: {job_url}")

    finally:
        driver.quit()

def test_visit_job_links_from_search():
    # Example Indeed search URL for Software Engineering Internships in Chicago
    search_url = "https://www.indeed.com/jobs?q=Software+Engineer+Internship&l=Chicago,+IL"
    
    # Test function to visit job links
    visit_job_links_from_search(search_url)

# Call the test function
test_visit_job_links_from_search()
