# ✅ Updated base image to avoid deprecated Debian repositories
FROM python:3.8-slim-bullseye

# Ensure apt commands don't fail and install awscli cleanly
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        curl \
        unzip \
        ca-certificates \
        awscli && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run your app
CMD ["python3", "app.py"]