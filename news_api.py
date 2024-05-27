from airflow import DAG
from datetime import timedelta, datetime
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
import json
from airflow.operators.python import PythonOperator
import pandas as pd



def transform_load_data(task_instance):
    data = task_instance.xcom_pull(task_ids="extract_news_data")
    titles = [article["title"] for article in data["articles"]]
    source = [article["source"]["name"] for article in data["articles"]]

    transformed_data = {"Title":titles,
                    "Source":source    
            }

    df_data = pd.DataFrame(transformed_data)
    aws_credentials = {"key": "###", "secret": "###", "token": "###"}
    now = datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")
    dt_string = 'current_news_data_apple_' + dt_string
    df_data.to_csv(f"s3://newsapibucketaws/{dt_string}.csv", index=False,storage_options=aws_credentials)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 8),
    'email': ['myemail@domain.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}



with DAG('news_dag',
        default_args=default_args,
        schedule_interval = '@daily',
        catchup=False) as dag:


        is_news_api_ready = HttpSensor(
        task_id ='is_news_api_ready',
        http_conn_id='news_api',
        endpoint='v2/everything?q=Apple&from=2024-05-26&sortBy=popularity&apiKey=###'
        )

        extract_news_data = SimpleHttpOperator(
        task_id = 'extract_news_data',
        http_conn_id = 'news_api',
        endpoint='v2/everything?q=Apple&from=2024-05-26&sortBy=popularity&apiKey=###',
        method = 'GET',
        response_filter= lambda r: json.loads(r.text),
        log_response=True
        )

        transform_load_news_data = PythonOperator(
        task_id= 'transform_load_news_data',
        python_callable=transform_load_data
        )

is_news_api_ready >> extract_news_data >> transform_load_news_data
