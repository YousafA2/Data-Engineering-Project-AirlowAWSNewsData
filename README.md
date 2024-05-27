# Data-Engineering-Project-AirlowAWSNewsData

The aim of this project is to demonstrate calling an API from newsapi.org and loading the data received into an S3 bucket within AWS. Apache Airflow was run on a virtual environment within an EC2 instance.

# Implemented DAG

The pipeline used was as follows:

![Screenshot 2024-05-27 161720](https://github.com/YousafA2/Data-Engineering-Project-AirlowAWSNewsData/assets/141333199/dca700ad-dd2b-45e5-bd02-6d28933b0a03)

The is_news_api_ready task checks if the News API is ready by making an HTTP request to the specified endpoint.

The extract_news_data task extracts news data from the News API.


# Requirments

Apache Airflow running on an EC2 instance.
Configuration of S3 bucket.

# Airflow Configuration

Navigate to Admin > Connections

![airflow step 1](https://github.com/YousafA2/Data-Engineering-Project-AirlowAWSNewsData/assets/141333199/c05d1fab-ff3a-4611-9075-ca61cd2a29a9)

Add a connection and input the connection id, connection type and host.

![airflow step 2](https://github.com/YousafA2/Data-Engineering-Project-AirlowAWSNewsData/assets/141333199/9d5568ac-6147-4583-b8b5-6fd0756cf31d)

Upon successful configuration, the DAG appears in th UI and can be run manually or according to the schedule.

![airflow step 3](https://github.com/YousafA2/Data-Engineering-Project-AirlowAWSNewsData/assets/141333199/4fea5936-7680-4fb1-b0ca-5c23ed6fc765)
