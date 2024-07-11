import torch
print(torch.__version__)
from transformers import pipeline
import pandas as pd

tqa = pipeline(task="table-question-answering", model="google/tapas-base-finetuned-wtq")

table = pd.read