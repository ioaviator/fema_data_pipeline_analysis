import pandas as pd
import requests

# FEMA API Endpoint
url = "https://www.fema.gov/api/open/v1/PublicAssistanceFundedProjectsDetails"
params = {
    "$top": 1000  # pagination
}

response = requests.get(url, params=params)

# Check response
if response.status_code == 200:
    data = response.json()['PublicAssistanceFundedProjectsDetails']
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv("fema_projects_raw.csv", index=False)
    print("Data saved to fema_projects_raw.csv")
else:
    print("Failed to fetch data:", response.status_code)
