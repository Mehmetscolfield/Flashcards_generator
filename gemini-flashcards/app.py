import streamlit as st
import fitz  # PyMuPDF
import docx
import random
import pandas as pd
import google.generativeai as genai

# -----------------------
# Helper Functions
# -----------------------
def extract_text(uploaded_file):
    """Extract text from PDF, DOCX, or TXT files."""
    if uploaded_file.name.endswith(".pdf"):
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            text = "".join(page.get_text() for page in doc)
    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        text = "\n".join(para.text for para in doc.paragraphs)
    elif uploaded_file.name.endswith(".txt"):
        text = uploaded_file.read().decode("utf-8")
    else:
        text = ""
    return text

def generate_flashcards(content):
    """Generate flashcards using Gemini AI."""
    if "api_key" not in st.session_state or not st.session_state.api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
        return None
    try:
        genai.configure(api_key=st.session_state.api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = f"""
You are a helpful AI that creates study flashcards.
Make 10–20 concise question–answer pairs from this text.

Format must be strictly:
Q: [Your question here]
A: [Your answer here]

Text:
{content}
"""
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def parse_flashcards(text):
    """Parse flashcards from AI response text into a list of dictionaries."""
    flashcards = []
    qa_pairs = text.strip().split('Q:')[1:]
    for pair in qa_pairs:
        try:
            question, answer = pair.split('A:')
            flashcards.append({"question": question.strip(), "answer": answer.strip()})
        except ValueError:
            continue
    return flashcards

def convert_to_csv(flashcards):
    """Convert flashcards list to CSV."""
    df = pd.DataFrame(flashcards)
    return df.to_csv(index=False).encode('utf-8')

# -----------------------
# Streamlit Page Setup
# -----------------------
st.set_page_config(page_title="Gemini AI Flashcard Generator", page_icon="🧠", layout="wide")

# Dark theme CSS
st.markdown("""
<style>
.stApp { background-color: #121212; color: white; }
.stButton>button { background-color: #4CAF50; color: white; border-radius: 12px; }
.stDownloadButton>button { background-color: #008CBA; color: white; border-radius: 12px; }
.stTextInput>div>div>input { border-radius: 12px; background-color: #1e1e1e; color: white; }
.flashcard { border-radius: 15px; padding: 25px; text-align: center; min-height: 200px; display: flex; justify-content: center; align-items: center; font-size: 20px; font-weight: bold; color: #ffffff; background: linear-gradient(to right, #1f1f1f, #333333); box-shadow: 0 8px 16px rgba(0,0,0,0.5); }
</style>
""", unsafe_allow_html=True)

st.title("🧠 Gemini AI Flashcard Generator")
st.write("Upload your notes or PDFs and automatically create flashcards using Google Gemini AI.")

# -----------------------
# Sidebar API Key Input
# -----------------------
with st.sidebar:
    st.session_state.api_key = st.text_input("Enter your Gemini API Key", type="password")
    if st.session_state.api_key:
        st.success("API Key configured!")
    else:
        st.warning("Please enter your Gemini API Key.")

# -----------------------
# File Uploader
# -----------------------
uploaded_file = st.file_uploader("Upload a .pdf, .docx, or .txt file", type=["pdf", "docx", "txt"])

# Initialize session state
for key in ['flashcards', 'card_index', 'flipped', 'extracted_text']:
    if key not in st.session_state:
        st.session_state[key] = [] if key == 'flashcards' else False if key == 'flipped' else "" if key == 'extracted_text' else 0

if uploaded_file:
    st.session_state.extracted_text = extract_text(uploaded_file)

# -----------------------
# Flashcard Controls
# -----------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Generate Flashcards", use_container_width=True):
        if st.session_state.extracted_text:
            with st.spinner("Generating flashcards..."):
                flashcards_text = generate_flashcards(st.session_state.extracted_text)
                if flashcards_text:
                    st.session_state.flashcards = parse_flashcards(flashcards_text)
                    st.session_state.card_index = 0
                    st.session_state.flipped = False
                    if not st.session_state.flashcards:
                        st.error("No flashcards generated. Check the AI output format.")
                    else:
                        st.rerun()
        else:
            st.error("Please upload a file first.")

with col2:
    if st.button("Regenerate", use_container_width=True):
        if st.session_state.extracted_text:
            with st.spinner("Regenerating flashcards..."):
                flashcards_text = generate_flashcards(st.session_state.extracted_text)
                if flashcards_text:
                    st.session_state.flashcards = parse_flashcards(flashcards_text)
                    st.session_state.card_index = 0
                    st.session_state.flipped = False
                    st.rerun()
        else:
            st.error("Please upload a file first.")

with col3:
    if st.session_state.flashcards:
        st.download_button(
            label="Download as CSV",
            data=convert_to_csv(st.session_state.flashcards),
            file_name="flashcards.csv",
            mime="text/csv",
            use_container_width=True
        )

with col4:
    if st.button("Clear", use_container_width=True):
        st.session_state.flashcards = []
        st.session_state.card_index = 0
        st.session_state.flipped = False
        st.rerun()

# -----------------------
# Flashcard Display
# -----------------------
if st.session_state.flashcards:
    st.header("Your Flashcards")

    nav_cols = st.columns([1,1,1,5])
    with nav_cols[0]:
        if st.button("⬅️ Previous", use_container_width=True):
            if st.session_state.card_index > 0:
                st.session_state.card_index -= 1
                st.session_state.flipped = False
                st.rerun()
    with nav_cols[1]:
        if st.button("Next ➡️", use_container_width=True):
            if st.session_state.card_index < len(st.session_state.flashcards) - 1:
                st.session_state.card_index += 1
                st.session_state.flipped = False
                st.rerun()
    with nav_cols[2]:
        if st.button("🔀 Shuffle", use_container_width=True):
            random.shuffle(st.session_state.flashcards)
            st.session_state.card_index = 0
            st.session_state.flipped = False
            st.rerun()

    st.write(f"Card {st.session_state.card_index + 1} of {len(st.session_state.flashcards)}")
    
    card_placeholder = st.empty()
    card = st.session_state.flashcards[st.session_state.card_index]

    if not st.session_state.flipped:
        with card_placeholder.container():
            st.markdown(f"<div class='flashcard'>{card['question']}</div>", unsafe_allow_html=True)
    else:
        with card_placeholder.container():
            st.markdown(f"<div class='flashcard'>{card['answer']}</div>", unsafe_allow_html=True)

    if st.button("Flip Card", use_container_width=True):
        st.session_state.flipped = not st.session_state.flipped
        st.rerun()
