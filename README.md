## To run, do the following:

### Build the airflow image from Dockerfile

`docker-compose build`

### To run on command line, get the container id for webserver

`docker ps`
`docker exec -it <container_id> bash`

### Once in container, run the Dag tasks test below to test the dag on command line

`airflow tasks test <dag-id> <task-id> <execution-date-in-the-past>`
`airflow tasks test dag_for_flask_V001 call_flask 2023-02-05`

### To run the Dag on webserver ui

`http:0.0.0.0:8080`
