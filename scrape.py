from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def scrape_jobs(job_title, city=None, date_posted=""):
    # Set up Selenium options
    options = Options()
    options.add_argument("--start-maximized")
    options.headless = False  # Set to True for headless mode
    driver = webdriver.Chrome(options=options)
    
    try:
        jobs = []
        page = 1 

        # Construct the initial URL with dynamic parameters
        search_url = f"https://www.indeed.com/jobs?q={job_title.replace(' ', '+')}"
        if city:
            search_url += f"&l={city.replace(' ', '+')}"
        if date_posted:
            search_url += f"&fromage={date_posted}"
        
        driver.get(search_url)
        time.sleep(2)  # Allow page content to load

        while True:
            print(f"Scraping page {page}...")

            # Wait for job listings to load
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@id='mosaic-provider-jobcards']"))
                )
            except Exception as e:
                print(f"Timeout or error occurred while loading job listings: {e}")
                break  # Move on to the next job title

            # Parse page content with BeautifulSoup
            soup = BeautifulSoup(driver.page_source, "html.parser")
            job_cards = soup.find_all("td", class_="resultContent css-lf1alc eu4oa1w0")

            if not job_cards:
                print("No job cards found, ending search.")
                break

            # Extract job details for each job card
            for job_card in job_cards:
                try:
                    title_element = job_card.find("a", class_="jcs-JobTitle") or job_card.find("h2", class_="jobTitle")
                    title = title_element.text.strip() if title_element else "No Title"
                    
                    company_element = job_card.find("span", attrs={"data-testid": "company-name"}) or job_card.find("span", class_="companyName")
                    company = company_element.text.strip() if company_element else "No Company"
                    
                    location_element = job_card.find("div", attrs={"data-testid": "text-location"}) or job_card.find("div", class_="companyLocation")
                    location = location_element.text.strip() if location_element else "No Location"
                    
                    pay_element = (
                        job_card.find("h2", class_="css-1rqpxry") or
                        job_card.find("span", class_="salary-snippet") or
                        job_card.find("div", string=lambda text: "$" in text if text else False)
                    )
                    pay = pay_element.text.strip() if pay_element else "No Pay Information"
                    
                    link_element = job_card.find("a", class_="jcs-JobTitle")
                    job_link = f"https://www.indeed.com{link_element.get('href', '')}" if link_element else "No Link"

                    jobs.append({
                        "title": title,
                        "company": company,
                        "location": location,
                        "pay": pay,
                        "link": job_link
                    })
                except Exception as e:
                    print(f"Error extracting job details: {e}")
                    continue  # Continue with the next job if this one fails

            # Look for the "Next" page button in the pagination element
            pagination = soup.find("nav", {"aria-label": "pagination"})
            next_button = pagination.find("a", {"aria-label": "Next Page"}) if pagination else None

            if next_button:
                next_url = "https://www.indeed.com" + next_button['href']
                driver.get(next_url)
                page += 1
                time.sleep(2)  # Allow the next page to load
            else:
                print("Reached the last page.")
                break  # No "Next" button means we've reached the last page

        # Print all job details collected
        for idx, job in enumerate(jobs, 1):
            print(f"Job {idx}:")
            print(f"Title: {job['title']}")
            print(f"Company: {job['company']}")
            print(f"Location: {job['location']}")
            print(f"Pay: {job['pay']}")
            print(f"Link to Apply: {job['link']}\n")

    finally:
        driver.quit()
