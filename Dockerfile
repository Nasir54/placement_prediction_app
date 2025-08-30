# Dockerfile for Streamlit app
FROM python:3.11-slim

WORKDIR /app

# Install minimal build deps if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app and model
COPY . .

ENV PORT=8501
EXPOSE 8501

CMD ["bash", "-lc", "streamlit run app_streamlit.py --server.port $PORT --server.enableCORS false --server.headless true"]

