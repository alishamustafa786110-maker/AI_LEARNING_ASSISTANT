# AI_LEARNING_ASSISTANT
````markdown
# 🤖 AI Learning Assistant

An AI-powered learning assistant built with **Streamlit**, **Groq**, and **GPT OSS 120B**.

The application helps students learn concepts, understand programming, create study notes, and practice through quizzes.

---

## ✨ Features

- 💬 AI-powered chat interface
- 🧠 Beginner, Intermediate, and Advanced learning levels
- 📚 Multiple learning modes
- 💡 Concept explanations
- 💻 Programming and coding assistance
- 📝 Study notes generation
- ❓ Interactive quiz mode
- 🗑️ Clear conversation
- 🔐 Secure API key management
- ☁️ Ready for Streamlit Cloud deployment

---

## 🛠️ Technologies

- Python
- Streamlit
- Groq API
- GPT OSS 120B

---

## 📁 Project Structure

```text
ai-learning-assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml
````

> `.streamlit/secrets.toml` is used only for local development and should never be committed to GitHub.

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-learning-assistant.git
```

Go into the project directory:

```bash
cd ai-learning-assistant
```

---

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure your Groq API key

Create this folder:

```text
.streamlit
```

Inside it, create:

```text
secrets.toml
```

Add:

```toml
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
```

Never upload this file to GitHub.

---

### 5. Start the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## ☁️ Deploy to Streamlit Community Cloud

1. Push this project to GitHub.
2. Open Streamlit Community Cloud.
3. Sign in with GitHub.
4. Create a new app.
5. Select this repository.
6. Select the `main` branch.
7. Set the main file to:

```text
app.py
```

8. Add your secret in Streamlit Cloud:

```toml
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
```

9. Deploy the application.

---

## 🔐 Security

Never put your Groq API key directly inside `app.py`.

Do not commit:

```text
.streamlit/secrets.toml
```

to GitHub.

If an API key is accidentally exposed publicly, revoke it and create a new one.

---

## 📸 Screenshots

Add screenshots of your application here after deployment.

Example:

```text
screenshots/
├── home.png
└── chat.png
```

---

## 📌 Future Improvements

Possible future features include:

* 📄 PDF document learning
* 📚 Upload study materials
* 🔎 Web search
* 🎙️ Voice interaction
* 🧑‍🏫 Personalized learning plans
* 📊 Student progress tracking
* 🧠 Retrieval-Augmented Generation (RAG)
* 👥 User accounts
* 💾 Persistent conversation history

---

## 👨‍💻 Author

**YOUR NAME**

Built with Python, Streamlit, Groq, and GPT OSS.

---

## 📄 License

This project is available for educational and personal use.

````

### Your project now

```text id="x6v8os"
ai-learning-assistant/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
````

We're almost ready to test it locally.

**Next file: `.streamlit/secrets.toml`**. This one is different because **you should create it locally but NOT push it to GitHub**.
