📄 PDF & Web Text Summarizer (Django + NLP)

A Django-based NLP web application that extracts text from PDF documents or web pages and generates clear, meaningful summaries using Natural Language Processing techniques.
This project demonstrates how NLP models can be integrated into a web application and deployed using Docker.

📌 Project Description

Reading long documents or articles can be time-consuming.
This project solves that problem by allowing users to upload a PDF file or provide a webpage URL and automatically generate a concise summary.
The application uses TextRank, an extractive NLP summarization technique, to identify and present the most important sentences in a readable format.

🎯 Key Features

-> Upload and summarize PDF documents
-> Fetch and summarize content from web pages
-> Adjustable summary length (number of sentences)
-> Sentence-wise, readable output
-> Error handling for invalid PDFs and URLs
-> Clean Django-based user interface
-> Fully Dockerized for easy deployment

🔁 Application Workflow
        User Input (PDF / URL)
                ↓
        Text Extraction
                ↓
        Text Preprocessing
                ↓
        NLP Summarization (TextRank)
                ↓
        Summary Display

🧠 Django Request–Response Flow
            User Request
               ↓
            urls.py
               ↓
            views.py
               ↓
            utils.py (NLP logic)
               ↓
            HTML Template
               ↓
            Response to User


This separation ensures clean architecture and maintainable code.

⚙️ How Summarization Works

-> Extracts raw text from PDFs or web pages
-> Cleans and preprocesses text
-> Applies TextRank to score sentences
-> Selects top-ranked sentences
-> Displays a concise, readable summary
-> This approach is fast, reliable, and easy to explain.

🛠️ Tech Stack
        Backend
        Python
        Django
        NLP & Machine Learning
        NLTK
        TextRank (Sumy)
        NumPy
        Data Extraction
        pdfplumber (PDF parsing)
        BeautifulSoup (Web scraping)
        Requests
        DevOps
        Docker
        Docker Hub

📁 Project Structure
        text_summarizer/
        │── manage.py
        │── requirements.txt
        │── Dockerfile
        │
        ├── summarizer/
        │   ├── views.py
        │   ├── utils.py
        │   ├── forms.py
        │   └── urls.py
        │
        ├── templates/
        │   └── index.html
        │
        └── text_summarizer/
            ├── settings.py
            ├── urls.py
            └── wsgi.py

🚀 Run the Project Locally
  1️⃣ Clone the Repository
  git clone https://github.com/GokulPawar636/django-nlp-text-summarizer.git
  cd text_summarizer
  
  2️⃣ Create Virtual Environment
  python -m venv env
  env\Scripts\activate   # Windows
  
  3️⃣ Install Dependencies
  pip install -r requirements.txt
  
  4️⃣ Run the Server
  python manage.py runserver
  
Open: http://127.0.0.1:8000/

🐳 Run Using Docker
  Pull Image from Docker Hub
  docker pull gokulpawar/django-text-summarizer

Run Container
  docker run -p 8000:8000 gokulpawar/django-text-summarizer


Open: http://localhost:8000/

