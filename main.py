from flask import Flask, render_template, request, redirect, url_for, session
import os
from utils import extract_text_from_pdf, chunk_text, search_in_chunks

from google_search import google_search
from llm_search import query_openai_api

GOOGLE_API_KEY = ""
GOOGLE_CSE_ID = ""


app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.secret_key = 'supersecretkey'  # Change this in production!

UPLOAD_FOLDER = 'app/uploads'  # This is where PDFs will be saved
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['pdf']
        if uploaded_file.filename != '':
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            uploaded_file.save(filepath)
            
            # Extract text from the uploaded PDF
            pdf_text = extract_text_from_pdf(filepath)
            
            # Chunk the text into smaller pieces for display
            chunks = chunk_text(pdf_text)
            session['chunks'] = chunks

            
            # Pass the chunks to the chat.html template to display them
            return render_template('chat.html', chunks=chunks)
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.form['question']
    chunks = session.get('chunks', [])

    # 1. First, check inside PDF
    answer = search_in_chunks(user_question, chunks)
    if answer:
        return render_template('answer.html', answer=answer, source="PDF")

    try:
        # 2. Ask OpenAI
        llm_answer = query_openai_api(user_question)
    except Exception as e:
        print(f"OpenAI error: {e}")
        llm_answer = None

    # 3. Always fetch Google results
    results = google_search(user_question, GOOGLE_API_KEY, GOOGLE_CSE_ID)

    if llm_answer:
        return render_template('answer.html', answer=llm_answer, results=results, source="LLM")
    else:
        return render_template('answer.html', results=results, source="Google (Fallback)")
@app.route('/reset')
def reset():
    session.pop('chunks', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
