# fulhaus-aptitude-test

### Deployment and Testing Instructions

1. Please cone the repository 
2. Change the directory to the root of this repository
3. Use the docker-compose.yaml file to build and run the docker image

  ```docker compose build```
  ```docker compose up```
  
4. Once the Flask app is running, make a POST request with the image file

```
curl --location '{{domain}}/get_results' \
--form 'file=@"{{image_file}}"'
```

### System Design

<p float = "left">
  <img src="readme_images/fulhaus-architecture.jpeg" width = 400 >
</p>
