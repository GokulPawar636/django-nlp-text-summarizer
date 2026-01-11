import pdfplumber
import requests
import nltk
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from pdfminer.pdfparser import PDFSyntaxError
from pdfminer.pdfdocument import PDFTextExtractionNotAllowed



# ✅ SAFE: no find(), no zip crash
def ensure_nltk_data():
    nltk.download("punkt", quiet=True)
    nltk.download("punkt_tab", quiet=True)


ensure_nltk_data()


def extract_pdf_text(file):
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

    except (PDFSyntaxError, PDFTextExtractionNotAllowed, Exception):
        return None  # ❗ invalid or corrupted PDF

    return text if text.strip() else None


def extract_web_text(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all("p")
    return " ".join(p.text for p in paragraphs)


def summarize_text(text, sentence_count):
    if not text.strip():
        return []

    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, sentence_count)

    # ✅ Return list of sentences instead of one paragraph
    return [str(sentence) for sentence in summary]

def clean_sentences(sentences):
    cleaned = []
    for s in sentences:
        s = s.strip()
        if len(s) > 30 and s not in cleaned:
            cleaned.append(s)
    return cleaned

