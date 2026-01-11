from django.shortcuts import render
from .forms import SummarizerForm
from .utils import extract_pdf_text, extract_web_text, summarize_text


def home(request):
    summary = None
    error = None
    input_type = "pdf"  # default

    if request.method == "POST":
        form = SummarizerForm(request.POST, request.FILES)
        input_type = request.POST.get("input_type", "pdf")

        # ✅ Initialize variables FIRST
        pdf = None
        url = None
        text = None

        if form.is_valid():
            sentence_count = form.cleaned_data.get("sentence_count")

            if input_type == "pdf":
                pdf = form.cleaned_data.get("pdf_file")

                if not pdf:
                    error = "Please upload a PDF file."
                else:
                    text = extract_pdf_text(pdf)
                    if text is None:
                        error = "Uploaded file is not a valid PDF or contains no readable text."

            elif input_type == "url":
                url = form.cleaned_data.get("url")

                if not url:
                    error = "Please enter a valid URL."
                else:
                    text = extract_web_text(url)
                    if not text or not text.strip():
                        error = "Could not extract text from the provided URL."

            # ✅ Safe check before summarizing
            if isinstance(text, str) and text.strip():
                summary = summarize_text(text, sentence_count)
            elif not error:
                error = "No readable text found to summarize."

    else:
        form = SummarizerForm()

    return render(
        request,
        "index.html",
        {
            "form": form,
            "summary": summary,
            "error": error,
            "input_type": input_type,
        },
    )
