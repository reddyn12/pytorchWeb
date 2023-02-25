from transformers import pipeline
import torch
import transformers.convert_graph_to_onnx as onnx_convert
from pathlib import Path
from transformers import GPT2Tokenizer, GPT2Model

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')
# text-generation
pipe = pipeline("text-generation", model="gpt2", feature_extractor="input_ids", max_length=100, num_return_sequences=1)

# t = pipe("I like corn because", max_length=100, num_return_sequences=5)
# print(t)
print(pipe("I love you so much"))
onnx_convert.convert_pytorch(pipe, opset=11, output=Path("gptNorm.onnx"), use_external_format=False)