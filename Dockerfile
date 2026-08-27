FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

WORKDIR /app

# Install system dependencies (build-essential, libjpeg, zlib for Pillow)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Make build script executable and run static collection / migrations / seeding
RUN chmod +x /app/build.sh && /app/build.sh

EXPOSE 8000

CMD ["sh", "-c", "gunicorn portfolio.wsgi:application --bind 0.0.0.0:${PORT:-8000}"]
