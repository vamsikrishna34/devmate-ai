#  Devmate AI

An intelligent GenAI code reviewer powered by Hugging Face and FastAPI.  
Devmate AI offers smart suggestions, semantic analysis, and an elegant frontend — built for engineers, collaborators, and recruiters alike.

---

##  Features

-  **Code Reviews with Codet5**: Receive contextual feedback, detect issues, and get improvement tips
-  **Semantic Diff**: Compare logic and meaning between code versions using sentence-transformers
-  **FastAPI Backend**: Clean modular architecture with Docker-ready deployment
-  **Frontend via GitHub Pages**: Seamless client-side UI to submit code and view results
-  **Modular Design**: Scalable architecture for multi-agent workflows and GenAI extensions

---

## 📍 Demo Links

| Service         | Link |
|----------------|------|
| 🔗 Frontend     | [https://vamsikrishna34.github.io/devmate-ai/] |
| 🔗 Backend API  | [https://devmate-ai.onrender.com/review]|



---

## 📦 Installation (Local)

```bash
git clone https://github.com/vamsikrishna34/devmate-ai.git
cd devmate-ai
pip install -r requirements.txt
uvicorn main:app --reload
