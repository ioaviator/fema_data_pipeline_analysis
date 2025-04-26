# FEMA Data Pipeline Analysis
## A data pipeline that aggregates and processes detailed information on public assistance funded projects from FEMA’s open data APIs.

# Architecture Overview



# Extracting the Data
This step involves ingesting the data from the source server, which in this case is the FEMA API.
The data is extracted using the requests library in Python. The API URL is specified, and a GET request is made ### to retrieve the data.
The response is then parsed into a JSON format for further processing.

# Transforming the Data
--.After extraction, the data is transformed into a structured format suitable for analysis.
This includes:
Cleaning the data
Handling missing values
Converting data types (e.g., dates, currency values)
Preparing the data for database insertion

# The final step in the pipeline involves loading the transformed data into a PostgreSQL database.
The database serves as a centralized, structured repository, making the data ready for:
Analysis
Reporting
Dashboarding in Power BI.

# DevOps & Deployment
Code Repository: GitHub
CI/CD Pipeline: Automated builds and tests via GitHub Actions
Containerization: Python scripts packaged using Docker
Image Hosting: Docker Hub
Infrastructure as Code: Resources provisioned on Azure using Terraform

## Technologies Used
Apache Airflow — Workflow orchestration
Azure Data Lake Storage — Cloud storage for raw data
PostgreSQL — Relational database for processed data
Power BI — Data visualization and reporting
Python — Data ingestion and transformation scripts
Docker — Containerization
GitHub Actions — CI/CD automation
Terraform — Infrastructure provisioning

