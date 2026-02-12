# 🛡️ Motor Insurance AI System
### Next-Gen Automated Claims Processing & Risk Intelligence Platform

The **Motor Insurance AI System** is an enterprise-grade, end-to-end solution designed to revolutionize the insurance claims lifecycle. By synergizing **Computer Vision**, **Semantic Search (RAG)**, and **Predictive Analytics**, it automates damage assessment, validates policy coverage, and flags fraudulent activities in real-time.

> **Status**: Production Ready 🟢 | **Version**: 2.0.0 | **Focus**: Automation, Transparency, & Risk Insight

---

## � Problem Statement

Traditional motor insurance claims processing is:
*   **Manual and time-consuming**: Days or weeks to settle simple claims.
*   **Prone to human error**: Subjective damage assessment leads to inconsistencies.
*   **Opaque in decision reasoning**: Customers rarely understand why a claim was rejected.
*   **Difficult to audit at scale**: Manual reviews cannot easily track systemic bias or fraud.

**This system addresses these challenges** by combining computer vision for objective assessment, semantic retrieval for accurate policy application, and an automated decision engine for instant, auditable results.

---

## �🏗️ System Architecture

The platform operates on a modular **API-first analytics-driven** architecture, ensuring scalability and separation of concerns.

```mermaid
graph TD
    User[User / Agent] -->|Uploads Image & Claim| Frontend[React Frontend]
    Frontend -->|REST API| Backend[FastAPI Gateway]
    
    subgraph "Core Processing Pipeline"
        Backend -->|Image Data| CV[Computer Vision (YOLO)]
        Backend -->|Policy Query| RAG[Policy RAG Engine]
        Backend -->|Claim Data| DE[Decision Engine]
        
        CV -->|Damage Assessment| DE
        RAG -->|Coverage Validation| DE
    end
    
    subgraph "Data & Analytics"
        DE -->|Persist| DB[(PostgreSQL)]
        DB -->|Aggregated Data| Analytics[Insights Module]
    end
```

### 🔹 1. Visual Intelligence Pipeline
*   **Model**: YOLOv8 + Customized EfficientNet
*   **Function**: Detects vehicle parts, classifies damage severity (Scratch, Dent, Smash), and estimates repair costs.
*   **Output**: JSON-structured damage report with confidence scores.

### 🔹 2. Policy RAG Engine (Retrieval-Augmented Generation)
*   **Stack**: FAISS Vector DB + SentenceTransformers + Llama 3 (Ollama)
*   **Function**: Semantically retrieves specific coverage clauses from complex PDF policy documents based on claim context.
*   **Benefit**: Eliminates manual policy reading; instantly verifies if a specific accident type is covered.

### 🔹 3. Automated Decision Engine
*   **Logic**: Synthesis of Visual Damage + Policy Coverage + Fraud Indicators.
*   **Outcome**: Generates an instant **Approve**, **Reject**, or **Flag for Review** recommendation with a transparent text explanation.

---

## 🔄 End-to-End Claim Flow

1.  **Submission**: User uploads vehicle damage images and incident details via the React Frontend.
2.  **Analysis**: The Computer Vision pipeline detects damage type and severity.
3.  **Retrieval**: The Policy RAG engine retrieves relevant coverage clauses based on the incident description.
4.  **Decision**: The Decision Engine combines damage data + policy context to form a judgment.
5.  **Result**: The claim is Approved, Rejected, or Flagged, with a generated explanation.
6.  **Insight**: The Analytics module aggregates this data to update insurer risk profiles and strictness rankings.

---

## 🚀 Key Capabilities

### 🔍 Precision Damage Detection
Automated identification of 15+ vehicle parts and damage types. Capable of distinguishing between cosmetic scratches and structural failure.

### 📜 Intelligent Policy Interpretation
Uses LLMs to "read" and "understand" policy documents. It doesn't just search keywords; it understands context (e.g., "Force Majeure" coverage during a storm).

### 🧠 Explainable AI (XAI) Decisions
Every decision comes with a **"Why?"**. The system generates human-readable explanations citing specific policy clauses and image evidence.

### 📊 Insurer Analytics & Ranking
**NEW**: A dedicated module that ranks insurance providers based on claim approval strictness, processing speed, and customer satisfaction metrics.

### ⚖️ Risk Exposure Insights
Calculates a **Customer Risk Score** by analyzing historical data, vehicle age, and accident frequency, helping insurers adjust premiums dynamically.

---

## 🧪 Real-World Applicability

This project simulates a production insurance workflow and demonstrates:
*   **AI Model Orchestration**: Chaining vision and language models effectively.
*   **Retrieval-Augmented Generation (RAG)**: Solving the "hallucination" problem in key business logic.
*   **Business Intelligence**: Transforming raw claim data into actionable strategic insights.
*   **Clean Architecture**: Separation of backend, ML, and analytics layers for maintainability.

---

## 📈 Policy Analytics & Insights Module

