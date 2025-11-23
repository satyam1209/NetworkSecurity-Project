FROM python:3.10-slim-bullseye
WORKDIR /app

# Copy requirements first for better layer caching
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app

# RUN apt update -y && apt install awscli -y

CMD ["python3", "app.py"]