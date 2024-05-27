# Data-Engineering-Project-AirlowAWSNewsData

The aim of this project is to demonstrate calling an API from newsapi.org and loading the data received into an S3 bucket within AWS. Apache Airflow was run on a virtual environment within an EC2 instance.

# Implemented DAG:

The pipeline used was as follows:

![Screenshot 2024-05-27 161720](https://github.com/YousafA2/Data-Engineering-Project-AirlowAWSNewsData/assets/141333199/dca700ad-dd2b-45e5-bd02-6d28933b0a03)

The is_news_api_ready task checks if the News API is ready by making an HTTP request to the specified endpoint.

The extract_news_data task extracts news data from the News API.
