import requests
import pandas as pd

url = "https://jsearch.p.rapidapi.com/search"

querystring = {
    "query": "Accounts Payable 7-12 years India remote OR hybrid OR onsite",
    "page": "1",
    "num_pages": "1"
}

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

jobs = []

for job in data["data"]:
    jobs.append({
        "Company": job["employer_name"],
        "Location": job["job_city"],
        "Job Title": job["job_title"],
        "Apply Link": job["job_apply_link"],
        "Work Type": job["job_employment_type"]
    })

df = pd.DataFrame(jobs)
df.to_excel("jobs.xlsx", index=False)

print("Excel file created!")
