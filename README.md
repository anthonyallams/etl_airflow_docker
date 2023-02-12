## To run, do the following:

### Build the airflow image from Dockerfile

`docker-compose build`

### Start the airflow process in docker-compose.yaml

`docker compose up -d `

### To run on command line, get the container id for webserver

`docker ps`

### Using the container gotten above, run docker exec command below

`docker exec -it <container_id> bash`

### Once in container, run the Dag tasks test below to test the dag on command line

`airflow tasks test <dag-id> <task-id> <execution-date-in-the-past>`
`airflow tasks test dag_for_flask_V001 call_flask 2023-02-05`

### To test curl, open a new cmd terminal and run the following

`curl 0.0.0.0:5005`

### To run the Dag on webserver ui

`http:0.0.0.0:8080`
