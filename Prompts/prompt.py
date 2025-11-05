import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables (make sure GROQ_API_KEY is in your .env file)
load_dotenv()

# --- Model Initialization ---
# Initialize the Groq Chat model
# We'll use a fast model like llama-3.1-8b-instant
try:
    llm = ChatGroq(model_name="llama-3.1-8b-instant")
except Exception as e:
    st.error(f"Error initializing Groq model: {e}")
    st.error("Please make sure your GROQ_API_KEY is set in your .env file.")
    llm = None  # Set llm to None so the app doesn't crash

# --- Streamlit App UI ---
st.header('Research Paper Summary Tool 📄')

# --- Inputs ---

# 1. Paper Name Dropdown
# (You can expand this list with any papers you want)
paper_list = [
    "Attention Is All You Need (Transformer)",
    "Generative Adversarial Networks (GANs)",
    "Deep Residual Learning for Image Recognition (ResNet)",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "PageRank: A Hypertext-Induced Topic-Sensitive Ranking",
    "Mastering the game of Go with deep neural networks (AlphaGo)",
    "A Method for Stochastic Optimization (Adam)"
]
selected_paper = st.selectbox(
    'Select a research paper:',
    options=paper_list,
    key='paper_select'
)

# 2. Level Dropdown
level_options = ['Beginner-Friendly', 'Technical', 'Advanced Expert']
selected_level = st.selectbox(
    'Select expertise level:',
    options=level_options,
    key='level_select'
)

# 3. Length Dropdown
length_options = ['Short Summary (1-2 sentences)', 'Detailed Paragraph', 'Key Bullet Points (3-5 points)']
selected_length = st.selectbox(
    'Select desired length/format:',
    options=length_options,
    key='length_select'
)

# --- Button and Logic ---

if st.button('Generate Research Summary', disabled=(llm is None)):
    if llm:
        # 1. Formulate a clear prompt from the inputs
        prompt = f"""
        Please generate a summary for the research paper: "{selected_paper}".

        Follow these instructions:
        1.  **Expertise Level:** The summary should be written at a "{selected_level}" level.
        2.  **Format/Length:** The output should be a "{selected_length}".

        Generate the summary based on these requirements.
        """
        
        # 2. Show a spinner while the model is working
        with st.spinner(f'Generating {selected_level} summary...'):
            try:
                # 3. Invoke the Groq model
                result = llm.invoke(prompt)
                
                # 4. Display the result
                st.subheader(f"Summary for: {selected_paper}")
                st.write(result.content)
                
            except Exception as e:
                st.error(f"An error occurred while generating the summary: {e}")
    else:
        st.error("The language model is not available. Please check your API key and setup.")
