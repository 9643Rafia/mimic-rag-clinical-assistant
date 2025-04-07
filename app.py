import streamlit as st
from data_loader import load_knowledge_graphs, load_annotated_samples
from rag_pipeline import embed_documents, retrieve_relevant_docs, generate_response

# Set your dataset paths
diagnostic_kg_path = "path/to/Diagnosis_flowchart"
samples_path = "path/to/Finished"

st.title("🧠 Clinical Assistant (RAG + MIMIC-IV)")

@st.cache_data
def load_data():
    knowledge_graphs = load_knowledge_graphs(diagnostic_kg_path)
    samples_data = load_annotated_samples(samples_path)
    documents = [sample["note"] for sample in samples_data]
    doc_embeddings = embed_documents(documents)
    return documents, doc_embeddings

documents, doc_embeddings = load_data()

query = st.text_input("Enter a clinical question:")
if query:
    st.write("🔍 Searching...")
    top_docs = retrieve_relevant_docs(query, doc_embeddings, documents)

    st.subheader("📄 Retrieved Documents")
    for doc in top_docs:
        st.text_area(label="", value=doc, height=120)

    st.subheader("✍️ Generated Answer")
    answer = generate_response(query, top_docs)
    st.success(answer)
