import streamlit as st
import tempfile
import os
from graph import process_pdf

def main():
    st.set_page_config(page_title="Agentic RAG", layout="wide")
    st.title("Next-Gen Agentic RAG")

    with st.sidebar:
        st.header("Upload de Documentos")
        uploaded_file = st.file_uploader("Escolha um PDF técnico", type="pdf")

    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_path = tmp.name

        if st.sidebar.button("Processar e Indexar"):
            with st.spinner("Processando..."):
                chunks = process_pdf(tmp_path)
                st.session_state["chunks"] = chunks
                st.success(f"Sucesso: {len(chunks)} chunks gerados!")
        
        os.remove(tmp_path)

if __name__ == "__main__":
    main()