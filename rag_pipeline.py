from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
import torch

# Load embedding model (BioBERT-based)
embedding_model = SentenceTransformer("pritamdeka/BioBERT-mnli-snli-scinli-scitail-mednli-stsb")
generator = pipeline("text2text-generation", model="google/flan-t5-large")

def embed_documents(documents):
    return embedding_model.encode(documents, convert_to_tensor=True)

def retrieve_relevant_docs(query, doc_embeddings, documents, top_k=3):
    query_embedding = embedding_model.encode(query, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(query_embedding, doc_embeddings)[0]
    top_results = torch.topk(similarities, k=top_k)
    return [documents[i] for i in top_results.indices]

def generate_response(query, context_docs):
    context = " ".join(context_docs)
    prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
    output = generator(prompt, max_length=512, do_sample=False)
    return output[0]['generated_text']
