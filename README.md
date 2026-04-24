# AWS_Data_Engineer_Pipeline_Airflow-UDACITY

Data Pipeline with Airflow and AWS RedshiftThis project implements a production-grade data pipeline for Sparkify, a music streaming startup. The pipeline automates the ETL (Extract, Transform, Load) process by staging data from S3 to Redshift, transforming it into a dimensional model, and performing data quality checks.## Project OverviewThe goal is to move from manual data processing to a scheduled, automated workflow using Apache Airflow. The data consists of user activity logs and song metadata stored in JSON format on Amazon S3.### The Pipeline ArchitectureThe DAG follows a specific sequence of operations:Staging: Data is copied from S3 buckets to staging tables in Redshift.Fact Loading: The songplays fact table is populated from the staging data.Dimension Loading: Tables for users, songs, artists, and time are loaded using a truncate-insert pattern.Data Quality: Custom checks ensure that critical columns do not contain null values and that tables are not empty.## Directory StructureThe workspace is organized to support custom Airflow operators and SQL modularity:Plaintext/home/workspace/airflow/
├── dags/
│   └── cd0031-automate-data-pipelines/
│       └── project/
│           └── starter/
│               └── final_project.py        # Main DAG definition
├── plugins/
│   ├── final_project_sql_statements.py     # SQL insert queries
│   └── final_project_operators/           # Custom Operator classes
│       ├── __init__.py
│       ├── stage_redshift.py
│       ├── load_fact.py
│       ├── load_dimension.py
│       └── data_quality.py
└── set_connections_and_variables.sh       # Setup script for AWS/Redshift

## Setup Instructions### 1. Initialize AirflowBefore the webserver can be accessed, you must initialize the metadata database and create an admin user:Bash# Create the admin user
airflow users create \
    --username admin \
    --firstname Gaurav \
    --lastname Bisht \
    --role Admin \
    --email gauravbisht2709@gmail.com \
    --password admin
    
### 2. Configure Connections & VariablesRun the provided shell script to automatically inject your AWS credentials and Redshift cluster details into Airflow:Bash/bin/bash /home/workspace/airflow/set_connections_and_variables.sh
Note: This sets aws_credentials, redshift connections, and the s3_bucket variable.### 3. Start Background ServicesEnsure the Airflow Scheduler and Webserver are running in the background:Bashairflow scheduler -D
airflow webserver -D

## Custom OperatorsOperatorDescriptionStageToRedshiftExecutes a COPY command to move JSON data from S3 to Redshift.LoadFactOperatorLoads data into the fact table using SQL provided in SqlQueries.LoadDimensionOperatorLoads dimension tables with an optional append_only flag (False = Truncate).DataQualityOperatorRuns a list of SQL test cases against the database and raises an error on failure.## How to RunOpen the Airflow UI (Port 8080).Toggle the final_project DAG to ON.Click Trigger DAG.Monitor the Graph View; once all tasks turn dark green, the data has been successfully loaded into Redshift.## ValidationAfter the pipeline completes, verify the results in Redshift:SQLSELECT count(*) FROM songplays;
Author: Gaurav Singh BishtDate: April 2026
