# 📊 Company Researcher  
Multi-Agent AI System using CrewAI for Automated Company Intelligence  

---

## 🚀 Overview  

Company Researcher is a multi-agent AI system built using CrewAI that automates company research and generates structured reports using LLMs.

The system uses role-based agents to:
- Collect real-time company data from the web  
- Analyze and summarize insights  
- Generate structured outputs using a defined schema  

---

## 🧠 Architecture  

User Input (Company Name)  
        ↓  
Researcher Agent (Web Search)  
        ↓  
Analyst Agent (Analysis & Report Generation)  
        ↓  
Structured Output (Pydantic Model)  
        ↓  
Markdown Report (output/final_report.md)  

---

## 🤖 Agents  

### Researcher Agent  
- Role: Senior Researcher  
- Goal: Collect relevant and important company information  
- Tools: SerperDevTool (web search)  
- LLM: llama3.1 (Ollama)  

### Analyst Agent  
- Role: Reporting Analyst  
- Goal: Analyze research and generate concise reports  
- LLM: llama3.1 (Ollama)  

---

## 📋 Tasks  

### Research Task  
- Research company data online  
- Collect relevant and important information  

### Analysis Task  
- Analyze research findings  
- Generate structured report  
- Save output to file  

Output file:  output/final_report.md

---

## 🧾 Structured Output  

The final report follows this schema:


class CompanyReport(BaseModel):  
Name: str  
Summary: str  
Technical_Focus: str  
Future_Aspirations: str  

---

## ⚙️ Tech Stack  

- Python  
- CrewAI  
- Ollama (llama3.1)  
- SerperDevTool  
- Pydantic  

---

## 📂 Project Structure  

```
Company_Researcher/
│
├── config/
│   ├── agents.yaml
│   ├── tasks.yaml
│
├── researcher/
│   └── crew.py
│
├── output/
│   └── final_report.md
│
├── main.py
├── requirements.txt
└── README.md
```


---

## ▶️ Running the Project  

### 1. Clone Repository  

git clone https://github.com/Maneesha01/Company_Researcher.git

cd Company_Researcher


### 2. Setup Environment  

python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
pip install -r requirements.txt


### 3. Add API Key  

Create `.env` file:  

SERPER_API_KEY=your_api_key


Make sure Ollama is running:  

ollama run llama3.1


### 4. Run  

python main.py


---

## 🔄 Workflow  

1. Input company name (default: Apple)  
2. Researcher Agent collects data  
3. Analyst Agent processes data  
4. Structured report is generated  
5. Output is saved and printed  

---

## 📊 Example Output  


Name: Apple  
Summary: Global leader in consumer electronics  
Technical_Focus: AI, hardware-software integration  
Future_Aspirations: Expansion in AI and AR/VR  
