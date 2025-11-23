FROM python:3.10-slim-bullseye
WORKDIR /app

# Copy requirements first for better layer caching
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install AWS CLI
RUN pip install --no-cache-dir awscli

# Copy application code
COPY . /app

CMD ["python3", "app.py"]