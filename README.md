# fulhaus-aptitude-test

### Deployment and Testing Instructions

1. Please cone the repository 
2. Change the directory to the root of this repository
3. Use the docker-compose.yaml file to build and run the docker image
<br /><br />
  ```docker compose build```
<br /><br />
  ```docker compose up```

4. Once the Flask app is running, make a POST request with the image file

```
curl --location '{{local_docker_host}}/get_results' \
--form 'file=@"{{image_file}}"'
```

### System Design

<p float = "left">
  <img src="fulhaus-architecture.jpeg" width = 400 >
</p>

The user interacts with the REST service, by uploading the image.

The REST service logs the request in a metadata table to maintian the requests made to the service, along with other statistics from the Model.

The image uploaded by the user can be added to the training set, an additional step is required to annotate the data with a label.

The model training can be scheduled using Apache Airflow, with Spark jobs training the model.
