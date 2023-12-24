
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, GenerationConfig
from peft import PeftModel
from peft.tuners.lora import LoraLayer
import json
import argparse
from utils import *
from tqdm import tqdm
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", type=str)
    parser.add_argument("--adapter_path", type=str)
    parser.add_argument("--input_file", type=str)
    parser.add_argument("--output_file", type=str)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    max_new_tokens = 256
    top_p = 0.9
    top_k = 10
    temperature=0.7
    model_name_or_path = args.model_path
    adapter_path = args.adapter_path

    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
    tokenizer.bos_token_id = 1
    bnb_config = get_bnb_config()
    model = AutoModelForCausalLM.from_pretrained(
        model_name_or_path,
        torch_dtype=torch.bfloat16,
        device_map={"": 0},
        load_in_4bit=True,
        quantization_config=bnb_config
    )

    model = PeftModel.from_pretrained(model, adapter_path)
    model.eval()
    result = []
    with open(args.input_file, "r") as f:
        data = json.load(f)
        for i in tqdm(range(len(data))):
            instruction = data[i]["instruction"]
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
            result.append({'instruction':instruction , "output":answer})
    json_result = json.dumps(result, ensure_ascii=False, indent=2)
    with open("output.json", "w", encoding="utf-8") as json_file:
        json_file.write(json_result)

if __name__ == "__main__":
    main()