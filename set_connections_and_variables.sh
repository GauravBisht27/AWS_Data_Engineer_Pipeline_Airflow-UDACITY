#!/bin/bash

# 1. Add AWS Credentials Connection
airflow connections add aws_credentials --conn-uri 'aws://AKIA4QE4NTH3R7EBEANN:s73eJIJRbnqRtll0%2FYKxyVYgrDWXfoRpJCDkcG2m@'

# 2. Add Redshift Connection (Using your specific endpoint and credentials)
airflow connections add redshift --conn-uri 'redshift://admin:Sparkify-123@sparkify-workgroup.381344489586.us-east-1.redshift-serverless.amazonaws.com:5439/dev'

# 3. Set S3 Variables (Using your specific bucket)
airflow variables set s3_bucket awss3-sparkify-pipeline

# 4. Set S3 Prefix
airflow variables set s3_prefix data-pipelines