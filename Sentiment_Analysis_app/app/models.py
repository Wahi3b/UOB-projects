from app import db
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

def load_model():
    tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    return model, tokenizer

def predict(model, tokenizer, text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_class_id = logits.argmax().item()
    prediction_label = model.config.id2label[predicted_class_id]
    return prediction_label



