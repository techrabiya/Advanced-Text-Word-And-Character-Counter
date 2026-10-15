import streamlit as st

st.set_page_config(page_title="Text Analyzer Tool", page_icon="🔤")

st.title("🔤 Advanced Text & Word Counter")
st.write("Paste your text below to get instant core metrics and analysis.")

text_input = st.text_area("Enter your text here:", "Python and Streamlit make building powerful web applications incredibly fast and fun!")

if text_input:
    words = len(text_input.split())
    chars = len(text_input)
    sentences = text_input.count('.') + text_input.count('!') + text_input.count('?')
    reading_time = round(words / 200, 2) # Average reading speed 200 words/min
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Words", words)
    col2.metric("Characters", chars)
    col3.metric("Sentences", max(sentences, 1))
    col4.metric("Est. Read Time (min)", reading_time)
    
    st.success("Core text analysis executed seamlessly!")
