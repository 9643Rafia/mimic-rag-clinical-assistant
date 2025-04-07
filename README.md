# mimic-rag-clinical-assistant
# 🧠 Clinical RAG Assistant using MIMIC-IV-Ext-Direct

This project implements a **Retrieval-Augmented Generation (RAG)** system designed to answer clinical questions using the [MIMIC-IV-Ext-Direct](https://physionet.org/content/mimic-iv-ext-direct/) dataset. It combines a powerful retriever (based on `sentence-transformers`) and a generative model (`Flan-T5`) to produce medically-informed responses.

## 🚀 Features

- ✅ Semantic document retrieval from MIMIC-IV-Ext-Direct
- ✅ Generative QA using Hugging Face Transformers
- ✅ Fully interactive **Streamlit frontend**
- ✅ Clean, modular Python code

## 📁 Project Structure

. ├── app.py # Streamlit interface ├── rag_pipeline.py # Retrieval + Generation logic ├── data_loader.py # Dataset loading (knowledge graphs, samples) ├── notebooks/ │ └── assignemnet5_gen.ipynb ├── requirements.txt └── README.md


## 💡 Example Query

> **"What are the diagnostic steps for chest pain?"**

**Output:**
> Based on the provided notes, chest pain is assessed via ECG, cardiac enzymes, and patient history. A follow-up includes imaging and rule-out of acute coronary syndrome.

## 🧪 Installation

```bash
git clone https://github.com/your-username/mimic-rag-clinical-assistant.git
cd mimic-rag-clinical-assistant
pip install -r requirements.txt
streamlit run app.py

## Dataset
To run the app, you must have access to the MIMIC-IV-Ext-Direct dataset. Please place it in the expected directories inside your Google Drive or local machine.

📄 License
This project is for academic use only. Respect privacy guidelines when handling healthcare data.

👤 Author
Rafia Zubair

Blog post on Medium: Building a Clinical RAG Assistant

