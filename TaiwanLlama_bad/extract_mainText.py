import json
import argparse
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, required=True)
    parser.add_argument("--output_file", type=str, required=True)
    args = parser.parse_args()
    return args

args = parse_args()

with open(args.input_file, "r", encoding="utf-8") as json_file:
    json_data = json_file.read()
    data_dict = json.loads(json_data)
    
data = []
for d in data_dict:
    mainText = d["mainText"]
    if "無罪" not in mainText and "駁回" not in mainText and "附表" not in mainText and "公訴" not in mainText:
        index = mainText.find("處")
        if index != -1:
            data.append({"kind" : d['sys'], "instruction" : mainText[:index-1], "output" : mainText[index:]})
            
print(len(data))
with open(args.output_file, "w", encoding="utf-8") as formatted_json_file:
    json.dump(data, formatted_json_file, ensure_ascii=False, indent=2)