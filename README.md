# 📊 Company Researcher

Multi-Agent AI System using CrewAI for Automated Company Intelligence

---

## 🚀 Overview

Company Researcher is a multi-agent AI system built using CrewAI that automates company research and generates **structured, source-grounded reports** using LLMs.

The system uses role-based agents to:

* Collect real-time company data from the web
* Analyze and synthesize insights
* Generate structured outputs with explicit fields and source references

---

## 🧠 Architecture

User Input (Company Name)  
↓  
Researcher Agent (Web Search + Source Collection)  
↓  
Analyst Agent (Analysis & Structured Report Generation)  
↓  
Pydantic Structured Output (Validated Schema)  
↓  
Markdown Report (output/final_report.md)  

---

## 🤖 Agents

### Researcher Agent

* Role: Senior Researcher
* Goal: Collect relevant company data along with **source links**
* Tools: SerperDevTool (web search)
* LLM: llama3.1 (Ollama)

### Analyst Agent

* Role: Reporting Analyst
* Goal: Analyze research and generate **structured, concise reports**
* LLM: llama3.1 (Ollama)

---

## 📋 Tasks

### Research Task

* Performs web search for company information
* Collects **relevant insights + source URLs**

### Analysis Task

* Processes research data
* Generates structured report using schema
* Saves output to file

Output file: `output/final_report.md`

---

## 🧾 Structured Output Schema

The final report follows a strongly-typed schema:

```python
class CompanyReport(BaseModel):
    """Detailed Research on company"""

    name: str = Field ("Official name of the company")
    summary: str = Field ("Brief 1 or 2 lines overview describing what the company does")
    technical_focus: List[str] = Field("Core technologies, domains, or technical areas focus of company")
    key_products: List[str] = Field("Major products or services offered by the company")
    competitors: List[str] = Field("Main competing companies in the same market or domain")
    risks: List[str] = Field("Potential risks such regulations, or technical challenges")
    sources: List[str] = Field("List of URLs or references used to gather the information")
```

### 📌 Key Improvements

* Structured multi-field output (not plain text)
* Explicit **source grounding**
* Better representation of real-world company insights (products, competitors, risks)

---

## ⚙️ Tech Stack

* Python
* CrewAI
* Ollama (llama3.1)
* SerperDevTool
* Pydantic

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

```
git clone https://github.com/Maneesha01/Company_Researcher.git
cd Company_Researcher
```

### 2. Setup Environment

```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Add API Key

Create `.env` file:

```
SERPER_API_KEY=your_api_key
```

Make sure Ollama is running:

```
ollama run llama3.1
```

### 4. Run

```
python main.py
```

---

## 🔄 Workflow

1. Input company name (default: Apple)
2. Researcher Agent collects data + sources
3. Analyst Agent structures insights
4. Validated report is generated
5. Output is saved and printed

---

## 📊 Example Output

```
Name: Apple  
Summary: Global leader in consumer electronics and software ecosystem  
Technical Focus: ["AI", "Consumer Electronics", "Chip Design"]  
Key Products: ["iPhone", "MacBook", "iCloud"]  
Competitors: ["Samsung", "Microsoft", "Google"]  
Risks: ["Supply chain dependency", "Market saturation"]  
Sources: ["https://...", "https://..."]
```

---

## 🚧 Future Improvements

* Evaluation metrics (accuracy, relevance)
* UI for interactive usage

---
