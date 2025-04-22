# Fema_Data_Pipeline_Analysis
A data pipeline that aggregates and processes detailed information  on public assistance funded projects from FEMA’s open data APIs

# Extracting the Data 
This step involves ingesting the data from the source serve which in this case is the FEMA API. The data is extracted using the requests library in Python. The API URL is specified, and a GET request is made to retrieve the data. The response is then parsed into a JSON format for further processing.

# Transforming the Data 
After extracting the data, it is transformed into a structured format suitable for analysis. This involves cleaning the data, handling missing values, and converting data types as necessary.

# Loading the Data 
The final step in the pipeline is loading the transformed data into a destination database or file format for storage and analysis.