# -----------------------------
# Base Image
# -----------------------------
FROM python:3.12.7

# -----------------------------
# Environment Variables
# -----------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# -----------------------------
# Set Working Directory
# -----------------------------
WORKDIR /app

# -----------------------------
# Install System Dependencies
# -----------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Copy Requirements
# -----------------------------
COPY requirements.txt /app/

# -----------------------------
# Install Python Dependencies
# -----------------------------
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Copy Django Project
# -----------------------------
COPY text_summarizer /app/text_summarizer

# -----------------------------
# Download NLTK Data
# -----------------------------
RUN python -m nltk.downloader punkt punkt_tab

# -----------------------------
# Expose Port
# -----------------------------
EXPOSE 8000

# -----------------------------
# Run Django Server
# -----------------------------
CMD ["python", "text_summarizer/manage.py", "runserver", "0.0.0.0:8000"]
