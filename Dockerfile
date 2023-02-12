FROM apache/airflow:2.5.1-python3.10
EXPOSE 5005
COPY requirements.txt /requirements.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt
# CMD ["flask", "run", "--host", "0.0.0.0"]
