from transformers import pipeline

llm = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct"
)

def get_llm():
    return llm