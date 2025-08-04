# Classifier-dbt

A containerized NLP pipeline that preprocesses text, computes TF-IDF vectors, stores them in PostgreSQL, and serves classifications via a FastAPI. The project leverages dbt for data transformation and is managed with Docker Compose for easy deployment.

## Features

- **Text Classification**: Classify text documents into predefined categories using TF-IDF features
- **RESTful API**: FastAPI-based endpoints for easy integration
- **Data Pipeline**: Automated data processing and transformation using dbt (data build tool)
- **Containerized**: Easy deployment with Docker and Docker Compose
- **Persistent Storage**: PostgreSQL database for storing predictions and results

## Prerequisites

- Docker and Docker Compose
- Python 3.9+
- PostgreSQL
- dbt (Data Build Tool)

## Project Structure

```
SumAI/
├── api/                 # FastAPI application
│   ├── main.py         # API endpoints and business logic
│   └── requirements.txt # Python dependencies
├── checkpoint/         # Saved models and vectorizers
├── data/               # Raw and processed data
│   └── raw/            # Raw data files (e.g., bbc_data.csv)
├── db/                 # Database related files
│   └── SumAI/          # dbt project
└── docker-compose.yml  # Container orchestration
```

## Getting Started

### 1. Environment Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd SumAI
   ```

2. Create a `.env` file in the root directory with the following variables:
   ```
   POSTGRES_USER=your_username
   POSTGRES_PASSWORD=your_password
   POSTGRES_DB=news
   ```

### 2. Running with Docker

1. Build and start the services:
   ```bash
   docker-compose up --build
   ```

2. The API will be available at `http://localhost:8000`

### 3. API Endpoints

- `GET /health`: Health check endpoint
- `GET /classify?text=your_text_here`: Classify input text

Example usage:
```bash
curl "http://localhost:8000/classify?text=This%20is%20a%20sports%20article"
```

## Development

### Setting up a development environment

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r api/requirements.txt
   ```

3. Run the API locally:
   ```bash
   uvicorn api.main:app --reload
   ```

## Database Management

The project uses dbt for data transformation. To run dbt models:

```bash
cd db/SumAI
dbt run
```
