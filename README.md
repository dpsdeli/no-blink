# FastAPI Image Upload Service

A FastAPI-based service that handles image file uploads and returns the uploaded images.

## Features

- Image upload endpoint
- Docker containerization
- Health check endpoint
- FastAPI Swagger UI documentation

## Prerequisites

- Python 3.12
- Docker
- Docker Compose

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Build and run with Docker Compose:
```bash
docker-compose up --build
```

## API Endpoints

- `POST /upload-image/`: Upload an image file
- `GET /health`: Health check endpoint

## Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the development server:
```bash
uvicorn main:app --reload
```

## Docker Commands

- Build and start containers:
```bash
docker-compose up --build
```

- Stop containers:
```bash
docker-compose down
```

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:80/docs`
- ReDoc: `http://localhost:80/redoc`
