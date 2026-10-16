# Cloud Deployment Lab

A simple Flask web application containerized using Docker and prepared for deployment on AWS EC2.

## Technologies Used
- Python
- Flask
- Docker
- Git and GitHub
- AWS EC2

## Project Files
- `app.py` — Flask web application
- `requirements.txt` — Python dependencies
- `Dockerfile` — Instructions to build the Docker image

## Run Locally

Build the Docker image:

```bash
docker build -t cloud-deployment-lab:1.0.0 .
```

Run the container:

```bash
docker run -d --name cloud-lab -p 5000:5000 cloud-deployment-lab:1.0.0
```

Open http://localhost:5000 in your browser.

## Stop the Container

```bash
docker stop cloud-lab
docker rm cloud-lab
```

## Deployment Goal
Deploy the Dockerized Flask application on an Ubuntu EC2 instance and access it through its public IP address.