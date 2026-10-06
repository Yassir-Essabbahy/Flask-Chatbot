# Automated Customer Support Chatbot — Flask & Python

[![Python Version](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Frontend](https://img.shields.io/badge/Frontend-HTML5%20%2F%20CSS3%20%2F%20JS-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://yessirdev.vercel.app)

An automated customer support chatbot web application built with Python and Flask. Designed to streamline client inquiries, provide real-time automated assistance, and manage conversation sessions through an accessible chat interface.

📁 **[Featured on Portfolio](https://yessirdev.vercel.app)**

---

## 💡 Features

* **Rule-Based & Intent Matching Flow**: Automatically identifies common customer support queries (account inquiries, pricing, store hours, technical support) and provides instant, formatted responses.
* **Flask REST API Backend**: Lightweight `/get_response` endpoint handling incoming messages with JSON payloads and error handling.
* **Modern Chat Messenger Interface**: Clean web chat interface with typing bubbles, auto-scrolling message feeds, and mobile responsiveness.
* **Session Persistence**: Maintains user context across conversation turns.

---

## 📁 Repository Structure

```
├── app.py              # Flask server, route controllers & response logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Accessible chat interface markup
└── static/
    ├── style.css       # Chat widget styling & message bubble design
    └── script.js       # Asynchronous fetch requests & DOM message rendering
```

---

## 🚀 Setup & Execution

1. Clone repository:
   ```bash
   git clone https://github.com/Yassir-Essabbahy/Flask-Chatbot.git
   cd Flask-Chatbot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Visit `http://127.0.0.1:5000` in your web browser.

---

## 👨‍💻 Author

**Yassir ESSABAHY** — Software & Game Developer  
* Portfolio: [yessirdev.vercel.app](https://yessirdev.vercel.app) | LinkedIn: [linkedin.com/in/yessir001](https://www.linkedin.com/in/yessir001/)