A completely new transparency layer designed for Underwriters and Auditors.

| Feature | Description | Business Value |
| :--- | :--- | :--- |
| **Clause Distribution** | Heatmap of most frequently invoked policy exclusions. | Identify ambiguous clauses causing disputes. |
| **Strictness Index** | Comparative scoring of insurer rejection rates. | Benchmarking for regulatory compliance. |
| **Cross-Company Similarity** | Jaccard similarity analysis of policy wordings. | Detect plagiarism or standard market shifting. |
| **Exposure Heatmap** | Geographic and demographic risk clustering. | Better portfolio risk management. |

---

## 🛠️ Technical Stack

### **Backend & Core API**
*   **Framework**: FastAPI (Python 3.9+)
*   **Auth**: JWT (JSON Web Tokens) with Role-Based Access Control (RBAC)
*   **Persistence**: PostgreSQL (SQLAlchemy ORM)

### **Machine Learning & AI**
*   **Vision**: YOLOv8, OpenCV
*   **LLM / NLP**: Ollama (Llama 3), SentenceTransformers (`all-MiniLM-L6-v2`)
*   **Vector Search**: FAISS (Facebook AI Similarity Search)

### **Frontend**
*   **Framework**: React 18
*   **Build Tool**: Vite
*   **Styling**: Tailwind CSS / Custom CSS Modules
*   **Visualization**: Chart.js / Recharts for Analytics

---

## 🔌 API Overview

Core RESTful endpoints available at `/docs`:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/claims/submit` | Multipart submission (Images + Metadata). Triggers full pipeline. |
| `GET` | `/api/claims/{id}` | Retrieve claim status, decision, and AI explanation. |
| `POST` | `/api/rag/query` | Ad-hoc semantic search against policy documents. |
| `GET` | `/api/analytics/ranking` | **[New]** Retrieve insurer strictness rankings. |
| `GET` | `/api/analytics/distribution` | **[New]** Get clause usage statistics. |

---

## 📐 Design Principles

1.  **Separation of Concerns**: Strict boundary between the minimal frontend (dumb UI) and the intelligent backend (business logic).
2.  **Stateless API Design**: Fully RESTful architecture allowing horizontal scaling of the inference engine.
3.  **Fail-Safe Persistence**: Claims are saved to the database *before* heavy processing begins, ensuring zero data loss during inference crashes.
4.  **Lazy Model Loading**: AI models are loaded into memory only on startup or first request to optimize resource usage.

---

## ⚡ Performance Considerations

*   **Lazy Loading**: Heavy ML models are only loaded when needed, reducing startup time and idle memory footprint.
*   **FAISS Indexing**: Policy embeddings are precomputed and stored, enabling sub-millisecond retrieval speeds even with large document sets.
*   **Cached Analytics**: Expensive aggregation queries are cached to ensure the dashboard remains snappy.

## 🔐 Security Considerations

*   **Authentication**: Secure JWT-based stateless authentication.
*   **Authorization**: Granular RBAC ensures Policy Holders cannot access Analytics or other users' claims.
*   **Configuration**: All sensitive secrets (DB credentials, API keys) are managed via environment variables.

---

## 📂 Project Structure

```bash
Motor-Insurance-AI/
├── backend/                   # Python FastAPI Logic
│   ├── analytics/             # 📊 New Analytics Module
│   │   ├── policy_insights/   # Ranking & Similarity Logic
│   │   └── router.py          # Analytics Endpoints
│   ├── core/                  # Config & Security
│   ├── db/                    # PostgreSQL Models & Schemas
│   ├── llm/                   # Llama 3 Integration
│   ├── ml/                    # YOLO & Computer Vision
│   ├── rag/                   # FAISS Vector Search
│   ├── main.py                # Application Entry Point
│   └── requirements.txt
├── Frontend/
│   └── modified_frontend/     # React Application
├── data/                      # Policy Documents & Datasets
├── .env.example               # Configuration Template
├── start-project.ps1          # 🚀 One-Click Windows Launcher
└── README.md                  # Documentation
```

---

## 🚢 Deployment & Setup

### Prerequisites
*   **PostgreSQL**: Running locally.
*   **Ollama**: Installed with `llama3` model (`ollama run llama3`).
*   **Python 3.8+** & **Node.js 16+**.

### 1️⃣ Environment Configuration
Create a `.env` file in the root directory:
```ini
DATABASE_URL=postgresql://user:pass@localhost:5432/motor_insurance_db
SECRET_KEY=your_secure_production_key
VITE_API_URL=http://localhost:8000
```

### 2️⃣ Quick Start (Windows)
We provide a unified launcher script that handles virtual environments and dependency checks:
```powershell
./start-project.ps1
```

### 3️⃣ Manual Start
*   **Backend**: `uvicorn main:app --reload`
*   **Frontend**: `npm run dev`

---

© 2024 Motor Insurance AI Solutions. All Rights Reserved.