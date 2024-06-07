from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModel
import numpy as np
import warnings
from transformers import logging

logging.set_verbosity_error()
warnings.filterwarnings("ignore")

tokenizer = AutoTokenizer.from_pretrained("maymuni/bert-base-turkish-cased-emotion-analysis")
bert = AutoModel.from_pretrained("maymuni/bert-base-turkish-cased-emotion-analysis",return_dict=False)

class Arch(nn.Module):

    def __init__(self, bert):
      
      super(Arch, self).__init__()

      self.bert = bert 
      
      self.dropout = nn.Dropout(0.1)
      
      self.relu =  nn.ReLU()

      self.fc1 = nn.Linear(768,512)
      
      self.fc3 = nn.Linear(512,6)

      self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, sent_id, mask):
 
      _, cls_hs = self.bert(sent_id, attention_mask=mask, return_dict=False)

      x = self.fc1(cls_hs)

      x = self.relu(x)

      x = self.dropout(x)

      x = self.fc3(x)

      x = self.softmax(x)

      return x

model = Arch(bert)

path = r'C:\Users\Monster\Desktop\ai_proje\Turkish-Emotion-Analysis-main\model\turkish_emotion_analysis.pt'
model.load_state_dict(torch.load(path, map_location=torch.device('cpu')))

class Text(BaseModel):
    text: str

def filter(text):
    final_text = ''
    for word in text.split():
        if word.startswith('@'):
            continue
        elif word == 'RT':
            continue
        elif word[-3:] in ['com', 'org']:
            continue
        elif word.startswith('pic') or word.startswith('http') or word.startswith('www'):
            continue
        elif word.startswith('!') or word.startswith('&') or word.startswith('-'):
            continue
        else:
            final_text += word+' '
    return final_text

def predict_emotion(text):
  text = filter(text)
  tokenized = tokenizer.encode_plus(
    text,
    pad_to_max_length=True,
    truncation=True,
    return_token_type_ids=False
    )

  input_ids = tokenized['input_ids']
  attention_mask = tokenized['attention_mask']

  seq = torch.tensor(input_ids)
  mask = torch.tensor(attention_mask)
  seq = seq.unsqueeze(0)
  mask = mask.unsqueeze(0)
  preds = model(seq, mask)
  preds = preds.detach().cpu().numpy()
  result = np.argmax(preds, axis=1)
  preds = torch.tensor(preds)
  probabilities = nn.functional.softmax(preds)

  return {'anger':float(probabilities[0][0]),
          'surprise':float(probabilities[0][1]),
          'joy':float(probabilities[0][2]),
          'sadness':float(probabilities[0][3]),
          'fear':float(probabilities[0][4]),
          'disgust':float(probabilities[0][5])
          }

app = FastAPI()

@app.post("/predict", response_model=dict)
async def predict(text: Text):
    return predict_emotion(text.text)

@app.get("/", response_class=HTMLResponse)
async def read_item():
    with open("index.html", "r", encoding="utf-8") as file:
        return file.read()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
