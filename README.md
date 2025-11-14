🧠 Gemini AI Flashcard Generator

Automatically generate study flashcards from PDF, DOCX, or TXT files using Google Gemini AI.

🚀 Features

✔ Upload .pdf, .docx, or .txt notes
✔ Extract text automatically
✔ Generate 10–20 high-quality flashcards using Gemini 2.5 Flash
✔ Flip, shuffle, and navigate cards
✔ Download flashcards as CSV
✔ Clean dark UI built with Streamlit
✔ Ideal for students, revision, and AI-powered study tools

🛠️ Tech Stack

Python 3.10+

Streamlit

PyMuPDF (fitz)

python-docx

Pandas

Google Gemini API

📦 Installation
1️⃣ Clone the repository
git clone https://github.com/<your-username>/gemini-flashcards.git
cd gemini-flashcards

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add your Gemini API key

Inside the app, open the sidebar and paste your key.

Get a free API key here:
https://aistudio.google.com/app/apikey

▶️ Run the App
streamlit run app.py


Your browser will open automatically at:
http://localhost:8501

📁 Project Structure
gemini-flashcards/
│── app.py
│── requirements.txt
│── README.md
│── assets/  (optional: images/icons)

📸 Screenshot

(Add a screenshot later for professionalism)

💡 How It Works

Extracts text from uploaded PDFs, Word docs, or text files

Sends content to Gemini AI using generativeai

AI returns formatted flashcards

User can scroll, flip, and download them

🧪 Example Flashcard
Q: What is machine learning?
A: A subset of AI that allows systems to learn patterns from data.
