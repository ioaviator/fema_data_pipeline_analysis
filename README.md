# FEMA Data Pipeline Analysis
## A data pipeline that aggregates and processes detailed information on public assistance funded projects from FEMA’s open data APIs.

# Architecture Overview

            +----------------+
            |      FEMA API   |
            +--------+--------+
                     |
                     v
            +--------+--------+
            | Apache Airflow  |   (Ingests data from API)
            +--------+--------+
                     |
                     v
         +-----------+-----------+
         | Azure Data Lake Storage |
         +-----------+-----------+
                     |
                     v
            +--------+--------+
            | Apache Airflow  |   (Processes and transforms data)
            +--------+--------+
                     |
                     v
         +-----------+-----------+
         |   PostgreSQL Database  |
         +-----------+-----------+
                     |
                     v
              +------+------+
              |   Power BI   |   (Visualization)
              +-------------+

# Extracting the Data
## This step involves ingesting the data from the source server, which in this case is the FEMA API.
### The data is extracted using the requests library in Python. The API URL is specified, and a GET request is made ### to retrieve the data.
#### The response is then parsed into a JSON format for further processing.

# Transforming the Data
## After extracting the data, it is transformed into a structured format suitable for analysis.
## This involves cleaning the data, handling missing values, and converting data types as necessary.

# Loading the Data
## The final step in the pipeline is loading the transformed data into a destination database or file format for ## storage and further analysis.
## Here, the processed data is stored in a PostgreSQL database and made ready for visualization using Power BI.

# DevOps & Deployment
## Code Repository: GitHub

## CI/CD Pipeline: GitHub Actions automatically builds and tests code.

## Containerization: Docker is used for packaging Python scripts.

## Image Hosting: Docker Hub stores and manages container images.

## Infrastructure as Code: Terraform provisions and manages Azure resources.

## Technologies Used
## Apache Airflow — Workflow orchestration

## Azure Data Lake Storage — Cloud storage for raw data

## PostgreSQL — Relational database for processed data

## Power BI — Data visualization and reporting

## Python — Data ingestion and transformation scripts

## Docker — Containerization

## GitHub Actions — CI/CD automation

## Terraform — Infrastructure provisioning

