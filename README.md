# 💼 AI Career Counsellor Bot

An AI-powered career guidance application built using **Streamlit** and the **Groq API**. The application provides personalized career advice based on the user's background, helping students, working professionals, and career switchers make informed career decisions.

---

## 🚀 Features

- 🤖 AI-powered career counselling
- 🔑 Bring Your Own Groq API Key
- 👨‍🎓 Personalized guidance for different user profiles:
  - Student
  - Working Professional
  - Career Switcher
- 💬 Interactive chat interface
- 🧠 Context-aware conversations with chat history
- ⚡ Fast responses powered by Groq's Llama 3.3 70B Versatile model
- 🗑️ One-click option to clear chat history
- 🎨 Simple and intuitive Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API
- Llama 3.3 70B Versatile

---

## 📂 Project Structure

```text
.
├── app.py
├── requirements.txt
├── README.md
└── .env (optional)
```

---

## ▶️ Running the Application

Launch the Streamlit application using:

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. Enter your Groq API key in the sidebar.
2. Select your career profile:
   - Student
   - Working Professional
   - Career Switcher
3. Ask any career-related question.
4. Receive personalized, AI-generated guidance based on your profile and conversation history.

---

## 📷 Workflow

```text
User
 │
 ▼
Enter Groq API Key
 │
 ▼
Select Career Profile
 │
 ▼
Ask Career Question
 │
 ▼
Groq Llama 3.3 70B Model
 │
 ▼
Personalized Career Advice
```

---

## 💬 Example Questions

- What skills should I learn to become a Data Scientist?
- Should I pursue higher studies or start working?
- How can I negotiate a better salary?
- I want to switch from Mechanical Engineering to Software Development. Where should I start?
- Which certifications will help me advance my career?
- How can I prepare for technical interviews?

---

## 🔒 Security

The application requires users to provide their own Groq API key during runtime. The API key is used only for the current session and is **not stored** by the application.

---

## 🌟 Future Enhancements

- Resume review and feedback
- Career roadmap generation
- Interview preparation assistant
- Resume and cover letter generation
- Job role recommendations
- Skill gap analysis
- Chat export functionality
- Dark mode and UI improvements

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Built with ❤️ using **Python**, **Streamlit**, and **Groq**.
