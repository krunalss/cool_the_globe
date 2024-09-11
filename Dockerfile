# Use an official Python 3.10 runtime as a parent image
FROM python:3.10-slim

# Install system dependencies required by Poetry and Python packages
RUN apt-get update \
    && apt-get install -y curl build-essential libssl-dev libffi-dev \
    && apt-get clean

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Set the working directory in the container
WORKDIR /app

# Copy only pyproject.toml and poetry.lock first to leverage Docker caching
COPY pyproject.toml poetry.lock /app/

# Install dependencies with Poetry (without creating a virtual environment)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of the application code
COPY . /app

# Expose port 8000
EXPOSE 8000

# Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "${PORT}"]
