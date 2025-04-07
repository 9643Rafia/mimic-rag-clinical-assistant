import os
import json

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_knowledge_graphs(kg_path):
    kg_files = [f for f in os.listdir(kg_path) if f.endswith(".json")]
    knowledge_graphs = {
        file: load_json(os.path.join(kg_path, file)) for file in kg_files
    }
    return knowledge_graphs

def load_annotated_samples(samples_path):
    samples_data = []
    for root, _, files in os.walk(samples_path):
        for file in files:
            if file.endswith(".json"):
                samples_data.append(load_json(os.path.join(root, file)))
    return samples_data
