# main.py

# Define pathways with associated job titles, without "Intern"
keywords_by_pathway = {
    "Software Engineering": [
        "Software",
        "Software Engineer",
        "Software Developer",
        "Full Stack Developer",
        "Backend Developer",
        "Frontend Developer"
    ],
    "Cybersecurity": [
        "Security",
        "Cybersecurity",
        "Security Analyst",
        "Security Engineer",
        "SOC Analyst"
    ],
    "Data Science and Analytics": [
        "Data Scientist",
        "Data Analyst",
        "Machine Learning",
        "AI Specialist"
    ],
    "Cloud Computing and DevOps": [
        "Cloud Engineer",
        "DevOps Engineer",
        "Site Reliability Engineer",
        "Systems Engineer"
    ],
    "Mobile Development": [
        "Mobile Developer",
        "iOS Developer",
        "Android Developer"
    ],
  
}

from scrape import scrape_jobs  # Import the scraping function from scrape.py

def main():
    # Loop through each pathway and associated job titles
    for pathway, keywords in keywords_by_pathway.items():
        print(f"Searching jobs for pathway: {pathway}")
        
        for keyword in keywords:
            # Dynamically append "Intern" to each job title
            job_title = f"{keyword} Intern"
            print(f"Searching jobs with title: {job_title}")
            # Call the scrape_jobs function for each job title
            scrape_jobs(job_title=job_title, city=None, date_posted="7")

if __name__ == "__main__":
    main()
