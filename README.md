
# 📄 Auto-content-creator

**A Document Q\&A system powered by LLMs (Large Language Models)**
This application allows users to upload documents (like PDFs) and ask questions based on their content. If the answer isn't found in the document, it intelligently queries Google Search for relevant results.

🔗 [Live Demo](https://llm-question-answer.onrender.com)

---

## ✨ Features

* 📚 Upload and query documents (PDF supported)
* 🤖 Local LLM-based document answering
* 🔎 External Google Search integration for broader queries
* 🌐 Deployed using Docker on Render
* 🛠️ Built with Flask, LangChain (or similar framework), and Google Custom Search API

---

## 🏗️ Project Structure

```
Auto-content-creator/
├── app/
│   ├── static/        
│   ├── templates/     
│   ├── uploads/       
├── project_venv/      
├── Dockerfile         
├── education_sample.pdf 
├── google_search.py   
├── llm_search.py      
├── main.py            
├── utils.py           
├── requirements.txt   
├── .gitignore         
└── README.md  
```

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Auto-content-creator.git
cd Auto-content-creator
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file with the following:

```ini
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_custom_search_engine_id
```

### 5. Run the Application

```bash
python main.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t llm_doc_qa .
```

### Run Docker Container

```bash
docker run -d -p 5000:5000 llm_doc_qa
```

---

## 🌍 Deployment on Render

This app is deployed on [Render](https://render.com) using Docker.

Be sure to set the following environment variables in Render's settings:

* `GOOGLE_API_KEY`
* `GOOGLE_CSE_ID`

---

## 📜 Technologies Used

* **Python**
* **Flask**
* **LangChain** / RAG-based approach
* **Google Custom Search API**
* **Docker**
* **Render.com** (Deployment)

---

## ✅ TODO

* [ ] Improve UI/UX for uploads and results
* [ ] Add support for more file formats (e.g., DOCX)
* [ ] Implement authentication (optional)
* [ ] Cache frequent queries

---

Feel free to customize further! Let me know if you want badges, screenshots, or usage examples added.
