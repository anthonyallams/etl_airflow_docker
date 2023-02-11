from datetime import datetime, timedelta
from flask import Flask
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

#Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to this fabulosity!</h1>'

#DAG Functionalities
default_args = {
    'owner': 'Legend',
    'retry': 5,
    'retry_delay': timedelta(minutes=5)
}

def flask_app():
    app.run(host="0.0.0.0", port=5005)


with DAG(
    default_args=default_args,
    dag_id="dag_for_flask_V001",
    start_date=datetime(2023, 2, 6),
    schedule='@once',
    catchup=False
    ):
    call_flask = PythonOperator(
        task_id="call_flask",
        python_callable=flask_app
    )
    
call_flask