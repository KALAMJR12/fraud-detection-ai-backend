#  Fraud Detection AI Backend

A Flask-based backend that analyzes uploaded transaction files (e.g., CSV) to classify financial activities as **Low**, **Medium**, or **High Risk**, and prepares notifications for auditors.

Built during the **Africa's Talking Open Hackathon** — by (https://github.com/KALAMJR12).

---

## Features
- Upload and process transaction files (CSV)
- Rule-based fraud classification
- Ready for Hugging Face or IBM Granite LLM integration
- SMS notification layer via Africa’s Talking API (coming soon)
- Deployed with Render using Gunicorn (production-ready)

---

##  Tech Stack
- **Backend:** Flask (Python)
- **AI/ML:** Hugging Face / IBM Granite (optional)
- **Notifications:** Africa’s Talking SMS API
- **Deployment:** Render (free hosting)

---

##  Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/KALAMJR12/fraud-detection-ai-backend.git
cd fraud-detection-ai-backend

# 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate   # (Windows)
# or source venv/bin/activate (Mac/Linux)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
 
