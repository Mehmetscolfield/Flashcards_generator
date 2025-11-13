# Gemini AI Flashcard Generator

Upload your notes or PDFs and automatically create flashcards using Google Gemini AI. Study smarter with instant Q&A cards and exportable decks.

## Features

*   **File Upload**: Upload .pdf, .docx, or .txt files.
*   **AI-Powered Flashcards**: Automatically generate question-answer pairs using Google Gemini.
*   **Interactive Viewer**: Flip through flashcards one by one.
*   **Navigation**: "Next," "Previous," and "Shuffle" buttons.
*   **Export**: Download your flashcards as a .csv file.

## Tech Stack

*   **Frontend**: Streamlit
*   **Backend**: Python
*   **AI**: Google Gemini
*   **Dependencies**: `streamlit`, `google-generativeai`, `PyMuPDF`, `python-docx`, `pandas`

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/gemini-flashcards.git
    cd gemini-flashcards
    ```

2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Get a Gemini API Key:**
    *   Go to [Google AI Studio](https://aistudio.google.com/) and create a free API key.

4.  **Run the app:**
    ```bash
    streamlit run app.py
    ```

## How to Use

1.  Enter your Gemini API Key in the sidebar.
2.  Upload a .pdf, .docx, or .txt file.
3.  Click "Generate Flashcards."
4.  Use the "Next," "Previous," and "Shuffle" buttons to navigate through your flashcards.
5.  Click "Flip Card" to see the answer.
6.  Click "Download as CSV" to save your flashcards.

## Screenshots

*(Add screenshots of the app here)*
