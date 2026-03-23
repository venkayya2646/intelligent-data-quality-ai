# 🧠 Intelligent Data Quality & AI Explanation System

An end-to-end data engineering project that performs automated data quality checks, detects anomalies using statistical techniques, and generates human-readable explanations using AI.

---

## 🚀 Project Overview

Modern data pipelines often fail silently due to data quality issues. This project solves that problem by building an **intelligent data observability system** that:

- Validates incoming data
- Detects anomalies (spikes, drops, inconsistencies)
- Uses AI to explain the root cause
- Alerts users for faster debugging

---

## 🏗️ Architecture


CSV Data → DuckDB → Data Quality Checks → Anomaly Detection → AI Explanation → Alerts


---

## 🛠️ Tech Stack

- **Python**
- **DuckDB** (Local Data Warehouse)
- **Pandas & NumPy**
- **LLM Integration** (OpenAI / Ollama - Local LLM)
- **VS Code**
- **Git & GitHub**

---

## 📂 Project Structure


intelligent-data-quality-ai/
│
├── data/ # Sample dataset
├── pipelines/ # Data ingestion
├── data_quality/ # Data validation checks
├── anomaly_detection/ # Statistical anomaly detection
├── ai_explanation/ # AI-based explanations
├── alerts/ # Alerting system
├── utils/ # DB connection
├── main.py # Pipeline runner
├── .gitignore
└── README.md


---

## ⚙️ How It Works

### 1. Data Ingestion
- Reads CSV data
- Loads into DuckDB (local database)

### 2. Data Quality Checks
- Row count validation
- Null checks
- Zero-value detection

### 3. Anomaly Detection
- Uses **Z-score method**
- Identifies unusual spikes or drops in data

### 4. AI Explanation
- Sends anomaly data to LLM
- Generates business-friendly explanations

### 5. Alerting
- Prints alerts to console (extendable to Slack/Email)

---

## ▶️ How to Run

### Step 1: Clone Repository
```bash
git clone https://github.com/your-username/intelligent-data-quality-ai.git
cd intelligent-data-quality-ai
Step 2: Create Virtual Environment
python -m venv venv
venv\Scripts\activate
Step 3: Install Dependencies
pip install -r requirements.txt
Step 4: Run Project
python main.py
🤖 AI Integration
Option 1: OpenAI API

Add your API key in .env file

Option 2: Local LLM (Recommended)

Install Ollama

Run:

ollama run llama3
```

📊 Sample Output

🚨 ALERT 🚨
Sales spike detected for product 'Phone'.

Possible reasons:
- Promotional campaign
- Bulk order
- Data ingestion issue

  
🌟 Key Features

Automated Data Quality Monitoring
Statistical Anomaly Detection (Z-score)
AI-Powered Root Cause Analysis
Modular Pipeline Design
Local Execution (No Cloud Required)


🚀 Future Enhancements

Airflow DAG for orchestration
Streamlit dashboard for visualization
Real-time streaming pipeline
Advanced anomaly detection (ML-based)
Slack / Email alert integration


🧠 Learnings

Handling real-world data quality issues
Integrating AI into data engineering workflows
Secure handling of API keys (.env, .gitignore)
End-to-end pipeline design


👨‍💻 Author

Venkat Yadlapalli


⭐ If you like this project

Give it a ⭐ on GitHub!


---

