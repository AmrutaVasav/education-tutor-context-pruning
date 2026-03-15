import streamlit as st
from context_pruning import prune_context

documents = open("dataset.txt").read().split("\n\n")

st.title("AI Education Tutor for Remote India")

question = st.text_input("Ask your question")

if question:
    answer = prune_context(question, documents)
    st.write("### Answer")
    st.write(answer)