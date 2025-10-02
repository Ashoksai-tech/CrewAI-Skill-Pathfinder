## 🚀 CrewAI Skill Pathfinder

**CrewAI Skill Pathfinder** is an AI-powered, multi-agent system designed to help users navigate the evolving tech landscape. By leveraging CrewAI's collaborative agent framework, the system:

* Analyzes **real-time job market trends**
* Creates **personalized study plans**
* Suggests **career paths and certifications**

Currently, this is a **command-line application** using Python and CrewAI with integrated tools like Serper and Gemini APIs.

---

### ✅ **Core Features**

* 🧠 Autonomous agents for skill research, planning, and career guidance
* 🌐 Real-time data extraction from job boards and tech blogs
* 📘 Custom learning path generation using Gemini API
* 🎯 Career advice aligned with market trends

---

### 🛠️ **Tech Stack**

* [x] Python 3.10+
* [x] [CrewAI](https://github.com/joaomdmoura/crewAI) for multi-agent orchestration
* [x] Google Gemini API for AI responses
* [x] Serper.dev for job search data
* [x] dotenv for secure API key handling

---

### 📌 **Planned Enhancements**

The next phase of this project includes building a full-stack deployment using:

* ⚙️ **Backend:** [FastAPI](https://fastapi.tiangolo.com/) – to expose the agent functionality via RESTful API
* 💻 **Frontend:** [React.js](https://reactjs.org/) – to provide a user-friendly interface for interacting with agents

---

### 📂 **Project Structure**

```
project/
│
├── agents.py                  # All CrewAI agents
├── tasks.py                   # All CrewAI tasks
├── tools.py                   # Tool integrations like Serper and Gemini
├── crew.py                    # Main CrewAI orchestration logic
├── custom_gemini_tool.py      # Gemini tool wrapper
├── .env                       # Environment variables
└── README.md                  # You're here!
```

---

### 🔐 **Environment Variables (.env)**

```env
GEMINI_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key
CREWAI_LLM_PROVIDER=gemini
```

---

### 🤝 **Contributing**

FastAPI and React integration will be added soon. Contributions, feedback, and feature suggestions are welcome!

---
