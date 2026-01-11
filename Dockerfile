# ==============================
# Base Image
# ==============================
FROM python:3.12.7

# ==============================
# Environment Variables
# ==============================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ==============================
# Install System Dependencies
# ==============================
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# ==============================
# Set Working Directory
# ==============================
WORKDIR /app

# ==============================
# Copy Requirements
# ==============================
COPY requirements.txt .

# ==============================
# Install Python Dependencies
# ==============================
RUN pip install --no-cache-dir -r requirements.txt

# ==============================
# Copy Django Project Files
# (manage.py is copied here)
# ==============================
COPY . .

# ==============================
# Download NLTK Data
# ==============================
RUN python -m nltk.downloader punkt punkt_tab

# ==============================
# Expose Django Port
# ==============================
EXPOSE 8000

# ==============================
# Run Django Development Server
# ==============================
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
