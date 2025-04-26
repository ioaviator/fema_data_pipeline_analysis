import requests

from include.ETL.config import URL


def extract():
  
  try:
      # FEMA API Endpoint
    response = requests.get(URL)
    
    # Raise an error for HTTP error codes (like 4xx or 5xx)
    response.raise_for_status()

    data = response.json()['PublicAssistanceFundedProjectsDetails']
      
  except requests.exceptions.RequestException as e:
    print(e)
  
  return data