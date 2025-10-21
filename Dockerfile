FROM python:3.8-slim-buster

# Ensure apt commands don't fail and install awscli cleanly
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        curl \
        unzip \
        ca-certificates \
        awscli && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
