import os
import torch

from customModel import GPTConfig, GPT
import customToken

ckpt_path = os.path.join("custOut", 'ckpt.pt')
checkpoint = torch.load(ckpt_path)
gptconf = GPTConfig(**checkpoint['model_args'])
model = GPT(gptconf)
state_dict = checkpoint['model']
unwanted_prefix = '_orig_mod.'
for k,v in list(state_dict.items()):
    if k.startswith(unwanted_prefix):
        state_dict[k[len(unwanted_prefix):]] = state_dict.pop(k)
model.load_state_dict(state_dict)
model.eval()

start_ids = customToken.tokenize("1 .")
t = (torch.tensor(start_ids, dtype=torch.long)[None, ...])
print(t)
torch.onnx.export(model, t,'testOnnx.onnx')