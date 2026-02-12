# 🖥️ Motor Insurance AI – Frontend

This is the **React + Vite frontend** for the Motor Insurance AI System.

It provides an interactive interface for:
- Submitting motor insurance claims
- Uploading vehicle damage images
- Viewing AI-based approval/rejection decisions
- Reading explainable policy clause references
- Exploring insurer analytics & rankings

---

## 🚀 Features

### 📤 Claim Submission
- Upload vehicle damage images
- Enter claim metadata
- Track claim status in real-time

### 🧠 AI Decision Display
- Shows damage assessment results
- Displays policy coverage validation
- Provides clear approval/rejection explanations

### 📊 Analytics Dashboard
- Insurer Strictness Ranking
- Clause Distribution Insights
- Cross-Company Similarity Analysis
- Risk Exposure Metrics

---

## 🛠️ Tech Stack

- **React 18**
- **Vite**
- **Axios** (API integration)
- **Tailwind CSS / CSS Modules**
- **Chart.js / Recharts** (Analytics Visualization)

---

## ⚙️ Configuration

The frontend connects to the FastAPI backend via environment variable:

Create a `.env` file inside this directory:

```env
VITE_API_URL=http://localhost:8000
