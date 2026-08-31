# Code Review Platform

An automated **Code Review Platform** built with **FastAPI** that analyzes Python code and identifies potential **security vulnerabilities** and **code-quality issues** using **Bandit** and **Ruff**. The platform uses **PostgreSQL** for database storage.

## 🚀 Features

* 🐍 Python code analysis
* 🔒 Security vulnerability detection using Bandit
* 🧹 Code-quality analysis using Ruff
* ⚡ REST API built with FastAPI
* 🐘 PostgreSQL database integration
* 📊 Structured code review results
* 📚 Interactive API documentation with Swagger UI
* 🔍 Detailed issue information including severity, line number, message, and error code
* 💾 Store code review results in PostgreSQL
* 🔄 Automatic server reload during development

## 🛠️ Tech Stack

| Technology     | Purpose                      |
| -------------- | ---------------------------- |
| **Python**     | Backend programming          |
| **FastAPI**    | REST API framework           |
| **Uvicorn**    | ASGI server                  |
| **PostgreSQL** | Database                     |
| **Bandit**     | Python security analysis     |
| **Ruff**       | Python code-quality analysis |
| **SQLAlchemy** | Database ORM                 |
| **Pydantic**   | Data validation              |

## 📂 Project Structure

```text
code-review-platform/
│
├── backend/
│   ├── app/
│   │   ├── analyzers/
│   │   │   └── python_analyzer.py
│   │   │
│   │   ├── routes/
│   │   │   └── review.py
│   │   │
│   │   ├── models/
│   │   │   └── ...
│   │   │
│   │   ├── schemas/
│   │   │   └── ...
│   │   │
│   │   ├── database.py
│   │   └── main.py
│   │
│   ├── requirements.txt
│   ├── .env
│   └── venv/
│
├── .gitignore
└── README.md
```

> **Important:** Never upload `venv/` or `.env` to GitHub.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/code-review-platform.git
```

### 2. Navigate to the Backend

```bash
cd code-review-platform/backend
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv bandit ruff
```

Or, if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## 🐘 PostgreSQL Setup

Make sure PostgreSQL is installed and running on your computer.

Create a PostgreSQL database for the application.

For example:

```sql
CREATE DATABASE code_review_db;
```

Then configure your database connection using an environment variable.

Create a `.env` file inside the `backend` folder:

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/code_review_db
```

Replace:

* `postgres` with your PostgreSQL username
* `your_password` with your PostgreSQL password
* `code_review_db` with your database name

> Never commit your `.env` file to GitHub because it contains database credentials.

## ▶️ Run the Application

From the `backend` directory:

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

FastAPI provides an interactive Swagger UI where you can test the API endpoints.

## 🔌 API Endpoint

### Create Code Review

```text
POST /reviews/
```

Example request:

```json
{
  "code": "import os\nos.system('echo Hello')"
}
```

## 📊 Example Response

```json
{
  "language": "python",
  "issues": [
    {
      "tool": "bandit",
      "test_id": "B605",
      "severity": "HIGH",
      "confidence": "HIGH",
      "message": "Starting a process with a shell, possible injection detected.",
      "line": 2
    },
    {
      "tool": "ruff",
      "code": "E501",
      "message": "Line too long",
      "line": 2,
      "column": 1
    }
  ],
  "total_issues": 2
}
```

## 🔄 Application Workflow

```text
User
  │
  ▼
Submit Python Code
  │
  ▼
FastAPI Backend
  │
  ├───────────────┐
  ▼               ▼
Bandit           Ruff
  │               │
  └───────┬───────┘
          ▼
   Combine Results
          │
          ▼
      PostgreSQL
          │
          ▼
    Review Response
```

## 🔍 Code Analysis

### Bandit

Bandit performs security-focused analysis of Python code and can detect potentially dangerous operations such as:

* Shell injection risks
* Unsafe system calls
* Insecure functions
* Security-related coding practices

### Ruff

Ruff performs fast Python linting and identifies issues such as:

* Unused imports
* Code-quality problems
* Style violations
* Potential programming errors

## 🗄️ Database

PostgreSQL is used to store code review information such as:

* Submitted code
* Programming language
* Detected issues
* Security findings
* Code-quality findings
* Review timestamps

## 🔒 Security

The project follows basic security practices:

* Environment variables are used for database credentials.
* `.env` is excluded from Git.
* Temporary Python files are deleted after analysis.
* User-submitted code is analyzed using isolated command-line tools.

> For production deployment, additional sandboxing and resource restrictions should be implemented before executing or analyzing untrusted code.

## 🚧 Future Improvements

* 🤖 AI-powered code review recommendations
* 🌐 Frontend integration
* 👤 User authentication
* 📜 Review history
* 🔗 GitHub repository integration
* 🔀 Pull Request code reviews
* 💬 AI-generated explanations
* 📈 Code-quality dashboard
* 🐳 Docker containerization
* ☁️ Cloud deployment
* 🔄 CI/CD integration
* 🧪 Automated testing
* 🔐 Secure code-execution sandbox

## 👩‍💻 Author

**Dhanashri Borse**

## 📄 License

This project is currently created for learning and development purposes.

---

⭐ If you find this project useful, consider giving the repository a star!
