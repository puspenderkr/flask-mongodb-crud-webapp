# Flask Application with MongoDB Docker Setup

This repository contains a simple Flask web application that uses MongoDB as its database, and it is containerized with Docker for easy deployment. Follow the instructions below to set up and run the application locally.

## Prerequisites

Before you begin, make sure you have the following software installed on your system:

- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/)

## Getting Started

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/flask-mongodb-docker-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd flask-mongodb-docker-app
    ```

## Building and Running the Docker Containers

3. Build the Docker image for the Flask application:

    ```bash
    docker build -t flask-app .
    ```

4. Start the Docker containers using Docker Compose:

    ```bash
    docker-compose up
    ```

This will start two containers: one for the Flask application and one for MongoDB. The Flask application will be accessible at `http://localhost:5000`.

## Accessing the Application

5. Open your web browser and go to `http://localhost:5000` to access the Flask application.

## Stopping the Application

To stop the running containers and remove them, press `Ctrl+C` in the terminal where you started the containers, and then run:

```bash
docker-compose down
```




# Running the web-app without using Docker

## Setup & Installation

Make sure you have the latest version of Python installed.

```bash
git clone <repo-url>
```

```bash
pip install -r requirements.txt
```

## Running The App

```bash
python app.py
```

## Viewing The App

Go to `http://127.0.0.1:5000`
