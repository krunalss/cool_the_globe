# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock to the container
COPY pyproject.toml poetry.lock /app/

# Install dependencies with Poetry, no virtual environment
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of the application code
COPY . /app

# Expose port 8000 (or whatever port your app is using)
EXPOSE 8000

# Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
