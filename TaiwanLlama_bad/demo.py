import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, GenerationConfig
from peft import PeftModel
from peft.tuners.lora import LoraLayer
from utils import *
import argparse
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str, Lrequired=True)
    parser.add_argument("--adapter_path", type=str, required=True)
    args = parser.parse_args()
    return args

args = parse_args()
max_new_tokens = 256
top_p = 0.9
top_k = 10
temperature=0.7
model_name_or_path = args.model_path
adapter_path = args.adapter_path

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
tokenizer.bos_token_id = 1

model = AutoModelForCausalLM.from_pretrained(
    model_name_or_path,
    torch_dtype=torch.bfloat16,
    device_map={"": 0},
    load_in_4bit=True,
    quantization_config=get_bnb_config()
)

model = PeftModel.from_pretrained(model, adapter_path)
model.eval()

def generate(model, instruction, max_new_tokens=max_new_tokens, top_p=top_p, top_k=top_k, temperature=temperature):
    inputs = tokenizer(get_prompt(instruction=instruction), return_tensors="pt").to('cuda')
    outputs = model.generate(
        **inputs, 
        generation_config=GenerationConfig(
            do_sample=True,
            max_new_tokens=max_new_tokens,
            top_p=top_p,
            top_k=top_k,
            temperature=temperature,
        )
    )
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    index = text.find('ASSISTANT')
    answer = text[index+11:]
    print(answer)
    return answer

while True:
    instruction = input("輸入案例：")
    generate(model, instruction)
